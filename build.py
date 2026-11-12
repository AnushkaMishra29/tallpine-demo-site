"""Build the Tallpine demo site: plain static pages, no dependencies.   python build.py

Tallpine is a made-up company. The site exists so a visitor-identification script (Swan) has real pages to watch and
so its forms can post real submissions into a HubSpot test portal, where the inbound engine picks them up.
Every page loads assets/swan.js (paste the Swan snippet there, once) and assets/site.js (the forms).
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
QUESTIONS = [
    ("q-value", "ai-spending-paying-off", "Is our AI spending paying off?",
     "Most leadership teams can list what they spent on AI. Far fewer can show what came back.",
     ["Spending is easy to count: licences, cloud bills, the team's time. Returns are harder, because they show up "
      "inside other people's work and nobody is asked to claim them.",
      "Tallpine keeps one record per initiative, from the first idea to the result Finance has reviewed. Each one "
      "carries an owner, a baseline, a target and the evidence behind the current figure.",
      "The answer to the board is then a list, not a slide: which initiatives have delivered, which are still a "
      "forecast, and which were stopped and why."]),
    ("q-strategy", "ai-changing-strategy", "How is AI changing strategy?",
     "When almost anything can be built in a week, deciding what not to build becomes the real work.",
     ["Teams now propose more AI projects in a quarter than they used to in a year. Without a way to compare them, "
      "the loudest sponsor wins.",
      "Tallpine ties every proposal to a focus area the leadership team has already agreed, and asks the same few "
      "questions of each one before it gets a budget.",
      "Strategy stops being a yearly document and becomes a weekly habit: a short review, a clear yes or no, and a "
      "written reason either way."]),
    ("q-people", "ai-and-our-people", "What does AI mean for our people?",
     "A tool that nobody uses changes nothing. Adoption has to be planned like any other part of the work.",
     ["Every initiative in Tallpine names the group of people whose work it is meant to change, and how many of "
      "them need to be using it for the plan to hold.",
      "Usage is read from the systems people already work in, so nobody fills in a survey and nobody guesses.",
      "When adoption stalls, the owner sees it in the same place as the budget and the timeline, early enough to "
      "do something about it."]),
    ("q-agents", "what-agents-cost", "What do AI agents really cost?",
     "Agents are cheap to start and easy to forget. The bill arrives later, and it is rarely tied to a result.",
     ["Running costs grow with every agent a team launches, and they are usually reported in a different place "
      "from the benefits.",
      "Tallpine puts the two side by side for each initiative, so a team can see what an agent costs to run next to "
      "what it has returned so far.",
      "The cheapest run is the one that never starts on an idea that was not ready, which is why every idea passes "
      "a short review before any agent is switched on."]),
]
BUYING = [
    ("product-status", "Product status", "What is live today, what is connected, and what is still on the roadmap.",
     [("Live", "Focus areas, intake review, gate reviews, adoption tracking and the value record are in use today."),
      ("Connected", "Work-management and usage data arrive through connectors set up during onboarding."),
      ("Roadmap", "Board-pack generation and cost tracking for agents are planned. We label them as roadmap until "
                  "they ship, and we do not promise dates on this page.")]),
    ("packaging", "Packaging", "How Tallpine is scoped, from one business unit to the whole company.",
     [("Start with one unit", "Most customers begin with a single business unit and a 90-day launch."),
      ("Grow by scope", "Scope widens as more units join. It is set by what you manage, never by the number of seats."),
      ("Talk to us", "We share numbers once the scope is clear, in a conversation rather than on a web page.")]),
    ("integrations", "Integrations", "The systems Tallpine reads from, so nobody has to re-enter their work.",
     [("Systems of work", "Project and ticketing tools supply progress and ownership."),
      ("Usage data", "Sign-in and activity data show whether people are actually using what was built."),
      ("Finance", "Finance reviews happen in Tallpine, with the evidence attached to each figure.")]),
    ("trust", "Trust", "How we handle your data and what we can and cannot claim today.",
     [("Your data stays yours", "Customer data is kept separate per customer and is never used to train shared models."),
      ("Plain answers", "If we do not hold a certification, we say so, and we tell you what we have in its place."),
      ("Ask us", "Security and compliance questions go to a named person, and you get a written reply.")]),
]
NAV = [("index.html", "Home"), ("resources/index.html", "Board questions"), ("product-status/index.html", "Product"),
       ("packaging/index.html", "Packaging"), ("trust/index.html", "Trust"), ("contact/index.html", "Contact")]
COUNTRIES = ["United States", "Canada", "United Kingdom", "Germany", "France", "India", "Australia", "Other"]


def page(path, title, body, lede=""):
    depth = path.count("/")
    up = "../" * depth
    nav = "".join(f'<a href="{up}{href}">{escape(label)}</a>' for href, label in NAV)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} · Tallpine</title>
<meta name="description" content="{escape(lede or title)}">
<meta name="robots" content="noindex">
<link rel="stylesheet" href="{up}assets/style.css">
<script src="{up}assets/swan.js" defer></script>
<script src="{up}assets/site.js" defer></script>
</head>
<body>
<header class="top"><div class="wrap bar">
  <a class="brand" href="{up}index.html"><span class="mark"></span>Tallpine</a>
  <nav>{nav}</nav>
  <a class="btn small" href="{up}demo/index.html">Request a demo</a>
</div></header>
<main>
{body}
</main>
<footer><div class="wrap">
  <p><strong>Tallpine is a made-up company.</strong> This is a demonstration site for a portfolio project: the product,
  the people and the customers described here do not exist. Forms on this site send what you type to a test CRM;
  please use made-up details.</p>
  <p class="links"><a href="{up}integrations/index.html">Integrations</a> · <a href="{up}kit/index.html">Evaluation kit</a> ·
  <a href="{up}contact/index.html">Contact</a></p>
</div></footer>
</body>
</html>
"""
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8", newline="\n")


