# QuadMann Gaming

Six pages built from your supplied brief and photos, with a charcoal and violet design, responsive layouts, a keyboard-operable photo gallery, and a curated YouTube library.

## Review locally

Serve the `dist` folder with any static website server. For example, with Python installed, open a terminal in this folder and run:

    python -m http.server 8765 --directory dist

Then open http://localhost:8765. The site uses website-relative paths, so opening index.html by itself is not the supported preview method.

## Updating your site

You can ask ChatGPT to change a page, upload additional photos, or add direct video links. For example: “Add these three clips to Fortnite,” or “Replace the Call of Duty tutorial placeholder with this video.”

For manual editing, `build.py` contains the story, social links, clip selections, tutorial selections, and image assignments. Optimized photos are in `dist/assets`. Run `python build.py` after editing content. Styling and interactions are in `dist/styles.css` and `dist/app.js`. `dist/videos.json` is a generated inventory, not the source of edits. The site does not update video statistics automatically.

## Content and checks

- All eight supplied story photos are used. The folder did not contain identifiable ICU or rehabilitation photos; no recovery-photo captions were invented.
- One controller photo was supplied. Additional angles can be added later.
- Four verified tutorial videos and fourteen gameplay videos/Shorts are included. Fortnite, Halo, Call of Duty, story-driven adventures, and other games have working filters.
- Titles, links, and displayed view counts were checked on the channel's Videos and Shorts pages on October 18, 2026. Counts are rounded where YouTube displayed rounded values.
- A channel-wide comment-count ranking was not available. Provide a YouTube Analytics export containing video links/IDs and comment counts, or a list of clips you want featured, to add a most-commented section accurately.
- A dedicated Call of Duty control tutorial is marked coming soon. Send its direct link when ready.
- One Short (Quadriplegic Chase Down) was unavailable for embedding during preview; its thumbnail opens the verified YouTube Short directly. Other players include a direct YouTube fallback.
- Mobile menu, game filter, keyboard photo navigation, Escape-to-close, and Discord copying were checked in the browser. The full setup tutorial player loaded. All-video playback and desktop visual inspection remain unverified.
- Local page and image links, image alt attributes, heading counts, and JavaScript syntax were checked. This is not a full accessibility certification.

## Live website and publishing

Website: https://quadmann.github.io/QuadMannGaming/

The GitHub Actions workflow in `.github/workflows/pages.yml` builds and checks the six pages, prepares their links for GitHub Pages, and publishes `_site/`. It runs after updates to `main`, or manually from Actions → Publish QuadMann Gaming → Run workflow.

Edit `build.py` for content and `dist/styles.css` or `dist/app.js` for design and interactions. Keep `dist/assets` for images. `prepare_pages.py` adjusts deployment paths without changing the local preview version.

Official product reference: https://www.quadstick.com/
Video source: https://www.youtube.com/@QuadMannGaming
