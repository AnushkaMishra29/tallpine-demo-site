// Swan visitor identification: paste the snippet from your Swan account here, once.
// Every page of the site loads this file, so one paste covers the whole site.
//
// How: in Swan, open the website-tracking (or "install script") screen and copy the snippet.
//   - If Swan gives you a <script> tag with JavaScript inside it, paste only the JavaScript between the tags below.
//   - If Swan gives you a tag like <script src="https://...some-id.js" async></script>, set SWAN_SRC to that address.
//
// The engine keeps only the company match from Swan (never a person), and nothing is ever sent on a visit alone.
(function () {
  "use strict";
  var SWAN_SRC = "";   // e.g. "https://.../your-site-id.js"
  if (SWAN_SRC) {
    var s = document.createElement("script");
    s.async = true;
    s.src = SWAN_SRC;
    document.head.appendChild(s);
  }
  // --- or paste Swan's inline JavaScript below this line ---

})();
