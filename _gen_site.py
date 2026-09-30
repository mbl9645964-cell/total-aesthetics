#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Total Aesthetics — Cosmetic & Dental Clinic — from-scratch static site generator."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
IMG = "assets/img/"

PHONE_DISPLAY = "+91 99999 99999"
PHONE_TEL = "tel:+919999999999"
WA_NUM = "919999999999"
def wa(msg):
    import urllib.parse
    return f"https://wa.me/{WA_NUM}?text={urllib.parse.quote(msg)}"
WA_BOOK = wa("Hello Total Aesthetics, I would like to book an appointment.")
WA_CHAT = wa("Hello Total Aesthetics, how can I help you?")
EMAIL = "hello@totalaesthetics.in"
ADDRESS = "RZ 88/J, Main Road, Block RZ, Raj Nagar I, Palam, New Delhi – 110077"
MAPS = "https://www.google.com/maps/search/Total+Aesthetics+Palam+New+Delhi"
HOURS = "Mon–Sat · 10:00 am – 7:00 pm"
IG = "https://www.instagram.com/totalaesthetics"
FB = "https://www.facebook.com/totalaesthetics"

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("services.html", "Services"),
    ("team.html", "Our Team"),
    ("clinic.html", "Clinic"),
    ("contact.html", "Contact"),
]

def ic(path, size=18):
    return f'<svg class="ic" viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg>'

I_PHONE = ic('<path d="M6.5 3h3l1.5 5-2 1.5a12 12 0 0 0 5.5 5.5L16 18l5 1.5v3a1 1 0 0 1-1.1 1A18 18 0 0 1 3.5 6.1 1 1 0 0 1 4.5 5"/>')
I_WA = '<svg class="ic" viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.29-.14-1.7-.84-1.96-.94-.26-.1-.45-.14-.64.15-.19.29-.74.94-.91 1.13-.17.19-.34.21-.62.07-.29-.14-1.21-.45-2.3-1.42-.85-.76-1.42-1.7-1.59-1.98-.17-.29-.02-.44.13-.58.13-.13.29-.34.43-.51.14-.17.19-.29.29-.48.1-.19.05-.36-.02-.51-.07-.14-.64-1.55-.88-2.12-.23-.55-.47-.48-.64-.48h-.55c-.19 0-.5.07-.76.36-.26.29-1 .98-1 2.38 0 1.4 1.02 2.76 1.17 2.95.14.19 2.01 3.08 4.88 4.32.68.29 1.21.47 1.63.6.68.22 1.31.19 1.8.12.55-.08 1.7-.69 1.94-1.36.24-.67.24-1.24.17-1.36-.07-.12-.26-.19-.55-.33z"/><path d="M12 .9C5.87.9.9 5.87.9 12c0 1.95.51 3.86 1.48 5.55L.8 23.1l5.68-1.49A11.06 11.06 0 0 0 12 23.1c6.13 0 11.1-4.97 11.1-11.1S18.13.9 12 .9zm0 20.2c-1.72 0-3.4-.46-4.87-1.34l-.35-.21-3.37.89.9-3.29-.23-.35A9.06 9.06 0 0 1 2.9 12 9.1 9.1 0 1 1 12 21.1z"/></svg>'
I_CLOCK = ic('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>')
I_PIN = ic('<path d="M12 21s7-5.5 7-11a7 7 0 1 0-14 0c0 5.5 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>')
I_ARROW = ic('<path d="M5 12h14M13 6l6 6-6 6"/>')
I_IG = ic('<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/>', 15)
I_FB = '<svg class="ic" viewBox="0 0 24 24" width="15" height="15" fill="currentColor" aria-hidden="true"><path d="M14 8h2V5h-2c-1.7 0-3 1.3-3 3v2H9v3h2v6h3v-6h2l1-3h-3V8.5c0-.3.2-.5.5-.5z"/></svg>'
I_STAR = ic('<path d="M12 3l2.6 5.6L20 9.5l-4 4 1 5.9L12 16.6 7 19.4l1-5.9-4-4 5.4-.9z"/>', 15)
I_MENU = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>'
I_CLOSE = '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>'
I_LEAF = ic('<path d="M5 19c0-8 6-13 14-13 0 8-5 14-13 14"/><path d="M5 19c3-4 6-6 10-8"/>', 34)

def page(title, description, body, active="", extra_head=""):
    def _nav_item(href, label):
        cur = ' aria-current="page"' if href == active else ""
        return f'<li><a href="{href}"{cur}>{label}</a></li>'
    nav_links = "".join(_nav_item(href, label) for href, label in NAV)
    mobile_links = "".join(f'<li><a href="{href}">{label}</a></li>' for href, label in NAV)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Total Aesthetics</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Jost:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/site.css">
