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

{% comment %}FIGURE feature-review + feature-review-phone (story 100, task 3): Post Reviews, a post's Review tab: pillar scores, Top edits, Run Review and Run Rewrite.{% endcomment %}

## Takeaways {#takeaways}

The post's main points as a list, ready to insert into the post: three to five specific items, 25 words or fewer each. It also checks the takeaways block the post already has, if any.

{% comment %}FIGURE feature-takeaways + feature-takeaways-phone (story 100, task 3): the Takeaways tab: the check and the suggested items, Insert into Post.{% endcomment %}

## Sources {{ pro }} {#sources}

Finds the post's factual claims and checks whether each has a source, needs one or should be worded more cautiously; medical, financial and safety claims count as critical. It suggests sources you can insert at the end of the post.

{% comment %}FIGURE feature-sources + feature-sources-phone (story 100, task 3): the Sources tab: the claims with their severity, the verdict, the suggested sources.{% endcomment %}

## SEO {{ pro }} {#seo}

Checks the focus keyphrase and the meta description, and proposes new ones where they are weak or missing: two to four words for the keyphrase, 120 to 156 characters for the description. With Yoast SEO active, it reads the post's current ones first.

{% comment %}FIGURE feature-seo + feature-seo-phone (story 100, task 3): the SEO tab: the assessments and the proposed keyphrase and meta description.{% endcomment %}

## Audit {{ pro }} {#audit}

A review, a Takeaways check, a Sources check and an SEO check of the post in one run, scored like Review.

{% comment %}FIGURE feature-audit + feature-audit-phone (story 100, task 3): the Audit tab: the pillar scores, then the takeaways, sources and SEO parts.{% endcomment %}

## Rewrite {{ pro }} {#rewrite}

Rewrites the post to improve its structure, readability and engagement while keeping its meaning, in line with your Blog Profile and Editorial Standards, and writes a new excerpt. The post is saved with the status Pending Review and the original stays in its revisions; Rewrite needs HTTPS on your site.

{% comment %}FIGURE feature-rewrite + feature-rewrite-phone (story 100, task 3): the Review tab's Run Rewrite button, or the History tab with a Rewrite applied row.{% endcomment %}

## Insert into Post {#insert-into-post}

Puts the suggested takeaways into the post at the top, as a plain list, and replaces any Takeaways inserted earlier. The post is saved right away and keeps its status; the previous version stays in Revisions.

{% comment %}FIGURE feature-insert + feature-insert-phone (story 100, task 3): the Insert Takeaways into the post confirmation.{% endcomment %}

### Pattern to use {{ pro }} {#pattern-to-use}

Insert into Post also puts the suggested sources at the end of the post, and can fill the first List block of a pattern you design in Appearance → Patterns instead of a plain list. Choose the pattern for Takeaways and for Sources in [Agent-Specific Overrides](#agent-specific-overrides).

## Connection {#connection}

Your plan, and the n8n webhook address and token, which you set on the n8n Workflow page. Add a **Notification URL**, such as a chat webhook, and the workflow posts a short report there each time a command finishes.

{% comment %}FIGURE feature-connection + feature-connection-phone (story 100, task 3): Settings, the Connection tab: License, n8n Connection, Notification URL.{% endcomment %}

## AI {#ai}

The **Default Model** every agent uses, and your **Blog Profile** and **Editorial Standards**: a preset, or your own text under Custom, sent with your commands so reviews and rewrites fit your site. A table shows what each agent sends; a change applies on the next command, with no n8n re-import.

{% comment %}FIGURE feature-ai + feature-ai-phone (story 100, task 3): Settings, the AI tab: AI Model, then AI Prompts & Context.{% endcomment %}

### Agent-Specific Overrides {{ pro }} {#agent-specific-overrides}

For each agent: a different **Model**, its **Reasoning Effort** or **Temperature**, **Additional Instructions** and, for Takeaways and Sources, the **Pattern to use**. Only the controls the selected model supports are shown.

{% comment %}FIGURE feature-overrides + feature-overrides-phone (story 100, task 3): the AI tab's Agent-Specific Overrides, the Key Takeaways Agent open.{% endcomment %}

## Automation {{ pro }} {#automation}

**Automated Reviews (Cron)** runs Review, SEO or Audit daily or weekly on a batch of posts, picked by their latest result from that agent: a score below the **Min Score Threshold**, or older than the **Max Result Age (days)**. Scheduled reviews do not count toward the monthly quota.

{% comment %}FIGURE feature-automation + feature-automation-phone (story 100, task 3): Settings, the Automation tab: Automated Reviews (Cron), enabled.{% endcomment %}

## Usage & Limits {#usage-and-limits}

The **Monthly Quota**: how many manual AI actions each Author may run a month, 20 by default, 0 for no limit. Editors and Administrators have no limit.

{% comment %}FIGURE feature-usage + feature-usage-phone (story 100, task 3): Settings, the Usage & Limits tab: Monthly Quota.{% endcomment %}

## Roles {{ pro }} {#roles}

What each WordPress role can do in the plugin: **View reviews**, **Run Review and Key Takeaways**, **Run paid agents**, **Manage agents** and **Manage settings**, applied to every user with that role. Roles that run the whole site, such as Administrator, keep everything, and a role with **Run paid agents** is not subject to the monthly quota.

{% comment %}FIGURE feature-roles + feature-roles-phone (story 100, task 3): Settings, the Roles tab: What each role can do.{% endcomment %}
