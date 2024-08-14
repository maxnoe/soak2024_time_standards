import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles

plt.style.use("dark_background")
plt.rcParams["font.family"] = "Fira Sans"

fig, ax = plt.subplots(layout="constrained")

v = venn3(
    subsets=(1, 1, 1, 1, 1, 1, 1),
    set_labels=('', '', ''),
)

v.get_label_by_id('100').set_text("Erdrotation")
v.get_label_by_id('010').set_text("SI-Sekunde")
v.get_label_by_id('001').set_text("Kontinuierlich")

v.get_label_by_id('110').set_text("UTC")
v.get_label_by_id('101').set_text("UT1")
v.get_label_by_id('011').set_text("TAI")

v.get_label_by_id('111').set_text("Unmöglich")

for label in "ABC":
    v.get_label_by_id(label).set_text("")

fig.savefig('build/standards_venn.svg', transparent=True)