<link rel="icon" href="{IMG}favicon.png">
{extra_head}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<div class="topbar"><div class="wrap topbar__row">
<div class="topbar__info">
<a href="{PHONE_TEL}">{I_PHONE}<span>{PHONE_DISPLAY}</span></a>
<a href="{WA_CHAT}" target="_blank" rel="noopener">{I_WA}<span>WhatsApp</span></a>
<span>{I_CLOCK}<span>{HOURS}</span></span>
</div>
<div class="topbar__soc">
<a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{I_IG}</a>
<a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{I_FB}</a>
<a href="{MAPS}" target="_blank" rel="noopener" aria-label="Directions">{I_PIN}</a>
</div>
</div></div>

<header class="site-header" data-header>
<div class="wrap nav">
<a class="brand" href="index.html">
<img class="brand__mark" src="{IMG}mark_icon.png" alt="">
<span class="brand__word"><span class="brand__name">Total Aesthetics</span><span class="brand__tag">Cosmetic &amp; Dental Clinic</span></span>
</a>
<ul class="nav__menu">{nav_links}</ul>
<a class="btn nav__cta" href="{WA_BOOK}" target="_blank" rel="noopener">Book an Appointment</a>
<button class="nav__toggle" data-nav-toggle aria-label="Open menu" aria-expanded="false">{I_MENU}</button>
</div>
</header>

<div class="nav-scrim" data-nav-scrim></div>
<nav class="mobile-nav" data-mobile-nav aria-label="Mobile">
<button class="mobile-nav__close" data-nav-close aria-label="Close menu">{I_CLOSE}</button>
<ul>{mobile_links}</ul>
<a class="btn" style="width:100%;justify-content:center" href="{WA_BOOK}" target="_blank" rel="noopener">Book an Appointment</a>
</nav>

<main id="main">
{body}
</main>

<footer class="site-footer">
<div class="wrap footer-grid">
<div>
<p class="footer-brand__name">Total Aesthetics</p>
<p class="footer-brand__stmt">A boutique cosmetic &amp; dental clinic in Palam, New Delhi — considered care, delivered with precision and warmth.</p>
<div class="footer-soc">
<a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{I_IG}</a>
<a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{I_FB}</a>
<a href="{MAPS}" target="_blank" rel="noopener" aria-label="Directions">{I_PIN}</a>
</div>
</div>
<div class="footer-col"><h5>Explore</h5><ul>
<li><a href="about.html">About</a></li><li><a href="services.html">Services</a></li>
<li><a href="team.html">Our Team</a></li><li><a href="clinic.html">Clinic</a></li></ul></div>
<div class="footer-col"><h5>Services</h5><ul>
<li><a href="services.html#cosmetic-dentistry">Cosmetic Dentistry</a></li><li><a href="services.html#implants">Dental Implants</a></li>
<li><a href="services.html#facial-aesthetics">Facial Aesthetics</a></li><li><a href="services.html#skin">Skin &amp; Laser</a></li></ul></div>
<div class="footer-col"><h5>Visit</h5><ul>
<li>{ADDRESS}</li><li><a href="{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
<li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>{HOURS}</li></ul></div>
</div>
<div class="wrap footer-bottom">
<span>&copy; 2026 Total Aesthetics. All rights reserved.</span>
<span><a href="privacy.html">Privacy Policy</a><a href="disclaimer.html">Medical Disclaimer</a></span>
</div>
</footer>

<a class="wa-fab" href="{WA_CHAT}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{I_WA}</a>
<nav class="mobar" aria-label="Quick contact"><div class="mobar__row">
<a href="{PHONE_TEL}">{I_PHONE}<span>Call</span></a>
<a href="{WA_CHAT}" target="_blank" rel="noopener">{I_WA}<span>Chat</span></a>
<a class="is-primary" href="{WA_BOOK}" target="_blank" rel="noopener">{I_ARROW}<span>Book</span></a>
</div></nav>

<script src="assets/js/site.js"></script>
</body>
</html>'''

def section_head(kicker, title, intro="", center=False, light=False):
    c = " is-center" if center else ""
    ec = "eyebrow--center" if center else ""
    el = "eyebrow--light" if light else ""
    out = f'<div class="section-head{c}" data-reveal><span class="eyebrow {ec} {el}">{kicker}</span><h2 class="display-2">{title}</h2>'
    if intro:
        out += f'<p class="lead" style="margin-top:1rem">{intro}</p>'
    return out + "</div>"

# ============================================================== INDEX =====
def build_index():
    hero = f'''<section class="hero" data-hero-slideshow>
