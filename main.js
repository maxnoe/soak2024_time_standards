function toMJD(d) {
  return (d.valueOf() / 86400e3 + 40587.0).toFixed(6).padStart(14, " ");
}

function toJD(d) {
  return (d.valueOf() / 86400e3 + 2440587.5).toFixed(6);
}

const I32_MAX = Math.pow(2, 31) - 1; 
const U32_MAX = Math.pow(2, 32);

function overflow() {
  t = (moment().tz("UTC").valueOf() / 1e3) % 20 - 15;
  t = Math.floor(Math.pow(2, 31) + t);
  if (t > I32_MAX) {
    t -= U32_MAX;
  }
  return t;
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
  const unix_overflow = document.getElementById("unix-overflow");

  window.setInterval(() => {
    const now = moment();
    iso_utc.innerHTML = now.tz('UTC').format("YYYY-MM-DDTHH:mm:ss.SSS") + "Z";
    iso_local.innerHTML = now.tz("Europe/Berlin").format("YYYY-MM-DDTHH:mm:ss.SSSZ");
    unix.innerHTML = now.tz("UTC").valueOf() / 1e3;
    mjd.innerHTML = toMJD(now.tz("UTC"));
    jd.innerHTML = toJD(now.tz("UTC"));

    t = overflow();
    unix_overflow.innerHTML = (t >>> 0).toString(2).padStart(32, "0") + ' ⇒ ' +  moment(t * 1e3).tz("UTC").format();
  }, 100);
});
