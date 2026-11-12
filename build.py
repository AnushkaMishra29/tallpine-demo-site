"""Build the Tallpine demo site: plain static pages, no dependencies.   python build.py

Tallpine is a made-up company. The site exists so a visitor-identification script (Swan) has real pages to watch and
so its forms can post real submissions into a HubSpot test portal, where the inbound engine picks them up.
Every page loads assets/swan.js (paste the Swan snippet there, once) and assets/site.js (the forms).
All wording is original to this site.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).parent
PORTAL = "247337201"                      # HubSpot free test portal (no client data)
FORMS = {                                 # the showcase engine's own forms (rules/hubspot.toml [forms])
    "demo": "ae0accee-f077-484c-9c95-a82de2780045",
    "kit": "02e1e0cd-4fad-4987-a869-7b78e11d5ce7",
    "contact": "8ef20014-e2f1-4f54-877a-19576ec3502b",
}

ICON = {   # simple line icons, 24x24, drawn here so the site loads nothing from elsewhere
    "compass": '<circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5z"/>',
    "list": '<path d="M9 6h11M9 12h11M9 18h11"/><path d="m4 6 1 1 2-2M4 12l1 1 2-2M4 18l1 1 2-2"/>',
    "people": '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c.6-3.4 3-5 6-5s5.4 1.6 6 5"/><path d="M16 5.2a3.2 3.2 0 0 1 0 5.6M18 15.4c1.7.7 2.7 2.2 3 4.6"/>',
    "chart": '<path d="M4 20V4M4 20h16"/><path d="m7 15 4-4 3 3 5-6"/>',
    "plug": '<path d="M9 3v5M15 3v5M7 8h10v3a5 5 0 0 1-10 0zM12 16v5"/>',
    "shield": '<path d="M12 3 5 6v5c0 4.4 2.9 8.2 7 10 4.1-1.8 7-5.6 7-10V6z"/><path d="m9 12 2 2 4-4"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m4 7 8 6 8-6"/>',
    "coins": '<ellipse cx="9" cy="7" rx="5" ry="2.5"/><path d="M4 7v5c0 1.4 2.2 2.5 5 2.5M4 12v5c0 1.4 2.2 2.5 5 2.5"/><ellipse cx="15" cy="13" rx="5" ry="2.5"/><path d="M10 13v5c0 1.4 2.2 2.5 5 2.5s5-1.1 5-2.5v-5"/>',
    "box": '<path d="m3 8 9-5 9 5v8l-9 5-9-5z"/><path d="m3 8 9 5 9-5M12 13v8"/>',
}


def icon(name):
    return (f'<svg class="icon" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" '
            f'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[name]}</svg>')


GUIDES = [   # (form value, address, title, one-line summary, icon, paragraphs, three takeaways)
    ("q-value", "ai-spending-paying-off", "Is our AI spending paying off?",
     "Most leadership teams can list what they spent on AI. Far fewer can show what came back.", "coins",
     ["Spending is the easy half to count: licences, cloud bills and the hours your people put in. The other half is "
      "harder, because the benefit turns up inside other teams' work and nobody is asked to write it down.",
      "A useful answer starts with one page per project. It says who is responsible, what the starting point was, "
      "what the project was meant to change, and what has been measured since.",
      "With that in place, the update to your board becomes a short list: projects that have delivered, projects "
      "that are still a forecast, and projects you stopped, with the reason."],
     ["Give every project a named owner and a starting point", "Keep forecasts and measured results apart",
      "Report stopped projects too, with the reason"]),
    ("q-strategy", "ai-changing-strategy", "How is AI changing strategy?",
     "When almost anything can be built in a week, deciding what not to build becomes the real work.", "compass",
     ["Teams now pitch more AI projects in a quarter than they used to in a year. Without a common way to compare "
      "them, the best-argued pitch wins, which is not always the most useful one.",
      "The fix is simple and takes discipline: agree a handful of priority themes for the year, then ask every "
      "proposal the same few questions before it gets time or money.",
      "Strategy then stops being a yearly document. It becomes a short weekly review with a clear yes or no and a "
      "written reason either way."],
     ["Agree a few priority themes for the year", "Ask every proposal the same questions",
      "Write down each yes and each no"]),
    ("q-people", "ai-and-our-people", "What does AI mean for our people?",
     "A tool that nobody uses changes nothing. Adoption has to be planned like any other part of the work.", "people",
     ["Every AI project is really a change to how a specific group of people works. Naming that group at the start, "
      "and how many of them need to be on board, makes the plan honest.",
      "Usage is best read from the systems people already work in. That way nobody fills in a survey, and nobody "
      "has to guess.",
      "When usage stalls, the project owner should see it in the same place as the budget and the timeline, early "
      "enough to do something about it."],
     ["Name the people each project is meant to help", "Read usage from the tools they already use",
      "Show usage next to budget and timeline"]),
    ("q-agents", "what-agents-cost", "What do AI agents really cost?",
     "Agents are cheap to start and easy to forget. The bill arrives later, and it is rarely tied to a result.", "chart",
     ["Running costs grow with every agent a team switches on, and they are usually reported somewhere different "
      "from the benefits.",
      "Putting the two side by side for each project changes the conversation. A team can see what an agent costs "
      "to run next to what it has delivered so far.",
      "The least expensive agent is the one that is never started on an idea that was not ready. A short review "
      "before anything is switched on pays for itself."],
     ["Report running cost per project, not per tool", "Show cost beside results",
      "Review an idea before any agent is switched on"]),
]
BUYING = [
    ("product-status", "Product status", "A plain list of what is available today, what arrives through connectors, "
     "and what is still planned.", "list",
     [("Available now", "Priority themes, proposal review, review checkpoints, usage tracking and the project record.", "now"),
      ("Through connectors", "Progress and usage data from your work-management and sign-in tools, set up during onboarding.", "conn"),
      ("Planned", "Board-report drafts and running-cost tracking for agents. We label these as planned until they "
                  "ship, and we do not publish dates here.", "plan")]),
    ("packaging", "Packaging", "Tallpine is scoped by how much of the company it covers, never by the number of seats.", "box",
     [("Start with one team", "Most customers begin with a single business unit and a pilot quarter.", ""),
      ("Widen when it works", "More units join as the first one shows results. The scope is what you manage, not who logs in.", ""),
      ("Numbers in conversation", "We share figures once the scope is clear, in a conversation, not on a web page.", "")]),
    ("integrations", "Integrations", "Tallpine reads from the systems your teams already use, so nobody re-enters their work.", "plug",
     [("Work management", "Project and ticketing tools supply progress and ownership.", ""),
      ("Usage", "Sign-in and activity data show whether people are using what was built.", ""),
      ("Reporting", "Results are compared with the figures your finance team already reports.", "")]),
    ("trust", "Trust", "How we handle your data, and what we will and will not claim.", "shield",
     [("Your data stays yours", "Each customer's data is kept separate and is never used to train shared models.", ""),
      ("Plain answers", "If we do not hold a certification, we say so and tell you what we have in its place.", ""),
      ("A named person", "Security and compliance questions go to a named person, and you get a written reply.", "")]),
]
NAV = [("product-status/index.html", "Product"), ("resources/index.html", "Guides"),
       ("packaging/index.html", "Packaging"), ("trust/index.html", "Trust"), ("contact/index.html", "Contact")]
COUNTRIES = ["United States", "Canada", "United Kingdom", "Germany", "France", "India", "Australia", "Other"]
LOGO = ('<svg viewBox="0 0 28 28" width="28" height="28" aria-hidden="true"><path d="M14 2 24 20H4z" fill="#0f766e"/>'
        '<path d="M14 9 21 22H7z" fill="#14213d" opacity=".9"/><rect x="12.4" y="21" width="3.2" height="5" rx="1" fill="#14213d"/></svg>')


def page(path, title, body, lede=""):
    up = "../" * path.count("/")
    nav = "".join(f'<a href="{up}{href}">{escape(label)}</a>' for href, label in NAV)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} · Tallpine</title>
<meta name="description" content="{escape(lede or title)}">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="{up}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{up}assets/style.css">
<script src="{up}assets/swan.js" defer></script>
<script src="{up}assets/site.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="notice"><div class="wrap">Demonstration site for a portfolio project. Tallpine is a made-up company. <a href="{up}about/index.html">About this site</a></div></div>
<header class="top"><div class="wrap bar">
  <a class="brand" href="{up}index.html" aria-label="Tallpine home">{LOGO}<span>Tallpine</span></a>
  <nav aria-label="Main">{nav}</nav>
  <a class="btn small" href="{up}demo/index.html">Request a demo</a>
</div></header>
<main id="main">
{body}
</main>
<footer><div class="wrap">
  <div class="fgrid">
    <div><a class="brand light" href="{up}index.html">{LOGO}<span>Tallpine</span></a>
      <p>The planning and review workspace for company AI programs.</p></div>
    <div><h4>Product</h4><a href="{up}product-status/index.html">Product status</a><a href="{up}packaging/index.html">Packaging</a>
      <a href="{up}integrations/index.html">Integrations</a><a href="{up}trust/index.html">Trust</a></div>
    <div><h4>Guides</h4>{"".join(f'<a href="{up}resources/{g[1]}/index.html">{escape(g[2])}</a>' for g in GUIDES)}</div>
    <div><h4>Get in touch</h4><a href="{up}demo/index.html">Request a demo</a><a href="{up}kit/index.html">Evaluation kit</a>
      <a href="{up}contact/index.html">Contact</a><a href="{up}about/index.html">About this site</a>
      <a href="{up}privacy/index.html">Privacy</a></div>
  </div>
  <p class="legal"><strong>Tallpine is a made-up company.</strong> The product, people and customers described on this
  site do not exist. Forms send what you type to a test CRM, so please use made-up details. The site may load a
  visitor-identification script that estimates which company a visit comes from; it does not identify individuals.
  See <a href="{up}privacy/index.html">Privacy</a>.</p>
</div></footer>
</body>
</html>
"""
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8", newline="\n")