<div class="hero__slides">
<div class="hero__slide is-active"><img src="{IMG}treatment-room-blue.jpg" alt="Treatment room at Total Aesthetics"></div>
<div class="hero__slide"><img src="{IMG}treatment-room-services.jpg" alt="Treatment room at Total Aesthetics"></div>
<div class="hero__slide"><img src="{IMG}entrance.jpg" alt="Total Aesthetics reception, Palam"></div>
<div class="hero__slide"><img src="{IMG}consultation.jpg" alt="Consultation room at Total Aesthetics"></div>
</div>
<div class="hero__scrim"></div>
<div class="wrap hero__inner">
<div data-reveal>
<span class="hero__eyebrow">Palam &middot; New Delhi</span>
<h1 class="hero__title">Where dentistry meets <em>total</em> aesthetics.</h1>
<p class="hero__lead">A boutique clinic bringing cosmetic dentistry, restorative care and facial aesthetics together — planned around how you actually want to look and feel.</p>
<div class="hero__actions">
<a class="btn btn--cream" href="{WA_BOOK}" target="_blank" rel="noopener">Book an Appointment</a>
<a class="text-link text-link--light" href="{WA_CHAT}" target="_blank" rel="noopener">{I_WA}<span>WhatsApp us</span></a>
<a class="text-link text-link--light" href="{PHONE_TEL}">{I_PHONE}<span>{PHONE_DISPLAY}</span></a>
</div>
<dl class="hero__ticket">
<div><dt>Address</dt><dd>Raj Nagar I, Palam</dd></div>
<div><dt>Hours</dt><dd>{HOURS}</dd></div>
<div><dt>Approach</dt><dd>Cosmetic &amp; dental care, one plan</dd></div>
</dl>
</div>
</div>
<div class="hero__dots" data-hero-dots></div>
</section>'''

    factstrip = f'''<section class="factstrip"><div class="wrap factstrip__row stagger" data-reveal>
<div class="fact"><span class="fact__no">01</span><h3>Cosmetic &amp; dental, together</h3><p>One team, one plan — no shuttling between separate clinics.</p></div>
<div class="fact"><span class="fact__no">02</span><h3>Modern technique</h3><p>Contemporary equipment and technique for precise, comfortable care.</p></div>
<div class="fact"><span class="fact__no">03</span><h3>Sterile by default</h3><p>Hospital-grade sterilisation and single-use instruments where it matters.</p></div>
<div class="fact"><span class="fact__no">04</span><h3>Honest planning</h3><p>You get a clear plan and a clear reason for every recommendation.</p></div>
</div></section>'''

    intro = f'''<section class="section bg-card"><div class="wrap split">
<div data-reveal>
<span class="eyebrow">Our philosophy</span>
<h2 class="display-2">Aesthetics is not an add-on — it is the whole picture.</h2>
<p class="lead" style="margin-top:1.3rem">Your smile, skin and confidence are connected. That is why Total Aesthetics brings cosmetic dentistry and facial aesthetics under one roof, planned together instead of treated as separate problems.</p>
<p class="muted" style="margin-top:1rem">Every visit starts with a conversation about what you actually want — then a plan built around it, explained in plain language before any treatment begins.</p>
<a class="text-link" style="margin-top:1.6rem" href="about.html">More about our approach{I_ARROW}</a>
</div>
<div class="split__media" data-reveal>
<figure class="frame frame--tall"><img src="{IMG}treatment-room.jpg" alt="Treatment room at Total Aesthetics"></figure>
</div>
</div></section>'''

    services_teaser = f'''<section class="section bg-band"><div class="wrap">
{section_head("What we offer", "Cosmetic dentistry and facial aesthetics, in one place.", "From a confident new smile to smoother, refreshed skin — every treatment planned around you.")}
<ul class="tlist" data-reveal>
<li><a href="services.html#cosmetic-dentistry"><span class="tlist__thumb"><img src="{IMG}treatment-room.jpg" alt=""></span><span class="tlist__body"><h3>Cosmetic Dentistry</h3><p>Whitening, veneers and smile design — refined, natural-looking results.</p></span><span class="tlist__arrow">{I_ARROW}</span></a></li>
<li><a href="services.html#implants"><span class="tlist__thumb"><img src="{IMG}consultation.jpg" alt=""></span><span class="tlist__body"><h3>Dental Implants &amp; Restorative Care</h3><p>Long-lasting replacements for missing or damaged teeth.</p></span><span class="tlist__arrow">{I_ARROW}</span></a></li>
<li><a href="services.html#facial-aesthetics"><span class="tlist__thumb"><img src="{IMG}entrance.jpg" alt=""></span><span class="tlist__body"><h3>Facial Aesthetics</h3><p>Non-surgical treatments for a refreshed, natural appearance.</p></span><span class="tlist__arrow">{I_ARROW}</span></a></li>
<li><a href="services.html#skin"><span class="tlist__thumb"><img src="{IMG}treatment-room.jpg" alt=""></span><span class="tlist__body"><h3>Skin &amp; Laser Treatments</h3><p>Considered skin and hair-reduction treatments for everyday confidence.</p></span><span class="tlist__arrow">{I_ARROW}</span></a></li>
</ul>
<p style="margin-top:2.2rem" data-reveal><a class="text-link" href="services.html">View every service{I_ARROW}</a></p>
</div></section>'''

    process = f'''<section class="section bg-ink"><div class="wrap">
{section_head("How it works", "A calm path from consultation to result.", "", light=True)}
<div class="steps stagger" data-reveal>
<div class="step"><span class="step__no">01</span><h3>Consultation</h3><p>We listen first — your concerns and goals shape everything that follows.</p></div>
<div class="step"><span class="step__no">02</span><h3>Plan</h3><p>A clear, written plan with options and honest recommendations.</p></div>
<div class="step"><span class="step__no">03</span><h3>Treatment</h3><p>Delivered with precision, at a pace that keeps you comfortable.</p></div>
<div class="step"><span class="step__no">04</span><h3>Aftercare</h3><p>Clear guidance and follow-up, so results are built to last.</p></div>
</div>
</div></section>'''

    confidence = f'''<section class="section bg-card"><div class="wrap split split--rev">
