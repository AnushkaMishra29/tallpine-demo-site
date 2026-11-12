# Tallpine demo site

Tallpine is a made-up company. This small static site exists for a portfolio project: it gives a
visitor-identification script real pages to watch, and its forms post real submissions into a HubSpot test portal,
where an inbound engine routes each one and stages a reply for a person to send.

- `build.py` writes every page (`python build.py`, no dependencies).
- `assets/site.js` sends each form to its HubSpot form through the public Forms API. No secret is stored here.
- `assets/swan.js` is the one place to paste the Swan snippet.

Please enter made-up details in the forms.
