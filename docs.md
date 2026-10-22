---
layout: page
title: Documentation
permalink: /docs/
---

## Requirements

- WordPress 6.6 or later, PHP 8.0 or later.
- An n8n instance, self-hosted or n8n Cloud, and an Anthropic API key: the workflow runs the reviews on Anthropic's models.
- WordPress and n8n must reach each other over the network: the plugin calls the n8n webhook, and n8n calls back the site's REST API. A local or password-protected site cannot be reached from n8n Cloud. The Rewrite agent also needs HTTPS, because it signs in with a WordPress Application Password.
- Yoast SEO, optional: its scores enrich the SEO and Audit agents and show on the Post Reviews screen.

## Install

Post Quality Manager is not installable yet. [Leave your email](mailto:hello@postquality.com?subject=Tell%20me%20when%20Post%20Quality%20Manager%20is%20available) and you will hear once, when you can install it. Once it is available:

1. Install the plugin and activate it.
2. Open **Post Quality → n8n Workflow** and click **Set up n8n** (or follow the welcome notice's **Set up the workflow** link). The setup guide connects your n8n and sets the workflow up for you. You type three values:
   - **Connect your n8n:** your n8n address and an n8n API key. Create the key for this site alone, with an expiration date.
   - **Set up the workflow:** your Anthropic API key. The plugin checks it once and writes it into an n8n credential; it never stores it.

   The guide then creates the workflow and its credentials in n8n, activates the workflow and tests the connection both ways. In its last step, pick a published post and click **Run Review** for your first review.
3. Rather not give the plugin an n8n API key? Choose **Set up by hand instead**: **Set up by hand** on the n8n Workflow page walks you through importing the workflow, creating its credentials (two, three with Pro) and pasting its production webhook URL back, with a Copy button for every value.
4. In **Settings → AI**, choose a Blog Profile and your Editorial Standards, or write your own under Custom. The guide offers them right after your first review, and Automated Reviews too on Pro.

## Using it

- **Post Reviews** lists every post with its latest score and status. Click Review to score a post, or select several and review them together.
- **Dashboard** shows the posts to fix next, the average score and the trend.
- **Insert into Post** puts the suggested Takeaways or Sources into the post with one click, as a plain list or in a pattern you design in Appearance → Patterns.
- **Automated Reviews** (Pro) scores posts on a schedule by age and score.
- **Roles** (Pro) sets what each WordPress role can do in the plugin.

## FAQ

**What does it cost me in AI calls?** You pay Anthropic per call, on your own API key. A review sends the post text plus your settings text once; the per-user monthly quota and the site-wide token limit in Settings cap what the plugin may spend. A worked example will be added here.

**Does my content leave my site?** Only to your own n8n instance and, through it, to Anthropic, on your instruction. See the [privacy policy](/privacy/).

**Multisite?** Not supported.

**Where do I report a bug?** Write to [hello@postquality.com](mailto:hello@postquality.com), for the free plugin and for Pro. Report a security problem the same way, privately.