<div class="split__media" data-reveal><figure class="frame frame--tall"><img src="{IMG}smile-confidence.jpg" alt="A confident smile"></figure></div>
<div data-reveal>
<span class="eyebrow">Cosmetic dentistry</span>
<h2 class="display-2">A smile that feels entirely yours.</h2>
<p class="lead" style="margin-top:1.3rem">Whitening, veneers and smile design are planned around your natural proportions — the goal is a smile that looks like a better version of you, not someone else’s.</p>
<p class="muted" style="margin-top:1rem">We talk through shade, shape and timeline before anything is done, so there are no surprises on the day.</p>
<a class="text-link" style="margin-top:1.6rem" href="services.html#cosmetic-dentistry">Explore cosmetic dentistry{I_ARROW}</a>
</div>
</div></section>'''

    wellness = f'''<section class="section bg-band"><div class="wrap split">
<div data-reveal>
<span class="eyebrow">Facial aesthetics &amp; skin</span>
<h2 class="display-2">Refreshed, natural — never overdone.</h2>
<p class="lead" style="margin-top:1.3rem">Our facial aesthetics and skin treatments are planned for subtlety: the aim is to look well-rested and like yourself, not visibly &ldquo;done.&rdquo;</p>
<p class="muted" style="margin-top:1rem">Every consultation starts with realistic expectations — what a treatment can genuinely achieve, and what it can’t.</p>
<a class="text-link" style="margin-top:1.6rem" href="services.html#facial-aesthetics">Explore facial aesthetics{I_ARROW}</a>
</div>
<div class="split__media" data-reveal><figure class="frame frame--tall"><img src="{IMG}spa-wellness.jpg" alt="A calming aesthetic treatment"></figure></div>
</div></section>'''

    faq_items = [
        ("Do you treat dental and cosmetic concerns in the same visit?", "Where it makes sense, yes — many consultations cover both, since a confident smile and refreshed skin are often part of the same conversation. Your plan is built around your goals, not a fixed package."),
        ("Is facial aesthetics treatment painful?", "Most treatments involve mild, brief discomfort at most. We discuss what to expect — and any numbing or comfort measures available — before starting."),
        ("How do I know which treatment is right for me?", "That is exactly what the consultation is for. We assess your concern, explain the realistic options, and recommend the smallest treatment that achieves your goal — never the most expensive one by default."),
        ("Do results from cosmetic treatments look natural?", "That is the standard we plan around. Every recommendation favours subtlety and your natural proportions over a dramatic, obviously-treated look."),
    ]
    faq_html = "".join(f'<div class="ledger__item" style="border-top:1px solid var(--line);padding:clamp(1.4rem,3vw,1.9rem) 0"><h3 class="display-3" style="font-size:1.15rem">{q}</h3><p class="muted" style="margin-top:.6rem">{a}</p></div>' for q, a in faq_items)
    faq = f'''<section class="section bg-card"><div class="wrap">
{section_head("Questions", "A few things patients often ask.", "", center=True)}
<div style="max-width:74ch;margin-inline:auto" data-reveal>{faq_html}<div style="border-top:1px solid var(--line)"></div></div>
</div></section>'''

    team_teaser = f'''<section class="section bg-ink"><div class="wrap">