def band(up=""):
    return (f'<section class="band"><div class="wrap"><div><h2>See it on your own priorities</h2>'
            f'<p>A 45-minute demo built around the questions your leadership team is asking.</p></div>'
            f'<p class="cta"><a class="btn light" href="{up}demo/index.html">Request a demo</a>'
            f'<a class="btn outline" href="{up}kit/index.html">Get the evaluation kit</a></p></div></section>')


def head(kicker, title, lede, name=None):
    ic = f'<span class="badge">{icon(name)}</span>' if name else ""
    return (f'<section class="phead"><div class="wrap">{ic}<p class="kicker">{escape(kicker)}</p>'
            f'<h1>{escape(title)}</h1><p class="lede">{escape(lede)}</p></div></section>')


def field(name, label, kind="text", required=False, options=None, placeholder="", half=False):
    req = ' required aria-required="true"' if required else ""
    star = ' <span class="req" aria-hidden="true">*</span>' if required else ""
    cls = "row half" if half else "row"
    if kind == "select":
        opts = '<option value="">Choose one</option>' + "".join(
            f'<option value="{escape(v)}">{escape(l)}</option>' for v, l in options)
        control = f'<select id="f-{name}" name="{name}"{req}>{opts}</select>'
    elif kind == "textarea":
        control = f'<textarea id="f-{name}" name="{name}" rows="4" placeholder="{escape(placeholder)}"{req}></textarea>'
    elif kind == "checkbox":
        return (f'<div class="row"><label class="check"><input type="checkbox" id="f-{name}" name="{name}" value="true"> '
                f'<span>{escape(label)}</span></label></div>')
    else:
        control = f'<input id="f-{name}" name="{name}" type="{kind}" placeholder="{escape(placeholder)}"{req}>'
    return f'<div class="{cls}"><label for="f-{name}">{escape(label)}{star}</label>{control}</div>'


