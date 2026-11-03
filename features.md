---
layout: page
title: Features
description: What each Post Quality Manager command and Settings tab does, with a picture of each, and which ones Pro adds.
permalink: /docs/features/
---
{%- comment -%}
  The Pro mark (story 100): the site's chip as a link reading "Pro" after each Pro heading, to the pricing comparison.
  Free sections carry none. Every fact sentence here restates the plugin (README, Documentation drift).
{%- endcomment -%}
{%- capture pro -%}<a class="chip chip-link" href="{{ "/pricing/#compare-h" | relative_url }}">Pro</a>{%- endcapture %}

What each part of Post Quality Manager does: the commands you run from Post Reviews, Insert into Post, then the Settings tabs. Review and Takeaways stay free; Pro adds every part marked Pro.{% unless site.launched %} Pro goes on sale with the first public release.{% endunless %}

<nav class="toc" aria-labelledby="toc-title">
<p class="toc-title" id="toc-title">On this page</p>
<ul role="list">
<li><a href="#review">Review</a></li>
<li><a href="#takeaways">Takeaways</a></li>
<li><a href="#sources">Sources</a></li>
<li><a href="#seo">SEO</a></li>
<li><a href="#audit">Audit</a></li>
<li><a href="#rewrite">Rewrite</a></li>
<li><a href="#insert-into-post">Insert into Post</a></li>
<li><a href="#connection">Connection</a></li>
<li><a href="#ai">AI</a></li>
<li><a href="#automation">Automation</a></li>
<li><a href="#usage-and-limits">Usage &amp; Limits</a></li>
<li><a href="#roles">Roles</a></li>
</ul>
</nav>

## Review {#review}

A score on four pillars, Structure, Readability, Engagement and Credibility, and the top edits to make. Its status follows the score: Ready to ship from 71, Needs revision from 41 to 70, Major revision at 40 or below.

{% include screenshot.html src="feature-review" width="1440" height="758" phone="feature-review-phone" phone_width="762" phone_height="758" alt="A post's Review tab in Post Reviews: Needs revision, score 57; bars for Structure, Readability, Engagement and Credibility; three top edits, the first: cut the second anecdote, it delays the first instruction; buttons Open in Editor, Re-run Review and Re-run Rewrite." caption="A post's Review tab in Post Reviews. Demo posts, fictional scores." %}

## Takeaways {#takeaways}

The post's main points as a list, ready to insert into the post: three to five specific items, 25 words or fewer each. It also checks the takeaways block the post already has, if any.

{% include screenshot.html src="feature-takeaways" width="1440" height="1082" phone="feature-takeaways-phone" phone_width="762" phone_height="1082" alt="A post's Takeaways tab: Needs revision, score 50; Block found and Position correct fail, the items are within the word limit and specific; one issue, the post has no Key Takeaways block; four rewritten items, the first: give each family member a private vault and share only the logins everyone needs; buttons Insert into Post and Re-run Takeaways." caption="The Takeaways tab, with Insert into Post. Demo posts, fictional scores." %}

## Sources {{ pro }} {#sources}

Finds the post's factual claims and checks whether each has a source, needs one or should be worded more cautiously; medical, financial and safety claims count as critical. It suggests sources you can insert at the end of the post.

{% include screenshot.html src="feature-sources" width="1440" height="1428" phone="feature-sources-phone" phone_width="762" phone_height="1428" alt="A post's Sources tab: Needs revision, score 55; 3 claims, 1 sourced, 0 unsourced critical, 1 unsourced moderate, verdict needs sources; two claims without a source, one moderate and one low, each with its issue and a suggestion; three rewritten sources; buttons Insert into Post and Re-run Sources." caption="The Sources tab. Demo posts, fictional scores." %}

## SEO {{ pro }} {#seo}

Checks the focus keyphrase and the meta description, and proposes new ones where they are weak or missing: two to four words for the keyphrase, 120 to 156 characters for the description. With Yoast SEO active, it reads the post's current ones first.

{% include screenshot.html src="feature-seo" width="1440" height="914" phone="feature-seo-phone" phone_width="762" phone_height="914" alt="A post's SEO tab: Needs revision, score 55; keyphrase assessment weak, proposed keyphrase family password manager; meta description missing, a proposed one of 142 characters; button Re-run SEO." caption="The SEO tab. Demo posts, fictional scores." %}

## Audit {{ pro }} {#audit}

A review, a Takeaways check, a Sources check and an SEO check of the post in one run, scored like Review.

{% include screenshot.html src="feature-audit" width="1440" height="1244" phone="feature-audit-phone" phone_width="762" phone_height="1244" alt="A post's Audit tab: Needs revision, score 58; its review part with bars for the four pillars, overall score 58 and three top edits; its takeaways part with the same checks as Takeaways and one issue." caption="The Audit tab, its review and takeaways parts. Demo posts, fictional scores." %}

## Rewrite {{ pro }} {#rewrite}

Rewrites the post to improve its structure, readability and engagement while keeping its meaning, in line with your Blog Profile and Editorial Standards, and writes a new excerpt. The post is saved with the status Pending Review and the original stays in its revisions; Rewrite needs HTTPS on your site.

