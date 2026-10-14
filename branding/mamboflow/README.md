# MamboFlow brand kit

MamboFlow is the In Good Company Impact Studio product for getting social. This folder holds the brand integration kit, draft four: Mambo in his original cream coat with the teal collar and gold charm, the script wordmark lifted from Maddie's reference, the In Good Company mark, the argyle atomic panel, the lockups, the pattern language, and the application mockups. Everything follows the In Good Company brand system (black and white base, Bodoni Moda and Inter, square corners, hairline rules, generous space).

## Brand architecture

In Good Company is the parent brand. MamboFlow is an endorsed product. It carries the studio's circle mark beside the line "By In Good Company" on every surface, inherits the studio's type and palette, and adds:

1. Mambo, the French bulldog mascot, as drawn: cream coat, teal collar, gold charm. Black-and-white treatments remain for documents and print.
2. The argyle atomic panel: a framed piece of Maddie's ceiling wallpaper behind Mambo. The only place the full palette lives.
3. Two patterns from Maddie's home: Foyer (hex starburst, dark grounds) and Argyle Atomic (the paper). Plus Signal (rings, light grounds) and Lattice (the paper's geometry in hairline, for documents).
4. Two flat accents for a single shape: Collar Teal (#3FA9A6) and Mambo Mustard (#E2B03A).

## Files

| Path | What it is |
| --- | --- |
| `mascot/mambo-cream.png` | In use everywhere. The original art, trimmed, transparent background. |
| `mascot/mambo-cream-sticker.png`, `mambo-cream-excited.png`, `mambo-cream-excited-sticker.png`, `mambo-cream-head.png`, `mambo-cream-peek-corner.png`, `mambo-cream-peek-paws.png`, `mambo-cream-peek-ledge.png` | Poses cut from the drawing: sticker, excited, head, corner peek, peek with paws (use only where a ledge hides the seam), peek on a paper ledge. |
| `wordmark/mamboflow-script-black.png`, `-white.png`, `swoosh-teal.svg` | The script wordmark as artwork, lifted from Maddie's reference and cleaned; black and white; the optional teal swoosh. Not a font. Trace to vector before large print. |
| `mascot/mambo-pop-teal.png` | Black-and-white coat with the teal collar and gold charm. Quiet alternate. |
| `mascot/mambo-pop-{pink,mustard,red}.png` | Alternate collar colors, same charm. |
| `mascot/mambo-pop-*-sticker.png` | White keyline versions for dark grounds. |
| `mascot/mambo-peek-up.png`, `mambo-peek-corner.png`, `mambo-head.png`, `mambo-peek-sticker.png` | Poses cut from the drawing: peeking over an edge, peeking in from a corner, head only, die-cut sticker. |
| `mascot/mambo-classic.png` | Quiet treatment, no color. Documents and print. |
| `mascot/mambo-ink.png` | Full watercolor shading in grayscale. Large editorial use. |
| `mascot/mambo-stamp.png` | Pure two-tone. Favicons, sizes under 64 px. |
| `lockups/lock-primary.png`, `lock-stacked.png`, `lock-swoosh.png`, `lock-pill.png` | Transparent lockups: Mambo on his panel, the In Good Company mark, the script wordmark, the endorsement beneath. Swoosh adds the teal underline; pill is the capsule badge. |
| `lockups/lock-rev.png` | Reversed lockup on ink. |
| `social/avatar.png`, `avatar-dark.png` | Profile avatars, 400 x 400. |
| `social/header.png` | X header, 1500 x 500. |
| `social/post-quote.png`, `post-announce.png` | Post templates, 1080 x 1080. Headlines are placeholder copy. |
| `app/icon-teal.png`, `icon.png`, `icon-dark.png`, `fav.png` | App icon on Collar Teal (in use), paper and ink alternates, favicon source. |
| `app/card.png`, `card-back.png`, `coins.png` | Business card front and back, 3.5 x 2 in at 300 dpi, and the three glyph coins. |
| `app/mobile-welcome.png`, `mobile-color.png` | Two mobile welcome screens, 390 x 844. |
| `app/signin.png` | Sign-in screen mockup, 1440 x 900. |
| `app/sig.png` | Email signature strip, 600 x 140. |
| `patterns/*.svg`, `patterns/tile-*.png` | Argyle Atomic (coarse and fine), Foyer, Lattice, and the mustard sparkle cell, as scalable SVG and 600 x 600 PNG tiles. |
| `source/assets.html`, `source/render.js` | The HTML compositions every PNG was rendered from, and the Playwright renderer. |
| `source/mascot_convert.py`, `source/mascot_pop.py` | Scripts that produced the mascot treatments from the color original. |
| `igc/` | The In Good Company mark and lockup as supplied, on transparent grounds: black and white, square-padded, and sized 512 to 16 px. Never redrawn. |
| `board/igc-variations.png`, `source/igcvar.html` | The emblem variations sheet and its source. |
| `board/brand-sheet.png`, `source/sheet.html` | The one-page brand sheet and its source. |
| `board/index.html` | The brand board (also published as a Claude artifact). |
| `fonts/` | Bodoni Moda and Inter variable fonts (SIL Open Font License), copied from the In Good Company design system. |

## Rules in brief

- Mambo is cream, as drawn, with the teal collar and gold charm. Use the supplied poses; never redraw him.
- The paper appears only inside a framed panel behind Mambo, bordered in paper white with a hairline edge. He overlaps its edges. Never tile it behind type.
- The lockup, in order: Mambo on his panel, the In Good Company mark, the script wordmark, the endorsement beneath in Bodoni Moda capitals at 0.34em tracking. Every measure derives from the wordmark width W: mark height 0.233W centered on the lettering, endorsement at 0.275W below the lettering top, sparkle at the top right of the w. See the `.lk` component in `source/assets.html`. The mark is black on light grounds, white on ink, never recolored, never inside the paper, never below 16 px.
- Wordmark: the script artwork in `wordmark/`. Bodoni Moda stays the display face for headlines.
- Endorsement: Inter 650, uppercase, 0.24em tracking. Legal name in contracts and footers: In Good Company Impact Studio, LLC.
- Clear space equals the height of the capital M on every side. Minimum primary lockup width on screen: 220 px.
- One pattern per surface. The panel counts as one. Never behind body copy.
- No em dashes, no emoji, no contractions in documents or product screens. Social captions may use contractions.

## Confirmed

- The wordmark: the script lettering from Maddie's reference, as artwork (October 14, 2026).
- Mambo's color: cream, as drawn (October 14, 2026).

- The lockup layout: Mambo and panel, mark, wordmark, endorsement beneath (October 14, 2026).

- The In Good Company mark: supplied by Maddie on October 14, 2026, and set beside the endorsement line everywhere.

- Endorsement wording: "MamboFlow by In Good Company" (October 14, 2026).
- The color pop: argyle atomic panel behind Mambo, teal collar, gold charm (October 14, 2026).

## Pending

- Paper colors were sampled by eye from photographs; confirm against the roll. [CONFIRM]
- Headlines on the post templates are placeholder copy. [CONFIRM]

## Rendering

```
cd source
node render.js avatar header lock-primary   # any frame ids from assets.html
```

Requires Playwright with Chromium. Fonts, patterns, and mascot files are referenced relatively.
