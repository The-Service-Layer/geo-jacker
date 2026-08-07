(function () {
  "use strict";

  // Mobile nav
  var btn = document.querySelector(".nav-toggle");
  var nav = document.getElementById("mainnav");
  if (btn && nav) {
    btn.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      btn.textContent = open ? "Close" : "Menu";
    });
  }

  // Copy buttons on code blocks
  document.querySelectorAll("pre[data-copy]").forEach(function (pre) {
    var b = document.createElement("button");
    b.type = "button";
    b.className = "btn btn-ghost";
    b.style.cssText = "margin:-1rem 0 1.8rem;font-size:.6rem;padding:.45rem .7rem";
    b.textContent = "Copy";
    b.addEventListener("click", function () {
      navigator.clipboard.writeText(pre.innerText).then(function () {
        b.textContent = "Copied";
        setTimeout(function () { b.textContent = "Copy"; }, 1800);
      });
    });
    pre.insertAdjacentElement("afterend", b);
  });

  // Current year in footer
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
