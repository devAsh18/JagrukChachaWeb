# Jagruk Chacha — Website

**"हर रुपये के पीछे एक कहानी।"**

The official website for Jagruk Chacha — a Hindi-first animated content brand explaining the hidden economics behind everyday Indian life.

Live at https://jagrukchacha.com

## About

This repository is the public-facing website: plain hand-authored HTML, CSS and
one JavaScript file. There is **no build step** — `.github/workflows/static.yml`
uploads the repository as-is via `actions/upload-pages-artifact`, and the
committed `.nojekyll` stops GitHub Pages from processing anything.

`_config.yml` holds shared site metadata (domain, social links, email); it is
not read by the build.

## Content

- **Episodes** — the full catalogue at `/episodes.html`
- **Homepage** — hero for the latest episode, plus the two most recent cards and a "coming soon" tile
- **About** — brand introduction
- **Contact** — get in touch
- **Legal** — Privacy Policy, Terms of Service, Disclaimer

## Publishing an episode

There is no single episode data file that drives the pages, so an episode is
edited in by hand in several places. For a new episode **E0N**:

1. `assets/episode-stats.json` — add the `e0N` entry (videoId + three platform links), bump `lastUpdated`
2. `episodes.html` — add a `.episode-card` in newest-first position, and a topic chip / `.topic-teaser`
3. `index.html` — hero badge, hero card (image, tag, title, description, 3 links), `<link rel="preload">`, `og:video`, the `VideoObject` JSON-LD
4. `sitemap.xml` — homepage `video:video` block, `<lastmod>` for `/` and `/episodes.html`
5. `js/main.js` — the **hardcoded** `VIDEO_ID` constant (~line 300). It is *not*
   derived from `episode-stats.json`, so it silently drifts — check it every time.

The homepage shows only the **two newest** episodes plus a coming-soon tile;
older episodes live on `episodes.html`.

### Thumbnails (updated 2026-10-08)

All episode thumbnails are now **fetched automatically from YouTube** using the pattern:
`https://img.youtube.com/vi/{VIDEO_ID}/0.jpg`

The `VIDEO_ID` comes from `assets/episode-stats.json`. No local thumbnail assets are needed —
this saves ~20 MB in the repo and eliminates the manual thumbnail generation/upload step.

When adding a new episode card to `index.html` or `episodes.html`, use the YouTube URL:
```html
<img src="https://img.youtube.com/vi/{videoId}/0.jpg" ...>
<source srcset="https://img.youtube.com/vi/{videoId}/0.jpg 1536w" type="image/jpeg">
```

The same YouTube URL pattern is used for:
- `index.html` hero card image and preload
- `index.html` and `episodes.html` episode cards
- `episodes.html` JSON-LD `thumbnailUrl`
- `sitemap.xml` `video:thumbnail_loc`

Episode content (title, script, cost breakdown, numbers) comes from
`JagrukChachaPipeline/04_CONTENT/scripts/approved/`.

## Development

Serve locally from the repo root — no build, no dependencies:

```
python3 -m http.server 8000
```

After editing `css/styles.css`, bump the `?v=` query string in all seven pages
so the CDN picks the change up.

## Quick Links

- **YouTube**: https://www.youtube.com/@JagrukChacha
- **Instagram**: https://www.instagram.com/jagrukchacha
- **Email**: jagrukchacha@gmail.com

For the production pipeline and content creation, see:
https://github.com/devAsh18/JagrukChachaPipeline