# Demo Script — for Jason's Sales Friend (First Tester)

Hey — thanks for taking 30-45 minutes on this.

You're the first outside-eyes test of a tool I've been building. It's an AI presales assistant for industrial automation sales (specifically AVEVA / Schneider Electric). You don't need to know the products — I want your **sales-perspective read** on whether the *outputs look like material a sales rep would actually use*. Honest feedback wins; this isn't a pitch.

## What it is in 30 seconds

A Cowork plugin that turns Claude into a content factory for industrial automation presales work. Drop it in, ask it questions, it produces battlecards, ROI analyses, opportunity briefings, executive customer-facing decks, and quick-reference cheat sheets — drawing from a curated content layer with confidence-tagged citations.

The version you're testing (**v0.3.1 — pilot release with HTML live artifacts**) builds on v0.2.6's QA-fix work, then v0.3.0 added the regulatory + AVEVA AI conversation refresh (current LCRI / FSMA 204 / PHMSA Mega Rule framing, AVEVA Industrial AI Assistant (GA January 2026) woven into the narrative, AspenTech-Emerson ownership reflected, AVEVA-as-Schneider parent framing made consistent across battlecards). v0.3.1 adds four interactive HTML artifacts: ROI calculator with sliders, content health dashboard, battlecard viewer with audience-signals selector, and a briefing dashboard. Native PDF + PPTX rendering still works the same way (introduced in v0.2.5). Outputs should look like real sales artifacts, not just text.

## What I want from you (in priority order)

1. **Does it sound like a real sales pro wrote this?** Voice, tone, framing. If anything reads like AI-generated boilerplate, flag it.
2. **Would you trust this walking into a meeting?** If you were the AE, would you read the briefing and feel prepared, or would you rewrite it?
3. **Does the artifact look polished enough for an actual customer?** Especially the deck and the PDF. If a customer received this from one of your reps, would it pass the smell test?
4. **What's missing or wrong?** I expect you to find weak spots. Tell me.

## Setup (~5 minutes)

1. **Install:** I'll send you `aveva-presales-pro-v0.3.1.plugin`. In Cowork, go to plugins, drag-and-drop. Cowork auto-installs.
2. **Skip onboarding for the demo.** The plugin ships with an example config (Q-Mation defaults). When the plugin asks "set up the plugin," say *"just exploring"* (or *"use the example config"*) — it loads the example and you can start testing immediately. If you'd rather see the real onboarding experience, the 9-step wizard takes 15 min and gives you a richer flavor.
3. **(Optional)** If you want native PDF/PPTX outputs, your Cowork tenant needs Python with `weasyprint`, `markdown`, `python-pptx`. If they're not there, you'll get Markdown output instead of polished files. Markdown is still useful for the gut-check.

## Five things to try (most important first)

### Try 1 — Battlecard (~3 min)

Type into Cowork:

> *"Show me the Honeywell battlecard for an upstream oil and gas opportunity."*

**What I'm looking for from you:** does the response sound like real sales content? Are the win/lose patterns plausible? Is the gap-closure offer something you could actually do in a real deal?

Compare what you see with what an enterprise sales rep at any of these companies would expect — Salesforce, ServiceNow, Oracle, etc. — when they pull up a battlecard. Is this on par? Better? Worse?

### Try 2 — Multi-skill orchestration (~5 min)

Type:

> *"I'm walking into a meeting with a 100K-population municipal water utility evaluating us versus a competitor called Ignition. Pricing is the lead objection. Brief me."*

**What I'm looking for:** does it weave the industry context + the competitor positioning + the pricing rebuttal into one coherent response, or does it feel like three separate articles glued together?

Sales reality check: would the "reframe → evidence → pivot to support → gap-closure offer" structure work in a real meeting? Or does it sound canned?

### Try 3 — Executive deck (Native PPTX render) (~5 min)

Type:

> *"Generate a CPG executive deck on FSMA 204 readiness — 20 slides, customer-facing."*

The plugin should produce an actual `.pptx` file. Open it. Look at it like a customer would receive it.