def form(kind, fields, button, steps):
    common = [field("firstname", "First name", required=True, half=True), field("lastname", "Last name", required=True, half=True),
              field("email", "Work email", "email", True, placeholder="you@company.example"),
              field("jobtitle", "Job title", required=True, half=True), field("company", "Company", required=True, half=True),
              field("country", "Country", "select", True, [(c, c) for c in COUNTRIES])]
    side = "".join(f'<li><span class="n">{n}</span><div><strong>{escape(h)}</strong><p>{escape(t)}</p></div></li>'
                   for n, (h, t) in enumerate(steps, 1))
    return (f'<section><div class="wrap split">'
            f'<form class="card form" data-hs-form="{FORMS[kind]}" data-hs-portal="{PORTAL}" data-kind="{kind}" novalidate>'
            f'<div class="fields">{"".join(common + fields)}</div>'
            f'<p class="note">This is a demonstration. Please enter made-up details, not real personal data.</p>'
            f'<button class="btn" type="submit">{escape(button)}</button>'
            f'<p class="status" role="status" aria-live="polite"></p></form>'
            f'<aside class="next"><h2>What happens next</h2><ol>{side}</ol></aside></div></section>')


def mock():
    rows = [("Claims triage assistant", "Delivered", "ok", 86), ("Contract summary tool", "In review", "rev", 54),
            ("Service desk agent", "Forecast", "fc", 38), ("Meeting notes pilot", "Stopped", "stop", 12)]
    body = "".join(f'<div class="mrow"><span class="mname">{escape(n)}</span><span class="pill {c}">{s}</span>'
                   f'<span class="mbar"><i style="width:{w}%"></i></span></div>' for n, s, c, w in rows)
    return (f'<div class="mock" role="img" aria-label="Illustration of a Tallpine project list with a status and a '
            f'usage bar for each project"><div class="mtop"><span></span><span></span><span></span>'
            f'<b>AI program · this quarter</b></div><div class="mhead"><span>Project</span><span>Status</span>'
            f'<span>Usage</span></div>{body}<div class="mfoot">4 projects · 1 delivered · 1 stopped with a reason</div></div>')


