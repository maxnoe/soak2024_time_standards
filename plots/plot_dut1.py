import astropy.units as u
from astropy.time import Time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.dates import DateFormatter, YearLocator
from matplotlib.colors import to_rgba
from matplotlib.lines import Line2D

plt.style.use("dark_background")


t0 = Time("1972-01-01T00:00:00", scale='utc')
t1 = Time.now() + 1 * u.year

dt = (t1 - t0).to_value(u.day)

t = t0 + np.arange(0, dt + 1, 1) * u.day

dut1 = t.get_delta_ut1_utc()

# dut1 = 86400 * ((t.ut1.jd1 - t.utc.jd1) + (t.ut1.jd2 - t.utc.jd2))

fig, ax = plt.subplots(layout="constrained", figsize=(8, 4))

x = t.tai.plot_date
y = dut1.to_value(u.s)

leap_occured = np.nonzero(np.abs(np.diff(y) > 0.5))[0]
segments = []
previous_leap = 0
colors = []
widths = []
styles = []
for idx in leap_occured:
    sl = slice(previous_leap + 1, idx + 1)

    segments.append(np.column_stack([x[sl], y[sl]]))
    widths.append(2)
    colors.append(to_rgba('C0'))
    styles.append('-')

    segments.append(np.column_stack([x[idx:idx+2], y[idx:idx+2]]))
    colors.append(to_rgba('C1'))
    widths.append(1)
    styles.append('--')


    previous_leap = idx

x_after = x[idx+1:]
y_after = y[idx+1:]

future = x_after > Time.now().plot_date

segments.append(np.column_stack([x_after[~future], y_after[~future]]))
colors.append(to_rgba('C0'))
widths.append(2)
styles.append('-')

segments.append(np.column_stack([x_after[future], y_after[future]]))
colors.append(to_rgba('C2'))
widths.append(2)
styles.append('-')


lines = LineCollection(segments, color=colors, linewidth=widths, linestyle=styles)

ax.legend(
    [
        Line2D([], [], linestyle='-', color='C0'),
        Line2D([], [], linestyle='-', color='C2'),
        Line2D([], [], linestyle='--', color='C1'),
    ],
    ["Messung", "Vorhersage", "Schaltsekunde"],
    ncol=3,
    bbox_to_anchor=(0.5, 1.01),
    loc="lower center",
)

ax.add_collection(lines)
ax.xaxis.set_major_formatter(DateFormatter("%Y"))
ax.xaxis.set_major_locator(YearLocator(5))
ax.xaxis.set_minor_locator(YearLocator())

ax.annotate("2016-12-31T23:59:60", (x[idx+1], y[idx+1]), xytext=(-5, 0), textcoords='offset points', ha='right', va='center', color='C1' )
ax.set(
    xlim=(0.95 * x.min(), 1.05 * x.max()),
    ylim=(-1, 1),
    ylabel="(UT1 – UTC) / s",
)

fig.savefig("build/dut1.svg", transparent=True)