**What I'm looking for:** is the visual quality acceptable? Does the narrative arc work (problem → implications → solution → outcome → call to action)? Would you give this to a customer or rewrite it?

Comparable to what you'd expect: a Gong customer deck, a Salesforce industry brief, a Deloitte client pitch. Better? Worse? On par?

### Try 4 — Quick reference (Native PDF render) (~3 min)

Type:

> *"Quick reference cheat sheet for Water Treatment, branded for [some made-up distributor name]."*

You should get a 1-page PDF. Look at the layout, the density, the scannability.

**What I'm looking for:** if you handed this to a rep walking into a meeting, would they have what they need in 60 seconds? Or is it cluttered / sparse / wrong?

### Try 5 — Account briefing (no CRM connected — manual) (~5 min)

Type:

> *"Prep me for a meeting with [pick a real company name you know — could be a customer of yours, a vendor, anyone]. They're in [industry]. Walk me into the conversation."*

The plugin will ask you for context (since it's not connected to a CRM). Provide what you'd typically know about a meeting: who you're meeting with, what stage, who else is involved, any prior conversation.

**What I'm looking for:** does the briefing format help? Or is it asking the wrong questions?

### Try 6 — HTML interactive artifacts (Bonus, ~5 min, optional)

v0.3.1 adds four interactive HTML artifacts. Try one or two:

> *"Show me the ROI calculator with sliders."* (or *"open the ROI calculator"*, *"play with the numbers"*)

Sliders for tag count, sites, OEE baseline / target, labor rate. Tier and vertical selectors. Watch the Year-1 / 3-year / 5-year totals + payback move in real time. This is the artifact AEs use sitting *with* a customer.

> *"Browse the battlecards."* (or *"show me the battlecards"*)

Picker for all 9 competitor cards. Audience-signals selector toggles framing (multi-vendor / single-vendor / cost-sensitive / enterprise-inclined). Each card shows the AVEVA Industrial AI Assistant counter to whatever AI offering the competitor has.

**What I'm looking for:** do the interactive artifacts feel like real tools, or like static templates dressed up?

## Five questions I want you to answer afterward

1. **Voice rating (1-5):** does this sound like real sales material?
2. **Trust rating (1-5):** would you walk into a meeting using this?
3. **Customer-facing rating (1-5):** would you give the deck/PDF to a customer?
4. **Friction rating (1-5):** how much rework would a real AE need?
5. **Game-changer rating (1-5):** if your team had this, would it change how they work?

5 = clearly yes, 1 = clearly no. Just numbers and 1-2 sentence reactions.

## What I'm NOT looking for (don't worry about these)

- Whether the AVEVA product names are right (I've got domain experts validating that)
- Whether the technical specifications are accurate (covered)
- Whether the pricing is current (the demo pricing book is intentionally illustrative; real distributors override it before customer use)
- Whether industry terms are precise (covered)

I want **your sales-domain instinct** on the outputs. That's what I can't get from technical reviewers.

## Time budget

- Setup: 5 min
- Five tries: 20-25 min
- Five-question feedback: 5-10 min
- **Total: 30-45 minutes** (plus ~5 min if you do the bonus Try 6)

## How to send feedback

Slack me, email me, voice memo me — whatever's easiest. Numbers + 1-2 sentences per question is plenty. Specific examples (*"Try 3 felt canned because…"*) are gold.

If something's actually broken (plugin won't install, error message, plugin doesn't activate on prompts), tell me that first and I'll debug before you waste more time. The most common gotchas:

- Plugin doesn't activate on a prompt → say *"load the AVEVA presales plugin"* explicitly to force activation.
- Output is Markdown when you wanted PDF/PPTX → native render dependencies aren't installed in your tenant. Markdown is still useful for the gut-check.
- Briefing skill asks for everything manually → CRM / Fireflies / M365 connectors aren't wired in your tenant. That's expected for the demo; just answer the questions inline.

## Why your read matters

You're the first outside-eyes test. If it lands with you, I take it to Q-Mation (the design-partner distributor). If it doesn't, I iterate before bothering them. Either way is useful — the more friction you find, the better.

Thanks again. Looking forward to your honest take.

— Jason