<div style="display:flex;align-items:flex-end;justify-content:space-between;gap:2rem;flex-wrap:wrap;margin-bottom:clamp(2rem,4vw,3rem)" data-reveal>
<div><span class="eyebrow eyebrow--light">The team</span><h2 class="display-2" style="color:var(--cream)">Care led by people you can trust.</h2></div>
<a class="text-link text-link--light" href="team.html">Meet the team{I_ARROW}</a>
</div>
<div class="team-grid stagger on-dark" data-reveal>
<article class="person"><a class="person__photo" href="team.html"><span class="person__ph">{I_LEAF}<span>Add team photo</span></span></a><div class="person__body"><h3 class="person__name">Dr. [Your Doctor]</h3><p class="person__role">Cosmetic &amp; Restorative Dentistry</p></div></article>
<article class="person"><a class="person__photo" href="team.html"><span class="person__ph">{I_LEAF}<span>Add team photo</span></span></a><div class="person__body"><h3 class="person__name">Dr. [Your Doctor]</h3><p class="person__role">Implantology &amp; Oral Care</p></div></article>
<article class="person"><a class="person__photo" href="team.html"><span class="person__ph">{I_LEAF}<span>Add team photo</span></span></a><div class="person__body"><h3 class="person__name">[Aesthetics Specialist]</h3><p class="person__role">Facial Aesthetics &amp; Skin</p></div></article>
</div>
</div></section>'''

    reviews = f'''<section class="section bg-band"><div class="wrap split split--rev">
<div class="split__media" data-reveal><figure class="frame frame--tall"><img src="{IMG}consultation.jpg" alt="Consultation room at Total Aesthetics"></figure></div>
<div data-reveal>
<span class="eyebrow">Patient trust</span>
<h2 class="display-2">Read as patients describe us.</h2>
<div style="margin-top:2rem">
<div class="quote"><blockquote>Genuinely different experience — they explained everything before starting, and the results speak for themselves.</blockquote><cite>Patient review</cite></div>
<div class="quote"><blockquote>Clean, modern clinic and a team that actually listens. Highly recommend for both dental and skin treatments.</blockquote><cite>Patient review</cite></div>
</div>
<a class="text-link" style="margin-top:1.8rem" href="{MAPS}" target="_blank" rel="noopener">Read reviews on Google{I_ARROW}</a>
</div>
</div></section>'''

    clinic_teaser = f'''<section class="section bg-card"><div class="wrap">
<div style="display:flex;align-items:flex-end;justify-content:space-between;gap:2rem;flex-wrap:wrap;margin-bottom:clamp(1.6rem,3vw,2.2rem)" data-reveal>
<div><span class="eyebrow">Inside the clinic</span><h2 class="display-2">A calm space, designed for ease.</h2></div>
<a class="text-link" href="clinic.html">Take a look inside{I_ARROW}</a>
</div>
<div class="gallery" data-reveal style="grid-auto-rows:100px">
<figure class="frame g2"><img src="{IMG}entrance.jpg" alt="Reception"></figure>
<figure class="frame g3"><img src="{IMG}treatment-room.jpg" alt="Treatment room"></figure>
<figure class="frame g3"><img src="{IMG}consultation.jpg" alt="Consultation room"></figure>
</div>
</div></section>'''

    cta = f'''<section class="ctaband"><div class="wrap ctaband__row" data-reveal>
<div><span class="eyebrow eyebrow--light">Book your visit</span><h2>Ready when you are.</h2><p>Message us on WhatsApp or call the clinic — new patients are always welcome.</p></div>
<div class="ctaband__btns"><a class="btn btn--cream" href="{WA_BOOK}" target="_blank" rel="noopener">Book an Appointment</a><a class="text-link text-link--light" href="{WA_CHAT}" target="_blank" rel="noopener">Chat with us{I_ARROW}</a></div>
</div></section>'''

    body = hero + factstrip + intro + services_teaser + confidence + wellness + process + faq + team_teaser + reviews + clinic_teaser + cta
    return page(
        "Cosmetic &amp; Dental Clinic in Palam, New Delhi",
        "Total Aesthetics — a boutique cosmetic and dental clinic in Palam, New Delhi, bringing smile and skin care together.",
        body, active="index.html"
    )

open(os.path.join(BASE, "index.html"), "w", encoding="utf-8").write(build_index())
print("index.html written")

# ============================================================== ABOUT =====
def build_about():
    hero = f'''<section class="section" style="padding-top:clamp(3rem,6vw,4.5rem)"><div class="wrap">
<nav aria-label="Breadcrumb" class="muted" style="font-size:.85rem;margin-bottom:1.6rem"><a href="index.html">Home</a> / About</nav>
<span class="eyebrow">About the clinic</span>
<h1 class="display-1" style="max-width:17ch">Dentistry and aesthetics, planned as one.</h1>
<p class="lead" style="margin-top:1.4rem;max-width:60ch">Total Aesthetics is a boutique cosmetic and dental clinic in Palam, New Delhi — built on the idea that a confident smile and healthy, refreshed skin are part of the same picture, not two separate appointments.</p>
</div></section>'''

    story = f'''<section class="section bg-card"><div class="wrap split split--rev">