def hero(kicker, title, lede, cta=True, up=""):
    buttons = (f'<p class="cta"><a class="btn" href="{up}demo/index.html">Request a demo</a>'
               f'<a class="btn ghost" href="{up}contact/index.html">Talk to us</a></p>') if cta else ""
    return (f'<section class="hero"><div class="wrap"><p class="kicker">{escape(kicker)}</p>'
            f'<h1>{escape(title)}</h1><p class="lede">{escape(lede)}</p>{buttons}</div></section>')


def field(name, label, kind="text", required=False, options=None, placeholder=""):
    req = " required" if required else ""
    star = ' <span class="req">*</span>' if required else ""
    if kind == "select":
        opts = '<option value="">Choose one</option>' + "".join(
            f'<option value="{escape(v)}">{escape(l)}</option>' for v, l in options)
        control = f'<select id="f-{name}" name="{name}"{req}>{opts}</select>'
    elif kind == "textarea":
        control = f'<textarea id="f-{name}" name="{name}" rows="4" placeholder="{escape(placeholder)}"{req}></textarea>'
    elif kind == "checkbox":
        return (f'<label class="check"><input type="checkbox" id="f-{name}" name="{name}" value="true"> '
                f'{escape(label)}</label>')
    else:
        control = f'<input id="f-{name}" name="{name}" type="{kind}" placeholder="{escape(placeholder)}"{req}>'
    return f'<label for="f-{name}">{escape(label)}{star}</label>{control}'


def form(kind, fields, button):
    common = [field("firstname", "First name", required=True), field("lastname", "Last name", required=True),
              field("email", "Work email", "email", True, placeholder="you@company.example"),
              field("jobtitle", "Job title", required=True), field("company", "Company", required=True),
              field("country", "Country", "select", True, [(c, c) for c in COUNTRIES])]
    rows = "".join(f'<div class="row">{f}</div>' for f in common + fields)
    return (f'<form class="card form" data-hs-form="{FORMS[kind]}" data-hs-portal="{PORTAL}" data-kind="{kind}" novalidate>'
            f'{rows}<p class="note">This is a demonstration. Please enter made-up details, not real personal data.</p>'
            f'<button class="btn" type="submit">{escape(button)}</button>'
            f'<p class="status" role="status" aria-live="polite"></p></form>')