def build():
    q_options = [(g[0], g[2]) for g in GUIDES]
    guide_cards = lambda up: "".join(
        f'<a class="card link" href="{up}{slug}/index.html"><span class="badge">{icon(ic)}</span><h3>{escape(title)}</h3>'
        f'<p>{escape(lede)}</p><span class="more">Read the guide</span></a>' for _, slug, title, lede, ic, _, _ in GUIDES)

    # home ---------------------------------------------------------------------------------------------------
    why = "".join(f'<div class="card"><span class="badge">{icon(ic)}</span><h3>{escape(h)}</h3><p>{escape(t)}</p></div>'
                  for ic, h, t in [
                      ("compass", "Decide what to back", "Every proposal is checked against the priorities your "
                       "leadership team has agreed, with the same short review each time."),
                      ("people", "See whether people use it", "Usage comes from the tools your teams already work in, "
                       "so you know early when a project is stalling."),
                      ("chart", "Know what it delivered", "Each project keeps its starting point, its target and the "
                       "measured result in one place, ready for your next board update.")])
    steps = "".join(f'<li><span class="n">{n}</span><h3>{escape(h)}</h3><p>{escape(t)}</p></li>' for n, (h, t) in enumerate([
        ("Set the priorities", "Leadership names a few themes where AI should make a difference this year."),
        ("Review each proposal", "Every idea answers the same short set of questions before it gets a budget."),
        ("Follow real usage", "Usage is read from the tools people already work in. No surveys."),
        ("Compare with the numbers", "Results are checked against the figures your finance team already reports.")], 1))
    promise = "".join(f'<div><span class="badge">{icon(ic)}</span><h3>{escape(h)}</h3><p>{escape(t)}</p></div>'
                      for ic, h, t in [("clock", "A reply within one business day", "Every request gets an answer by the end of the next working day."),
                                       ("mail", "Written by a person", "Someone on our team reads your message and replies to what you asked."),
                                       ("shield", "No automated follow-ups", "You hear from us again only if you ask us to stay in touch.")])
    page("index.html", "Run your AI program like a portfolio",
         f'<section class="hero"><div class="wrap hgrid"><div><p class="kicker">AI program planning and review</p>'
         f'<h1>Run your AI program like a portfolio</h1>'
         f'<p class="lede">Tallpine is the workspace where leadership teams decide which AI projects to back, see '
         f'whether people use them, and know what each one delivered.</p>'
         f'<p class="cta"><a class="btn" href="demo/index.html">Request a demo</a>'
         f'<a class="btn ghost" href="resources/index.html">Read the guides</a></p></div>{mock()}</div></section>'
         f'<section><div class="wrap"><p class="kicker">Why teams use Tallpine</p><h2>One place for the decisions that matter</h2>'
         f'<div class="grid three">{why}</div></div></section>'
         f'<section class="alt"><div class="wrap"><p class="kicker">How it works</p><h2>Four habits, one shared record</h2>'
         f'<ol class="steps">{steps}</ol></div></section>'
         f'<section><div class="wrap"><p class="kicker">Guides</p><h2>Four questions leaders are asking about AI</h2>'
         f'<div class="grid two">{guide_cards("resources/")}</div></div></section>'
         f'<section class="alt"><div class="wrap"><p class="kicker">When you write to us</p><h2>What you can expect</h2>'
         f'<div class="grid three promise">{promise}</div></div></section>' + band(),
         "Tallpine is the workspace where leadership teams decide which AI projects to back.")

    # guides ---------------------------------------------------------------------------------------------------
    page("resources/index.html", "Guides",
         head("Guides", "Four questions leaders are asking about AI",
              "Short, plain answers to the questions we hear most from leadership teams.") +
         f'<section><div class="wrap"><div class="grid two">{guide_cards("")}</div></div></section>' + band("../"))
    for key, slug, title, lede, ic, paras, takeaways in GUIDES:
        body = "".join(f"<p>{escape(p)}</p>" for p in paras)
        points = "".join(f"<li>{escape(t)}</li>" for t in takeaways)
        page(f"resources/{slug}/index.html", title,
             head("Guide", title, lede, ic) +
             f'<section><div class="wrap article"><article class="prose">{body}</article>'
             f'<aside><div class="card"><h3>In short</h3><ul class="ticks">{points}</ul></div>'
             f'<div class="card callout"><h3>Put this question to us</h3><p>Ask for a demo built around this question, '
             f'or request a 30-minute briefing.</p>'
             f'<a class="btn block" href="../../demo/index.html?question={key}">Request a demo</a>'
             f'<a class="btn ghost block" href="../../contact/index.html?question={key}">Request the briefing</a></div>'
             f'</aside></div></section>', lede)

    # product pages ----------------------------------------------------------------------------------------------
    for slug, title, lede, ic, blocks in BUYING:
        cards = "".join(f'<div class="card">{f"<span class=tag-{tag}>{escape(h)}</span>" if tag else f"<h3>{escape(h)}</h3>"}'
                        f'<p>{escape(t)}</p></div>' for h, t, tag in blocks)
        page(f"{slug}/index.html", title,
             head("Product", title, lede, ic) +
             f'<section><div class="wrap"><div class="grid three">{cards}</div></div></section>' + band("../"), lede)

    # about and privacy --------------------------------------------------------------------------------------
    page("about/index.html", "About this site",
         head("About", "About this site", "Tallpine is a made-up company, built to demonstrate how an inbound "
              "engine handles website enquiries.") +
         '<section><div class="wrap narrow prose">'
         '<p>This site is part of a portfolio project in go-to-market engineering. Nothing here is a real product, '
         'customer or offer, and the company does not exist.</p>'
         '<p>The site has two jobs. First, its forms send what you type to a test CRM, where an inbound engine works '
         'out who is writing, chooses a route, drafts a reply from approved wording and sets a one-business-day '
         'deadline. A person approves and sends every reply; nothing is sent automatically.</p>'
         '<p>Second, it gives a visitor-identification script real pages to watch. That script estimates which '
         '<em>company</em> a visit comes from. The engine keeps only the company, never a person, and it never '
         'sends a message because of a visit alone.</p>'
         '<p>If you try the forms, please use made-up details.</p></div></section>')
    page("privacy/index.html", "Privacy",
         head("Privacy", "Privacy", "What this demonstration site collects, in plain words.") +
         '<section><div class="wrap narrow prose">'
         '<h2>Forms</h2><p>What you type into a form is sent to a HubSpot test account used only for this '
         'demonstration. Please enter made-up details. No phone number is asked for or stored.</p>'
         '<h2>Visitor identification</h2><p>The site may load a script from Swan that estimates which company a '
         'visit comes from, based on the network the visit arrives through. It is an estimate about an organization. '
         'The project keeps only the company name and the pages visited; any detail about an individual is '
         'discarded before anything is stored or scored.</p>'
         '<h2>No marketing</h2><p>Nobody is added to a mailing list, and no message is ever sent because of a visit.</p>'
         '<h2>Questions</h2><p>Use the <a href="../contact/index.html">contact form</a>.</p></div></section>')

    # forms --------------------------------------------------------------------------------------------------
    after = [("We read your request", "A person on our team reads what you wrote."),
             ("You get a reply", "By the end of the next business day, with two possible times."),
             ("We prepare", "The session is built around the question you picked.")]
    page("demo/index.html", "Request a demo",
         head("Demo", "Request a demo", "Tell us a little about your AI work. We reply within one business day "
              "with two possible times.") + form("demo", [
                  field("board_question", "Which question matters most to you?", "select", False, q_options),
                  field("ai_initiatives", "Roughly how many AI projects are under way?", placeholder="For example: about 60", half=True),
                  field("current_tools", "Tools you use today", placeholder="For example: Jira, ServiceNow", half=True),
                  field("preferred_time", "Preferred time", placeholder="For example: weekday mornings, Eastern"),
                  field("message", "What would you like to see?", "textarea"),
              ], "Request the demo", after))
    page("kit/index.html", "Evaluation kit",
         head("Evaluation", "Get the evaluation kit", "A short guide for teams comparing ways to run an AI "
              "program. We send the link and follow up once, in person.") + form("kit", [
                  field("evaluation_stage", "Where are you in your evaluation?", "select", False,
                        [("exploring", "Just exploring"), ("comparing", "Comparing options"), ("deciding", "Close to a decision")]),
                  field("message", "Anything else we should know?", "textarea"),
              ], "Send me the kit", [("The link arrives", "You get the kit by email straight away."),
                                     ("One follow-up", "A person writes to you once, to see whether it helped."),
                                     ("Then it is up to you", "No further messages unless you ask.")]))
    page("contact/index.html", "Contact",
         head("Contact", "Talk to us", "Tell us what brings you here and the right person will reply.") + form("contact", [
             field("reason", "What brings you here?", "select", True,
                   [("buying", "Buying for my organization"), ("partnership", "A partnership"), ("careers", "Careers"),
                    ("selling", "Selling to Tallpine"), ("press", "Press or analyst"), ("other", "Something else")]),
             field("board_question", "Which question matters most to you? (optional)", "select", False, q_options),
             field("message", "Message", "textarea"),
             field("briefings_opt_in", "Invite me to executive briefings", "checkbox"),
         ], "Send", [("We read your message", "It goes to the person who handles that kind of request."),
                     ("You get a reply", "By the end of the next business day."),
                     ("No mailing list", "You are added to nothing unless you tick the box.")]))
    (ROOT / "assets" / "favicon.svg").write_text(LOGO.replace('width="28" height="28"', 'xmlns="http://www.w3.org/2000/svg"'),
                                                 encoding="utf-8", newline="\n")
    print("built", len(list(ROOT.rglob("index.html"))), "pages")


if __name__ == "__main__":
    build()
