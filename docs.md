---
layout: page
title: Documentation
description: How to set up and use Post Quality Manager, from what it needs to upgrading to Pro.
permalink: /docs/
---

How to set up and use Post Quality Manager, from what it needs to upgrading to Pro.

<nav class="toc" aria-labelledby="toc-title">
<p class="toc-title" id="toc-title">On this page</p>
<ul role="list">
<li><a href="#requirements">Requirements</a></li>
<li><a href="#getting-n8n">Getting n8n</a></li>
<li><a href="#getting-started">Getting started</a></li>
<li><a href="#set-up-by-hand">Set up by hand</a></li>
<li><a href="#using-it">Using it</a></li>
<li><a href="#upgrade-to-pro">Upgrade to Pro</a></li>
<li><a href="#faq">FAQ</a></li>
</ul>
</nav>

## Requirements {#requirements}

- WordPress 6.6 or later and PHP 8.0 or later, on a single site: Multisite is not supported.
- Your own n8n, self-hosted, and an Anthropic API key: the workflow runs the reviews on Anthropic's models.
- Your site and n8n must reach each other over the network: the plugin calls the n8n webhook, and n8n calls your site's REST API back. A local, private or password-protected site cannot be called back.
- Yoast SEO, optional: its scores enrich the SEO and Audit agents and show on the Post Reviews screen.

## Getting n8n {#getting-n8n}

Post Quality runs its reviews in an n8n you host yourself, on a server your site can reach and that can reach your site back. n8n's own guide covers installing and running it: [Self-hosting n8n (docs.n8n.io)](https://docs.n8n.io/hosting/).

## Getting started {#getting-started}

{% if site.launched -%}
<div class="install">
<a class="btn btn-primary-light" href="{{ site.wporg_url }}" aria-describedby="install-note">Install from WordPress.org</a>
<p class="version-line">Version {{ site.version }}, updated {{ site.version_date }}, tested up to WordPress {{ site.tested_up_to }} · <a href="{{ site.changelog_url }}">What's new →</a></p>
<p class="install-note" id="install-note">Opens the plugin's WordPress.org page.</p>
</div>
{%- else -%}
<div class="install">
<p>Post Quality is not installable yet. One email when it is, then your address is deleted.</p>
<a class="btn btn-primary-light" href="{% include interest-href.html from="the documentation page" %}"><svg class="icon" aria-hidden="true" focusable="false"><use href="#i-mail"/></svg>Tell me when it's available<span class="vh"> (opens your email app)</span></a>
</div>
{%- endif %}

Once it is installed and active, open **Post Quality → n8n Workflow** and click **Set up n8n**, or follow the welcome notice's **Set up the workflow** link. The setup guide asks for three values:

- **Connect your n8n:** your n8n address and an n8n API key.
- **Set up the workflow:** your Anthropic API key. The plugin checks it once with Anthropic and writes it into an n8n credential; your site never stores it.

{% include screenshot.html src="setup" width="1280" height="708" phone="setup-phone" phone_width="800" phone_height="777" alt="Illustration of the setup guide, step 2 of 5: the n8n address and the n8n API key are connected, and a field asks for the Anthropic API key." caption="An illustration of the setup guide's three values. Fictional values." %}

The guide then creates the workflow and its credentials in n8n, publishes the workflow and tests the connection both ways. In its last step, **Run your first review**: pick a published post and click **Run Review**.

The plugin keeps the n8n API key on your site to set up and update the workflow, so create one for this site alone, with an expiration date (in n8n: Settings → n8n API). Rather not? [Set up by hand](#set-up-by-hand).

After the first review, the guide offers your Blog Profile, your Editorial Standards and, with Pro, scheduled reviews. Change them any time in **Settings**.

Rewrite needs HTTPS on your site (it signs in with a WordPress Application Password).

## Set up by hand {#set-up-by-hand}

For an n8n whose public API is off or out of reach, or if you prefer not to give the plugin an n8n API key, choose **Set up by hand instead** in the setup guide. **Set up by hand** on the n8n Workflow page then walks you through four steps, with a Copy button for every value:

1. **Import the workflow.**
2. **Create the credentials:** two, three with Pro.
3. **Check the credential in each node.**
4. **Publish and connect:** paste the workflow's production webhook URL (`/webhook/`, not `/webhook-test/`) and click **Save and test**.

The guide then runs your first review.

## Using it {#using-it}

- **Post Reviews** lists every post with its latest score and status. Click Review to score a post, or select several and review them together.
- **Dashboard** shows the posts to fix next, the average score and the trend.
- **Insert into Post** puts the suggested Takeaways or Sources into the post with one click, as a plain list or in a pattern you design in Appearance → Patterns.
- **Automated Reviews** (Pro) scores posts on a schedule, by age and score.
- **Roles** (Pro) sets what each WordPress role can do in the plugin.

## Upgrade to Pro {#upgrade-to-pro}

**Never delete the free plugin first:** deleting removes your stored reviews and settings.{% unless site.launched %} Pro goes on sale with the first public release; these steps apply from then.{% endunless %}

1. After checkout, Freemius emails you the license key and a link to the Pro build.
2. On each site, upload the Pro build with **Plugins → Add New Plugin → Upload Plugin** and activate it. The free build is deactivated for you, and your reviews and settings carry over.
3. Enter the license key on the activation screen, or through the **Activate License** link on the Plugins screen.
4. Once Pro is active, you may delete the free build: your data stays.

- **Move a site:** move an activation from one site to another in the customer portal.
- **Cancel:** cancel the renewal any time in the customer portal. Pro stays on until the end of the year you paid for, and Freemius emails you before each renewal.
- **Refund:** within 14 days of buying or renewing, ask in the customer portal or at [hello@postquality.com](mailto:hello@postquality.com). See the [refund policy](/refund/).
- **When the license ends:** nothing is deleted. Your site returns to Free: reviews, settings, schedules and role rights are kept, and Review and Key Takeaways keep working. Renewing unlocks everything again.

## FAQ {#faq}

<div class="faq-list">
<details class="faq" id="cost">
<summary>What does it cost me in AI calls?</summary>
<div class="faq-a">
<p>You pay Anthropic per call, on your own API key, and your n8n hosting separately. A review sends the post text plus your settings text once.</p>
<p>To cap what you spend, set a spend limit in your Anthropic account: the plugin's Monthly Quota only limits how many AI actions each Author runs (Editors and Administrators have no limit).{% unless site.launched %} A worked cost example is coming.{% endunless %}</p>
</div>
</details>
<details class="faq">
<summary>Does my content leave my site?</summary>
<div class="faq-a">
<p>Only to your own n8n and, through it, to Anthropic, on your instruction. See the <a href="{{ "/privacy/" | relative_url }}">privacy policy</a>.</p>
</div>
</details>
<details class="faq">
<summary>Does it work on Multisite?</summary>
<div class="faq-a">
<p>No. Post Quality runs on single sites only.</p>
</div>
</details>
<details class="faq">
<summary>Where do I report a bug?</summary>
<div class="faq-a">
<p>Write to <a href="mailto:{{ site.email }}">{{ site.email }}</a>, for the free plugin and for Pro. Report a security problem the same way, privately.</p>
</div>
</details>
</div>