{% include screenshot.html src="feature-rewrite" width="1440" height="740" phone="feature-rewrite-phone" phone_width="762" phone_height="740" alt="A post's History tab, newest first: Rewrite applied on November 1, 2026, then Audit 58, SEO 55, Sources 55, Takeaways 50 and Review 57, each Needs revision." caption="A post's History, a Rewrite applied on top. Demo posts, fictional scores." %}

## Insert into Post {#insert-into-post}

Puts the suggested takeaways into the post at the top, as a plain list, and replaces any Takeaways inserted earlier. The post is saved right away and keeps its status; the previous version stays in Revisions.

{% include screenshot.html src="feature-insert" width="1516" height="474" phone="feature-insert-phone" phone_width="800" phone_height="590" alt="The Insert Takeaways into the post confirmation: 4 takeaways go into the post at the top, using the pattern chosen in Settings, and replace any Takeaways inserted earlier; the post is saved right away and keeps its status, the previous version stays in Revisions; buttons Cancel and Insert into Post." caption="Insert into Post asks before it saves the post. Demo site." %}

### Pattern to use {{ pro }} {#pattern-to-use}

Insert into Post also puts the suggested sources at the end of the post, and can fill the first List block of a pattern you design in Appearance → Patterns instead of a plain list. Choose the pattern for Takeaways and for Sources in [Agent-Specific Overrides](#agent-specific-overrides).

## Connection {#connection}

Your plan, and the n8n webhook address and token, which you set on the n8n Workflow page. Add a **Notification URL**, such as a chat webhook, and the workflow posts a short report there each time a command finishes.

{% include screenshot.html src="feature-connection" width="1440" height="1124" phone="feature-connection-phone" phone_width="772" phone_height="1454" alt="Settings, Connection tab: License, Current plan: Pro, everything unlocked; n8n Connection with a placeholder n8n Webhook URL and a link to the n8n Workflow page for the Webhook Token; an empty Notification URL field." caption="Settings, Connection, on Pro. Demo site." %}

## AI {#ai}

The **Default Model** every agent uses, and your **Blog Profile** and **Editorial Standards**: a preset, or your own text under Custom, sent with your commands so reviews and rewrites fit your site. A table shows what each agent sends; a change applies on the next command, with no n8n re-import.

{% include screenshot.html src="feature-ai" width="1440" height="1668" phone="feature-ai-phone" phone_width="772" phone_height="2156" alt="Settings, AI tab: AI Model with the Default Model Claude Sonnet 4.6; AI Prompts & Context with the Agnostic Scoring Framework note and the Blog Profile set to Technical / IT Blog, its preset text shown below." caption="Settings, AI: the model and the Blog Profile. Demo site." %}

### Agent-Specific Overrides {{ pro }} {#agent-specific-overrides}

For each agent: a different **Model**, its **Reasoning Effort** or **Temperature**, **Additional Instructions** and, for Takeaways and Sources, the **Pattern to use**. Only the controls the selected model supports are shown.

{% include screenshot.html src="feature-overrides" width="1440" height="1428" phone="feature-overrides-phone" phone_width="772" phone_height="1414" alt="Agent-Specific Overrides, the Key Takeaways Agent open: Model Claude Haiku 4.5, Reasoning Effort not available for that model, Temperature 0.2, two sentences of Additional Instructions, Pattern to use set to a pattern named Key takeaways box." caption="Agent-Specific Overrides for the Key Takeaways Agent. Demo site." %}

## Automation {{ pro }} {#automation}

**Automated Reviews (Cron)** runs Review, SEO or Audit daily or weekly on a batch of posts, picked by their latest result from that agent: a score below the **Min Score Threshold**, or older than the **Max Result Age (days)**. Scheduled reviews do not count toward the monthly quota.

{% include screenshot.html src="feature-automation" width="1440" height="1366" phone="feature-automation-phone" phone_width="772" phone_height="1690" alt="Settings, Automation tab: Automated Reviews (Cron) enabled, Frequency Weekly, Batch Size 5, Command Review, Min Score Threshold 70, Max Result Age 90 days." caption="Settings, Automation. Demo site." %}

## Usage & Limits {#usage-and-limits}

The **Monthly Quota**: how many manual AI actions each Author may run a month, 20 by default, 0 for no limit. Editors and Administrators have no limit.

{% include screenshot.html src="feature-usage" width="1440" height="540" phone="feature-usage-phone" phone_width="772" phone_height="724" alt="Settings, Usage & Limits tab: Monthly Quota, AI Actions per User 20." caption="Settings, Usage & Limits. Demo site." %}

## Roles {{ pro }} {#roles}

What each WordPress role can do in the plugin: **View reviews**, **Run Review and Key Takeaways**, **Run paid agents**, **Manage agents** and **Manage settings**, applied to every user with that role. Roles that run the whole site, such as Administrator, keep everything, and a role with **Run paid agents** is not subject to the monthly quota.

{% include screenshot.html src="feature-roles" width="1440" height="1014" phone="feature-roles-phone" phone_width="772" phone_height="1550" alt="Settings, Roles tab: a table of roles by View reviews, Run Review and Key Takeaways, Run paid agents, Manage agents and Manage settings; Administrator has every box ticked and locked, Editor all but Manage settings, Author the first two, Contributor View reviews only, Subscriber none." caption="Settings, Roles. Demo site." %}
