# postquality.com

The public home of Post Quality Manager, the WordPress plugin: a static site served by GitHub Pages at https://postquality.com (Jekyll, `minima` theme, built by GitHub Pages).

- `index.md`, `pricing.md`, `docs.md`: the front, pricing and documentation pages.
- `privacy.md`, `terms.md`, `refund.md`, `support.md`: the policies. Their source of truth is `docs/policies/` in the plugin repository; change them there first, then copy here.
- `_includes/head.html`, `_includes/footer.html`: copies of `minima` 2.5.1's, with the favicon and the policy links added and the analytics include removed; `assets/main.scss` darkens two theme colours for contrast.
- `404.html`, `robots.txt`: the missing-page page and the crawler rules; `jekyll-sitemap` writes `sitemap.xml`.
- `CNAME`: the custom domain.

Local build (optional, GitHub Pages builds on push): `bundle config set --local path vendor/bundle` (the setting lives in the ignored `.bundle/`, so a fresh clone needs it; gems go to the ignored `vendor/`), `bundle install`, then `PAGES_REPO_NWO=vincentheimann/postquality.com bundle exec jekyll build --baseurl ""`. Without a GitHub token, `jekyll-github-metadata` cannot find the repository and guesses a `/pages/...` base URL; the two settings stand in for what GitHub Pages knows on its own. On Windows, the Ruby with the DevKit is `C:/Ruby32-x64` (some gems build native extensions); run Bundler with `MSYSTEM` and `MSYS` unset.

Improving the site (content, screenshots, checkout, layout) is plugin backlog story 57.
