// Forms: send the fields to the matching HubSpot form (the public Forms API; no secret is needed or stored here).
// The inbound engine reads the submission from HubSpot on its next cycle and stages the reply for a person.
(function () {
  "use strict";
  var params = new URLSearchParams(location.search);

  document.querySelectorAll("form[data-hs-form]").forEach(function (form) {
    // A board-question page links here with ?question=q-value: pre-select it, as the page promised.
    var q = params.get("question"), sel = form.querySelector('[name="board_question"]');
    if (q && sel && sel.querySelector('option[value="' + q + '"]')) sel.value = q;

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = form.querySelector(".status"), button = form.querySelector("button[type=submit]");
      status.className = "status";
      if (!form.checkValidity()) {
        status.textContent = "Please fill in the fields marked with a star, with a valid email address.";
        status.classList.add("err");
        var bad = form.querySelector(":invalid");
        if (bad) bad.focus();
        return;
      }
      var fields = [];
      new FormData(form).forEach(function (value, name) {
        if (String(value).trim() !== "") fields.push({ name: name, value: String(value).trim() });
      });
      // Made-up companies use ".example" addresses, which HubSpot rejects as invalid. Adding ".example.com" keeps
      // the address undeliverable and lets HubSpot accept it; the engine strips the suffix again when it reads it.
      fields.forEach(function (f) {
        if (f.name === "email" && /\.(example|test)$/i.test(f.value)) f.value = f.value.replace(/\.test$/i, "") + ".example.com";
      });
      var box = form.querySelector('[name="briefings_opt_in"]');
      if (box && !box.checked) fields.push({ name: "briefings_opt_in", value: "false" });
      // Where the visitor came from, so the reply can lead with the right question.
      if (!fields.some(function (f) { return f.name === "source_page"; })) {
        fields.push({ name: "source_page", value: q ? "board question page: " + q : (document.referrer ? new URL(document.referrer).pathname : "direct") });
      }
      var url = "https://api.hsforms.com/submissions/v3/integration/submit/" +
                form.dataset.hsPortal + "/" + form.dataset.hsForm;
      button.disabled = true;
      status.textContent = "Sending…";
      fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ fields: fields, context: { pageUri: location.href, pageName: document.title } })
      }).then(function (res) {
        if (!res.ok) return res.text().then(function (t) {
          var e = new Error("HubSpot answered " + res.status + ": " + t.slice(0, 300));
          e.refused = true;
          e.badEmail = /INVALID_EMAIL|BLOCKED_EMAIL/.test(t);
          throw e;
        });
        form.reset();
        status.textContent = "Thank you. Your request is in, and a person will reply within one business day.";
        status.classList.add("ok");
      }).catch(function (err) {
        // Say what actually went wrong, so the person can fix it.
        if (err.badEmail) {
          status.textContent = "That email address was not accepted. For this demonstration use a made-up address " +
                               "ending in .example, such as name@corvane.example.";
        } else if (err.refused) {
          status.textContent = "The form service did not accept this request. Please check the fields and try again.";
        } else {
          status.textContent = "Your browser blocked the request before it was sent. An ad blocker or privacy " +
                               "shield often does this: switch it off for this site, or try another browser.";
        }
        status.classList.add("err");
        console.error(err);
      }).finally(function () { button.disabled = false; });
    });
  });
})();
