// Print / PDF support. Paper can't be clicked, so when printing:
//  - switch to the light colour scheme,
//  - open every collapsible box,
//  - show every tab of a tab group, each under its own label.
// Runs on browser Print (any page) and always on the print page with #pdf
// in the URL (used by scripts/make_pdf.py, where no print event fires).

(function () {
  let saved = null;

  function addTabLabels() {
    // once per page: a label above each tab's content, only visible in print
    document.querySelectorAll(".tabbed-set").forEach((set) => {
      if (set.dataset.printLabels) return;
      set.dataset.printLabels = "1";
      const labels = set.querySelectorAll(":scope > .tabbed-labels > label");
      const blocks = set.querySelectorAll(":scope > .tabbed-content > .tabbed-block");
      blocks.forEach((block, i) => {
        if (!labels[i]) return;
        const p = document.createElement("p");
        p.className = "print-tab-label";
        p.textContent = labels[i].textContent.trim();
        block.prepend(p);
      });
    });
  }

  function enterPrint() {
    if (saved) return;
    addTabLabels();
    saved = {
      scheme: document.body.getAttribute("data-md-color-scheme"),
      closed: [...document.querySelectorAll("details:not([open])")],
    };
    document.body.setAttribute("data-md-color-scheme", "default");
    saved.closed.forEach((d) => d.setAttribute("open", ""));
  }

  function leavePrint() {
    if (!saved) return;
    if (saved.scheme) document.body.setAttribute("data-md-color-scheme", saved.scheme);
    saved.closed.forEach((d) => d.removeAttribute("open"));
    saved = null;
  }

  function dropEmptySections() {
    // Menu groups whose pages are all excluded from print (e.g. "For editors")
    // leave a heading with nothing under it: remove it and its contents entry.
    document.querySelectorAll("#print-site-page section.md-section").forEach((sec) => {
      const next = sec.nextElementSibling;
      if (next && !next.classList.contains("md-section")) return;
      document
        .querySelectorAll(`#print-page-toc a[href="#${sec.id}"]`)
        .forEach((a) => (a.closest("li") || a).remove());
      sec.remove();
    });
  }

  document.addEventListener("DOMContentLoaded", dropEmptySections);
  window.addEventListener("beforeprint", enterPrint);
  window.addEventListener("afterprint", leavePrint);

  if (location.hash === "#pdf") {
    // after Material has applied the saved palette
    window.addEventListener("load", enterPrint);
    document.addEventListener("DOMContentLoaded", enterPrint);
  }
})();