<div class="split__media" data-reveal><figure class="frame frame--tall"><img src="{IMG}entrance.jpg" alt="Total Aesthetics reception"></figure></div>
<div data-reveal>
<span class="eyebrow">Why &ldquo;total&rdquo; aesthetics</span>
<h2 class="display-2">Most clinics treat your smile and your skin as separate problems.</h2>
<p class="lead" style="margin-top:1.3rem">We built Total Aesthetics around the opposite idea: cosmetic dentistry, restorative care and facial aesthetics, planned together by one team that understands how they affect each other.</p>
<p class="muted" style="margin-top:1rem">That means fewer appointments, a consistent plan, and results considered as a whole — not treatment by treatment.</p>
</div>
</div></section>'''

    values = f'''<section class="section bg-ink"><div class="wrap">
{section_head("How we work", "A short list of things we take seriously.", "", light=True)}
<div class="feat-grid stagger" data-reveal>
<div class="feat"><span class="feat__no">i.</span><h3>Listening first</h3><p>Every visit starts with your concerns and goals, not a fixed checklist.</p></div>
<div class="feat"><span class="feat__no">ii.</span><h3>Plans in writing</h3><p>You leave knowing what was found, what is recommended, and why.</p></div>
<div class="feat"><span class="feat__no">iii.</span><h3>Considered, not rushed</h3><p>Treatment paced for comfort and precision, never a conveyor belt.</p></div>
<div class="feat"><span class="feat__no">iv.</span><h3>Sterile by default</h3><p>Hospital-grade sterilisation and single-use instruments where it matters.</p></div>
</div>
</div></section>'''

    cta = f'''<section class="ctaband"><div class="wrap ctaband__row" data-reveal>
<div><span class="eyebrow eyebrow--light">See what we offer</span><h2>Explore our services.</h2><p>Cosmetic dentistry, restorative care and facial aesthetics — in full.</p></div>
<div class="ctaband__btns"><a class="btn btn--cream" href="services.html">View Services</a></div>
</div></section>'''

    body = hero + story + values + cta
    return page("About", "The philosophy behind Total Aesthetics, Palam, New Delhi.", body, active="about.html")

open(os.path.join(BASE, "about.html"), "w", encoding="utf-8").write(build_about())
print("about.html written")

# ============================================================ SERVICES ====
def build_services():
    hero = f'''<section class="section" style="padding-top:clamp(3rem,6vw,4.5rem)"><div class="wrap">
<nav aria-label="Breadcrumb" class="muted" style="font-size:.85rem;margin-bottom:1.6rem"><a href="index.html">Home</a> / Services</nav>
<span class="eyebrow">Services</span>
<h1 class="display-1" style="max-width:18ch">Every treatment, planned around you.</h1>
<p class="lead" style="margin-top:1.4rem;max-width:60ch">Cosmetic dentistry, restorative care and facial aesthetics — each explained honestly, with a plan you understand before you commit.</p>
</div></section>'''

    items = [
        ("cosmetic-dentistry", "treatment-room.jpg", "Cosmetic Dentistry", "Professional whitening, veneers and smile design — planned around your natural proportions for results that still look like you."),
        ("implants", "consultation.jpg", "Dental Implants &amp; Restorative Care", "Long-lasting replacements for missing teeth, plus crowns, bridges and fillings for damaged or worn teeth."),
        ("root-canal", "treatment-room.jpg", "Root Canal &amp; Preventive Dentistry", "Root canal therapy to save a tooth that would otherwise need extraction, alongside routine check-ups and cleaning."),
        ("aligners", "consultation.jpg", "Aligners &amp; Orthodontics", "Clear aligners and braces for adults and teenagers, straightened discreetly and at your own pace."),
        ("facial-aesthetics", "entrance.jpg", "Facial Aesthetics", "Non-surgical treatments for a refreshed, natural appearance — discussed honestly, with realistic expectations."),
        ("skin", "treatment-room.jpg", "Skin &amp; Laser Treatments", "Considered skin treatments and laser hair reduction, suited to your skin type and comfort."),
    ]
    lis = []
    for anchor, img, title, desc in items:
        lis.append(f'<li id="{anchor}"><a href="{WA_BOOK}" target="_blank" rel="noopener"><span class="tlist__thumb"><img src="{IMG}{img}" alt=""></span><span class="tlist__body"><h3>{title}</h3><p>{desc}</p></span><span class="tlist__arrow">{I_ARROW}</span></a></li>')
    listing = f'<section class="section bg-card"><div class="wrap"><ul class="tlist" data-reveal>{"".join(lis)}</ul></div></section>'

    cta = f'''<section class="ctaband"><div class="wrap ctaband__row" data-reveal>