def build():
    q_options = [(key, title) for key, _, title, _, _ in QUESTIONS]

    # home ---------------------------------------------------------------------------------------------------
    cards = "".join(f'<a class="card link" href="resources/{slug}/index.html"><h3>{escape(title)}</h3>'
                    f'<p>{escape(lede)}</p><span class="more">Read the answer</span></a>'
                    for _, slug, title, lede, _ in QUESTIONS)
    steps = "".join(f'<div class="card"><p class="num">{n}</p><h3>{escape(h)}</h3><p>{escape(t)}</p></div>'
                    for n, h, t in [
                        (1, "Agree the focus", "Leadership names the few areas where AI should change the numbers."),
                        (2, "Review every idea", "Each proposal answers the same short set of questions before it is funded."),
                        (3, "Track real use", "Adoption is read from the tools people already work in."),
                        (4, "Let Finance confirm", "A result counts when Finance has reviewed the evidence behind it.")])
    page("index.html", "The management system for AI value",
         hero("AI value management", "Know what your AI spending is returning",
              "Tallpine gives leadership one record for every AI initiative, from the first idea to a result that "
              "Finance has reviewed.") +
         f'<section><div class="wrap"><h2>Four questions boards are asking</h2><div class="grid two">{cards}</div></div></section>'
         f'<section class="alt"><div class="wrap"><h2>How it works</h2><div class="grid four">{steps}</div></div></section>'
         '<section><div class="wrap center"><h2>See it on your own priorities</h2>'
         '<p class="lede">A 45-minute demo built around the questions your board is asking.</p>'
         '<p class="cta"><a class="btn" href="demo/index.html">Request a demo</a>'
         '<a class="btn ghost" href="kit/index.html">Get the evaluation kit</a></p></div></section>',
         "Tallpine gives leadership one record for every AI initiative.")

    # resources ----------------------------------------------------------------------------------------------
    listing = "".join(f'<a class="card link" href="{slug}/index.html"><h3>{escape(title)}</h3><p>{escape(lede)}</p>'
                      f'<span class="more">Read the answer</span></a>' for _, slug, title, lede, _ in QUESTIONS)
    page("resources/index.html", "Board questions",
         hero("Resources", "Four questions boards are asking about AI",
              "Short, plain answers to the questions we hear most from leadership teams.", cta=False, up="../") +
         f'<section><div class="wrap"><div class="grid two">{listing}</div></div></section>')
    for key, slug, title, lede, paras in QUESTIONS:
        body = "".join(f"<p>{escape(p)}</p>" for p in paras)
        page(f"resources/{slug}/index.html", title,
             hero("Board question", title, lede, cta=False, up="../../") +
             f'<section><div class="wrap narrow prose">{body}'
             f'<div class="card callout"><h3>Put this question to us</h3><p>Ask for a demo built around this question, '
             f'or request a 30-minute executive briefing.</p><p class="cta">'
             f'<a class="btn" href="../../demo/index.html?question={key}">Request a demo on this question</a>'
             f'<a class="btn ghost" href="../../contact/index.html?question={key}">Request the briefing</a></p></div>'
             f'</div></section>', lede)

    # buying-stage pages ---------------------------------------------------------------------------------------
    for slug, title, lede, blocks in BUYING:
        cards = "".join(f'<div class="card"><h3>{escape(h)}</h3><p>{escape(t)}</p></div>' for h, t in blocks)
        page(f"{slug}/index.html", title,
             hero("Product", title, lede, cta=False, up="../") +
             f'<section><div class="wrap"><div class="grid three">{cards}</div>'
             f'<p class="cta center"><a class="btn" href="../demo/index.html">Request a demo</a></p></div></section>', lede)

    # forms --------------------------------------------------------------------------------------------------
    page("demo/index.html", "Request a demo",
         hero("Demo", "Request a demo", "Tell us a little about your AI work and we will come back within one "
              "business day with two times.", cta=False, up="../") +
         '<section><div class="wrap narrow">' + form("demo", [
             field("board_question", "Which board question matters most?", "select", False, q_options),
             field("ai_initiatives", "Roughly how many AI initiatives are in flight?", placeholder="For example: about 60"),
             field("current_tools", "Tools you use today", placeholder="For example: Jira, ServiceNow"),
             field("preferred_time", "Preferred time", placeholder="For example: weekday mornings, Eastern"),
             field("message", "What would you like to see?", "textarea"),
         ], "Request the demo") + "</div></section>")
    page("kit/index.html", "Evaluation kit",
         hero("Evaluation", "Get the evaluation kit", "A short guide for teams comparing ways to manage AI value. "
              "We send the link and follow up once, in person.", cta=False, up="../") +
         '<section><div class="wrap narrow">' + form("kit", [
             field("evaluation_stage", "Where are you in your evaluation?", "select", False,
                   [("exploring", "Just exploring"), ("comparing", "Comparing options"), ("deciding", "Close to a decision")]),
             field("message", "Anything else we should know?", "textarea"),
         ], "Send me the kit") + "</div></section>")
    page("contact/index.html", "Contact",
         hero("Contact", "Talk to us", "Tell us what brings you here and the right person will reply.", cta=False, up="../") +
         '<section><div class="wrap narrow">' + form("contact", [
             field("reason", "What brings you here?", "select", True,
                   [("buying", "Buying for my organization"), ("partnership", "A partnership"), ("careers", "Careers"),
                    ("selling", "Selling to Tallpine"), ("press", "Press or analyst"), ("other", "Something else")]),
             field("board_question", "Which board question matters most? (optional)", "select", False, q_options),
             field("message", "Message", "textarea"),
             field("briefings_opt_in", "Invite me to executive briefings", "checkbox"),
         ], "Send") + "</div></section>")
    print("built", len(list(ROOT.rglob("index.html"))), "pages")


if __name__ == "__main__":
    build()
