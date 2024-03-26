$(document).ready(function () {
  clockUpdate();
  setInterval(clockUpdate, 1000);
});

function padZero(x) {
  return x < 10 ? `0${x}` : x;
}

function base12(x) {
  if (x > 12) {
    x = x - 12;
  } else if (x == 0) {
    x = 12;
  }
  return x;
}

function formatTime(dt, seconds) {
  const h = padZero(base12(dt.getHours()));
  const m = padZero(dt.getMinutes());
  const s = padZero(dt.getSeconds());
  const suffix = dt.getHours() > 12 ? "PM" : "AM";

  return `${h}:${m}:${s} <small>${suffix}</small>`;
}

function clockUpdate() {
  let clock_html;
  const container_style =
    'style="display: grid;grid-template-columns: auto auto;justify-items: stretch;justify-content: space-between;"';
  const container_item_style = 'style="font-weight:bold;font-size:large;"';
  const is_multi_clock =
    frappe.boot.time_zone.user &&
    frappe.boot.time_zone.user != frappe.boot.time_zone.system;

  if (is_multi_clock) {
    const now_user = new Date(frappe.datetime.convert_to_user_tz());
    const now_sys = new Date(frappe.datetime.convert_to_system_tz());
    clock_html = `
      <div ${container_style}>
        <div>User:</div><div ${container_item_style}>${formatTime(
          now_user,
        )}</div>
        <div>Site:</div><div>${formatTime(now_sys)}</div>
        </div>`;
  } else {
    const now_user = new Date(frappe.datetime.convert_to_user_tz());
    clock_html = `<div ${container_style}>
      <div>Time:</div><div ${container_item_style}>${formatTime(now_user)}</div>
      </div>`;
  }

  $("#desk-navbar-extended-clock").html(`<div>${clock_html}</div>`);
}

setTimeout(() => {
  $(".dropdown-navbar-user a:contains('Show Time')").attr(
    "id",
    "desk-navbar-extended-clock",
  );
  $(".dropdown-navbar-user button:contains('Show Time')").attr(
    "id",
    "desk-navbar-extended-clock",
  );
}, 1000);