<div><span class="eyebrow eyebrow--light">Not sure what you need?</span><h2>Tell us your goal — we&rsquo;ll recommend a plan.</h2></div>
<div class="ctaband__btns"><a class="btn btn--cream" href="{WA_BOOK}" target="_blank" rel="noopener">WhatsApp Us</a></div>
</div></section>'''

    body = hero + listing + cta
    return page("Services", "Cosmetic dentistry, restorative care and facial aesthetics at Total Aesthetics, Palam.", body, active="services.html")

open(os.path.join(BASE, "services.html"), "w", encoding="utf-8").write(build_services())
print("services.html written")

# =============================================================== TEAM =====
def build_team():
    hero = f'''<section class="section" style="padding-top:clamp(3rem,6vw,4.5rem)"><div class="wrap">
<nav aria-label="Breadcrumb" class="muted" style="font-size:.85rem;margin-bottom:1.6rem"><a href="index.html">Home</a> / Our Team</nav>
<span class="eyebrow">The team</span>
<h1 class="display-1" style="max-width:16ch">Care led by people you can trust.</h1>
<p class="lead" style="margin-top:1.4rem;max-width:60ch">A small, considered team — so the person planning your treatment is the one who sees it through.</p>
</div></section>'''

    people = [
        ("Dr. [Your Doctor]", "Cosmetic &amp; Restorative Dentistry", "BDS, [qualifications]", "Leads smile design, veneers and restorative work — focused on results that look natural and last."),
        ("Dr. [Your Doctor]", "Implantology &amp; Oral Care", "BDS, [qualifications]", "Specialises in implants and root canal therapy, with a gentle, patient-first approach."),
        ("[Aesthetics Specialist]", "Facial Aesthetics &amp; Skin", "[qualifications]", "Plans facial aesthetics and skin treatments around realistic, natural-looking outcomes."),
    ]
    cards = []
    for name, role, qual, bio in people:
        cards.append(f'''<article class="person" data-reveal>
<span class="person__photo"><span class="person__ph">{I_LEAF}<span>Add team photo</span></span></span>
<div class="person__body"><h3 class="person__name">{name}</h3><p class="person__role">{role}</p><p class="person__qual">{qual}</p><p class="person__bio">{bio}</p></div>
</article>''')
    grid = f'<section class="section bg-card"><div class="wrap"><div class="team-grid">{"".join(cards)}</div></div></section>'

    cta = f'''<section class="ctaband"><div class="wrap ctaband__row" data-reveal>
<div><span class="eyebrow eyebrow--light">Book a consultation</span><h2>Meet the team in person.</h2></div>
<div class="ctaband__btns"><a class="btn btn--cream" href="{WA_BOOK}" target="_blank" rel="noopener">Book an Appointment</a></div>
</div></section>'''

    body = hero + grid + cta
    return page("Our Team", "Meet the team at Total Aesthetics, Palam, New Delhi.", body, active="team.html")

open(os.path.join(BASE, "team.html"), "w", encoding="utf-8").write(build_team())
print("team.html written")

# ============================================================== CLINIC ====
def build_clinic():
    hero = f'''<section class="section" style="padding-top:clamp(3rem,6vw,4.5rem)"><div class="wrap">
<nav aria-label="Breadcrumb" class="muted" style="font-size:.85rem;margin-bottom:1.6rem"><a href="index.html">Home</a> / Clinic</nav>
<span class="eyebrow">The clinic</span>
<h1 class="display-1" style="max-width:16ch">A calm, considered space.</h1>
<p class="lead" style="margin-top:1.4rem;max-width:60ch">In Raj Nagar I, Palam — designed to feel unhurried the moment you walk in.</p>
</div></section>'''

    gallery = f'''<section class="section bg-card"><div class="wrap">
<div class="gallery" data-reveal>
<figure class="frame g1"><img src="{IMG}entrance.jpg" alt="Reception"><span class="frame__tag">Reception</span></figure>
<figure class="frame g2"><img src="{IMG}treatment-room-services.jpg" alt="Treatment room"><span class="frame__tag">Treatment room</span></figure>
<figure class="frame g4"><img src="{IMG}consultation.jpg" alt="Consultation room"><span class="frame__tag">Consultation room</span></figure>
<figure class="frame g4"><img src="{IMG}treatment-room-blue.jpg" alt="Treatment room"><span class="frame__tag">Treatment room</span></figure>
<figure class="frame g5"><img src="{IMG}treatment-room-blue-2.jpg" alt="Treatment room"><span class="frame__tag">Treatment room</span></figure>
</div>
</div></section>'''

    access = f'''<section class="section bg-ink"><div class="wrap split">
