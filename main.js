function toMJD(d) {
  return (d.valueOf() / 86400e3 + 40587.0).toFixed(6).padStart(14, " ");
}

function toJD(d) {
  return (d.valueOf() / 86400e3 + 2440587.5).toFixed(6);
}

Reveal.initialize({
  hash: true,
  slideNumber: true,
  plugins: [
    RevealHighlight,
    RevealMath.KaTeX,
    RevealZoom,
  ],
  width: 960,
  height: 600,
  zoomLevel: 5,
}).then(() => {
  const iso_utc = document.getElementById("current-iso-utc");
  const iso_local = document.getElementById("current-iso-local");
  const unix = document.getElementById("current-unix");
  const jd = document.getElementById("current-jd");
  const mjd = document.getElementById("current-mjd");

  window.setInterval(() => {
    const now = moment();
    iso_utc.innerHTML = now.tz('UTC').format();
    iso_local.innerHTML = now.tz("Europe/Berlin").format();
    unix.innerHTML = now.valueOf() / 1e3;
    mjd.innerHTML = toMJD(now);
    jd.innerHTML = toJD(now);
  }, 100);
});
