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
6. `assets/episodes/E0N/` — thumbnails (see below)

The homepage shows only the **two newest** episodes plus a coming-soon tile;
older episodes live on `episodes.html`.

### Thumbnails

Cards render at `aspect-ratio: 16/9` with `object-fit: cover`, so every
landscape file must actually be 16:9:

| file | used for |
|---|---|
| `E0N-Thumbnail-640.webp` | `srcset` 640w |
| `E0N-Thumbnail-1280.webp` | `srcset` 1280w |
| `E0N-Thumbnail-1536.webp` | `srcset` 1536w (**must be 1536×864**) |
| `E0N-Thumbnail-16x9.jpeg` | `<img src>` fallback (**must be 1536×864**) |

`E0N-Thumbnail.webp` and `E0N-Thumbnail.jpeg` are 9:16 portrait *artwork
sources* — they are no longer referenced by any page. The
`*_2K_*.jpeg` / `*-Landscape_2K_*` files are the generation originals and are
also unreferenced; keep them in the pipeline repo rather than shipping them.

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