<div data-reveal><span class="eyebrow eyebrow--light">Getting here</span><h2 class="display-2" style="color:var(--cream)">Easy to find, easy to reach.</h2><p class="mut" style="margin-top:1.2rem">{ADDRESS}. Street parking is available nearby.</p><a class="text-link text-link--light" style="margin-top:1.4rem" href="{MAPS}" target="_blank" rel="noopener">Open in Google Maps{I_ARROW}</a></div>
<div class="split__media" data-reveal><figure class="frame frame--wide"><img src="{IMG}entrance.jpg" alt="Total Aesthetics entrance"></figure></div>
</div></section>'''

    body = hero + gallery + access
    return page("Clinic", "Inside Total Aesthetics, Palam, New Delhi.", body, active="clinic.html")

open(os.path.join(BASE, "clinic.html"), "w", encoding="utf-8").write(build_clinic())
print("clinic.html written")

# ============================================================= CONTACT ====
def build_contact():
    hero = f'''<section class="section" style="padding-top:clamp(3rem,6vw,4.5rem)"><div class="wrap">
<nav aria-label="Breadcrumb" class="muted" style="font-size:.85rem;margin-bottom:1.6rem"><a href="index.html">Home</a> / Contact</nav>
<span class="eyebrow">Get in touch</span>
<h1 class="display-1" style="max-width:16ch">Let&rsquo;s find you a time.</h1>
<p class="lead" style="margin-top:1.4rem;max-width:60ch">Message us on WhatsApp, call the clinic, or send a note below — we usually reply the same day.</p>
</div></section>'''

    grid = f'''<section class="section bg-card"><div class="wrap contact-grid">
<div data-reveal>
<div class="contact-card"><h3>{I_PIN}Visit</h3><p>{ADDRESS}</p><a class="text-link" href="{MAPS}" target="_blank" rel="noopener">Get directions{I_ARROW}</a></div>
<div class="contact-card"><h3>{I_CLOCK}Hours</h3><p>{HOURS}</p></div>
<div class="contact-card"><h3>{I_PHONE}Contact</h3><p><a href="{PHONE_TEL}">{PHONE_DISPLAY}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p><a class="text-link" href="{WA_BOOK}" target="_blank" rel="noopener">WhatsApp us{I_ARROW}</a></div>
</div>
<div data-reveal>
<form data-wa-form>
<div class="formfield"><label for="cf-name">Your name</label><input id="cf-name" name="name" type="text" required></div>
<div class="formfield"><label for="cf-phone">Phone number</label><input id="cf-phone" name="phone" type="tel"></div>
<div class="formfield"><label for="cf-msg">How can we help?</label><textarea id="cf-msg" name="message" required></textarea></div>
<button class="btn" type="submit" style="width:100%;justify-content:center">Send via WhatsApp</button>
<p class="form__msg"></p>
</form>
</div>
</div></section>'''

    body = hero + grid
    return page("Contact", "Contact Total Aesthetics, Palam, New Delhi.", body, active="contact.html")

open(os.path.join(BASE, "contact.html"), "w", encoding="utf-8").write(build_contact())
print("contact.html written")

# ====================================================== PRIVACY/DISCLAIMER
def build_legal(title, active, paras):
    hero = f'''<section class="section" style="padding-top:clamp(3rem,6vw,4.5rem)"><div class="wrap">
<nav aria-label="Breadcrumb" class="muted" style="font-size:.85rem;margin-bottom:1.6rem"><a href="index.html">Home</a> / {title}</nav>
<span class="eyebrow">Legal</span>
<h1 class="display-1" style="max-width:18ch">{title}</h1>
</div></section>'''
    body_paras = "".join(f'<p class="muted" style="margin-bottom:1.2rem">{p}</p>' for p in paras)
    content = f'<section class="section bg-card"><div class="wrap" style="max-width:70ch">{body_paras}</div></section>'
    body = hero + content
    return page(title, f"{title} — Total Aesthetics.", body, active=active)

open(os.path.join(BASE, "privacy.html"), "w", encoding="utf-8").write(build_legal(
    "Privacy Policy", "privacy.html",
    [
        "Total Aesthetics respects your privacy. Information you share with us — by phone, WhatsApp, email or the contact form on this site — is used only to respond to your enquiry and to manage your care.",
        "We do not sell or share your personal information with third parties for marketing purposes. Clinical records are kept confidential and handled in line with standard medical record-keeping practice.",
        "If you have questions about how your information is handled, please contact us directly at " + EMAIL + ".",
    ]
))
print("privacy.html written")

open(os.path.join(BASE, "disclaimer.html"), "w", encoding="utf-8").write(build_legal(
    "Medical Disclaimer", "disclaimer.html",
    [
        "The content on this website is provided for general informational purposes only and is not a substitute for professional dental or aesthetic medical advice, diagnosis or treatment.",
        "Always consult a qualified practitioner regarding any concern before making treatment decisions. Individual results vary from patient to patient depending on clinical circumstances.",
        "In an emergency, please call the clinic directly at " + PHONE_DISPLAY + ".",
    ]
))
print("disclaimer.html written")
