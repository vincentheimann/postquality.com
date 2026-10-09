---
layout: page
title: Documentation
permalink: /docs/
---

## Requirements

- WordPress 6.6 or later, PHP 8.0 or later.
- An n8n instance, self-hosted or n8n Cloud, and an API key for the AI provider you want to use (Anthropic by default).
- WordPress and n8n must reach each other over the network: the plugin calls the n8n webhook, and n8n calls back the site's REST API. A local or password-protected site cannot be reached from n8n Cloud. The Rewrite agent also needs HTTPS, because it signs in with a WordPress Application Password.
- Yoast SEO, optional: its scores enrich the SEO and Audit agents and show on the Post Reviews screen.

## Install

1. Install the plugin from the WordPress.org directory once listed, or upload the zip from the latest [GitHub release](https://github.com/vincentheimann/post-quality-manager/releases) under Plugins → Add New → Upload Plugin, and activate it.
2. Open **Post Quality → n8n Workflow** (the welcome notice links there) and click **Set up the workflow**. The guide walks you through seven steps, each with the exact n8n menu items, a Copy button for every value and a Done mark, and remembers where you stopped:
   - get an n8n instance;
   - import your pre-configured workflow, by URL or by file;
   - create three credentials: a Header Auth named for the webhook token (header `X-PQM-Token`), a Header Auth for your AI provider key, and a Basic Auth with a WordPress Application Password for a user who can edit posts (the guide can create it for you);
   - link each credential to its node;
   - publish the workflow and copy its production webhook URL (`/webhook/`, not `/webhook-test/`);
   - paste it into the guide, which saves and pings it;
   - run your first review from the guide.
3. In **Settings → AI**, choose a Blog Profile and your Editorial Standards, or write your own under Custom. The guide's last step links there and to Automated Reviews.

## Using it

- **Post Reviews** lists every post with its latest score and status. Click Review to score a post, or select several and review them together.
- **Dashboard** shows the posts to fix next, the average score and the trend.
- **Insert into Post** puts the suggested Takeaways or Sources into the post with one click, as a plain list or in a pattern you design in Appearance → Patterns.
- **Automated Reviews** (Pro) scores posts on a schedule by age and score.
- **Roles** (Pro) sets what each WordPress role can do in the plugin.

## FAQ

**What does it cost me in AI calls?** You pay your AI provider per call. A review sends the post text plus your settings text once; the per-user monthly quota and the site-wide token limit in Settings cap what the plugin may spend. A worked example per provider will be added here.

**Does my content leave my site?** Only to your own n8n instance and the AI provider you configured, on your instruction. See the [privacy policy](/privacy/).

**Multisite?** Not supported.

**Where do I report a bug?** For the free plugin, the [WordPress.org support forum](https://wordpress.org/support/plugin/post-quality-manager/) or a [GitHub issue](https://github.com/vincentheimann/post-quality-manager/issues). Pro customers write to [hello@postquality.com](mailto:hello@postquality.com). Security problems: see the [security policy](https://github.com/vincentheimann/post-quality-manager/security/policy).
