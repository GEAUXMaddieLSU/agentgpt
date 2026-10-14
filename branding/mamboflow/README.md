# MamboFlow brand kit

MamboFlow is the In Good Company Impact Studio product for getting social. This folder holds the first brand integration draft: the mascot in black and white, the lockups, the pattern language, and the application mockups. Everything here follows the In Good Company brand system (black and white only, Bodoni Moda and Inter, square corners, hairline rules, generous space).

## Brand architecture

In Good Company is the parent brand. MamboFlow is an endorsed product. It carries the line "By In Good Company" on every surface, inherits the studio's type and palette, and adds three things of its own:

1. Mambo, the French bulldog mascot, always drawn in black and white.
2. Three mid-century patterns: Signal (concentric rings), Atomic (starbursts), Boomerang (flat kidney shapes).
3. Mambo Mustard (#D6A026), one accent, used on product surfaces only. Never on studio materials.

## Files

| Path | What it is |
| --- | --- |
| `mascot/mambo-classic.png` | Default treatment. Black-and-white illustration, transparent background, 1254 px. |
| `mascot/mambo-ink.png` | Full watercolor shading in grayscale. Large editorial use. |
| `mascot/mambo-stamp.png` | Pure two-tone. Favicons, sizes under 64 px, print. |
| `mascot/mambo-classic-sticker.png` | Classic with a white keyline. Dark grounds. |
| `mascot/mambo-spot-mustard.png` | Classic with the collar in Mambo Mustard. Optional. |
| `lockups/lock-primary.png` | Mambo + wordmark + endorsement, horizontal, transparent. |
| `lockups/lock-stacked.png` | Stacked version for square and tall spaces, transparent. |
| `lockups/lock-rev.png` | Reversed lockup on ink. |
| `social/avatar.png`, `social/avatar-dark.png` | Profile avatars, 400 x 400. |
| `social/header.png` | X header, 1500 x 500. |
| `social/post-quote.png`, `social/post-announce.png` | Post templates, 1080 x 1080. |
| `app/icon.png`, `app/icon-dark.png`, `app/fav.png` | App icon 512 x 512 and favicon source 128 x 128. |
| `app/signin.png` | Sign-in screen mockup, 1440 x 900. |
| `app/sig.png` | Email signature strip, 600 x 140. |
| `patterns/tile-*.png` | The three pattern tiles, 600 x 600. |
| `source/assets.html` | The HTML compositions every PNG was rendered from. Edit here, re-render with Playwright. |
| `source/mascot_convert.py` | The script that produced the black-and-white mascot treatments from the color original. |
| `board/index.html` | The brand board (also published as a Claude artifact). |
| `fonts/` | Bodoni Moda and Inter variable fonts (SIL Open Font License), copied from the In Good Company design system. |

## Rules in brief

- Mambo is black and white. The collar is the only place color may live, and only on MamboFlow surfaces.
- Lockup order never changes: Mambo, wordmark, endorsement line.
- Wordmark: Bodoni Moda 500, tracking -0.035em, "Mambo" upright and "Flow" italic.
- Endorsement: Inter 650, uppercase, 0.24em tracking. Legal name in contracts and footers: In Good Company Impact Studio, LLC.
- Clear space equals the height of the capital M on every side. Minimum primary lockup width on screen: 220 px.
- One pattern per surface, behind Mambo or beside a headline, never behind body copy.
- No em dashes, no emoji, no contractions in documents or product screens. Social captions may use contractions.

## Open decisions

1. Accent color: Mambo Mustard on product surfaces (recommended) or strict black and white everywhere.
2. Default mascot treatment: Classic (recommended) or Stamp.
3. Endorsement wording: "By In Good Company" (recommended) or "An In Good Company Impact Studio product".

## To verify

- The In Good Company swirl mark and primary logo files were not readable from the design system's asset store or the OneDrive folder in this session. The endorsement is set in type until the supplied mark is dropped in. [CONFIRM]
- Proposed lines ("Social, in good company." and others on the board) are drafts, not approved copy. [CONFIRM]

## Rendering

```
cd source
node render.js avatar header lock-primary   # any frame ids from assets.html
```

Requires Playwright with Chromium. Fonts and mascot files are referenced relatively.
