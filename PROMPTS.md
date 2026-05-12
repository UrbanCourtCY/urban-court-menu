# Urban Court Menu — AI Prompts
## Ready-to-use prompts for continuing the project

---

## HOW TO USE THIS FILE

Copy and paste the relevant prompt into your AI coding environment (Cursor, Claude Code, Windsurf, etc.).
Always start with **PROMPT 0** (project setup) in any new session before anything else.
Then use the specific prompts below for each feature you want to build.

---

---

## PROMPT 0 — PROJECT SETUP (use this first in every new session)

```
You are helping me build a luxury digital bar menu for Urban Court, a private VIP fitness and wellness venue in Limassol, Cyprus. Everything on the menu is complimentary — there are NO prices. Clientele is VIP/private members only.

Read the CONTEXT.md file in this project to understand the full brief, design system, menu content, and roadmap before doing anything.

The current working file is urbancourt_menu_v2.html — this is the file we are building on. Do not rewrite it from scratch unless I explicitly ask.

Design principles to always respect:
- Dark luxury editorial aesthetic. Near-black background (#080808), gold (#c9a84c), Cormorant Garamond headings, Montserrat body text.
- Never feels like a restaurant menu or a food delivery app. Feels like a private members club editorial catalog.
- Bilingual EN/RU: every text element must have data-en and data-ru attributes. The setLang() function handles switching.
- No prices anywhere.
- Mobile-first. This is primarily viewed on phone after scanning a QR code.

Confirm you have read CONTEXT.md and understood the brief before proceeding.
```

---

---

## PROMPT 1 — INTEGRATE REAL PHOTOS

```
I have taken photos for the Urban Court menu and I am attaching them now. 

For each photo I give you:
1. Add it to the relevant section of urbancourt_menu_v2.html
2. Use the same CSS mask-image technique used in vip_menu_final.html to fade the image into the black background — radial gradient mask, edges fade to transparent
3. The image should sit behind the section content as an atmospheric background, or float beside/above the card depending on the section
4. Do not let the image reduce text readability — add a subtle dark overlay if needed
5. Keep the coloured atmospheric orb glows underneath the image

Photos I am providing:
[DESCRIBE YOUR PHOTOS HERE WHEN YOU HAVE THEM — e.g. "smoothie_hero.jpg — tall glass smoothie on dark marble surface" etc.]
```

---

## PROMPT 2 — REFINE THE SMOOTHIE BASE SELECTOR

```
In urbancourt_menu_v2.html, the smoothie cards have a base selector (milk options + alternative bases). 

I want to improve this feature:
1. Add a subtle animated highlight when a base is selected — the pill should glow gold softly, not just change border colour
2. Add a tiny confirmation line below the selector that appears after selection, e.g. "Your Energy Mix will be prepared with Oat Milk" — styled in a very small, italic, gold-dim colour
3. Make sure the selector resets cleanly if the user navigates away and comes back to the same card
4. Ensure the RU language version of the confirmation line also works correctly with setLang()

Keep the same overall card styling — the selector should feel like it grows naturally from the card without disrupting the editorial feel.
```

---

## PROMPT 3 — ADD COURT ORDERING SYSTEM (Phase 2)

```
I want to add a court ordering feature to urbancourt_menu_v2.html.

The flow:
1. Guest browses the menu and taps an "Add" button on any item (small, gold, unobtrusive — does not dominate the card)
2. A persistent floating order tray appears at the bottom of the screen showing the number of items selected
3. Tapping the tray expands an order summary showing all selected items with quantities
4. At the top of the order summary, the guest selects their court number from a dropdown (Courts 1 through 6, plus "Lounge Area" and "Terrace")
5. For any smoothie in the order, the order summary shows which base they selected
6. A "Send Order" button submits the order

For now, "Send Order" should:
- Display a beautiful confirmation screen ("Your order has been received. We will bring it to Court [X] shortly.")
- Clear the order tray
- (Leave a TODO comment where the actual backend submission will go)

Style everything in the same dark/gold aesthetic. The floating tray should feel premium, not like a DoorDash cart. Small, elegant, fixed to the bottom of the screen.
```

---

## PROMPT 4 — HOST ON CLOUDFLARE PAGES

```
Walk me through deploying urbancourt_menu_v2.html to Cloudflare Pages so it's live with a real URL I can use for the QR code.

I have a Cloudflare account. I want:
1. Step-by-step instructions for creating a new Cloudflare Pages project from a single HTML file
2. How to set up a custom subdomain if I have a domain connected to Cloudflare (e.g. menu.urbancourt.cy)
3. How to update the live site when I make changes to the file
4. How to generate a QR code that points to the live URL

Keep the instructions simple — I am not a developer.
```

---

## PROMPT 5 — GENERATE QR CODE PAGE

```
Create a separate file called urbancourt_qr.html that:
1. Displays a single QR code linking to [INSERT MENU URL HERE]
2. Styled in the same dark/gold Urban Court aesthetic — the QR code itself should have a gold/dark colour scheme, not the default black-and-white
3. Below the QR code, small text: "Scan to view our menu" in English and Russian
4. The Urban Court logo/wordmark in Cormorant Garamond above the QR code
5. This page should be printable — when printed (Ctrl+P), it outputs cleanly on A4 paper, centred, no browser chrome

Use a JS QR code library from cdnjs.cloudflare.com to generate the QR code client-side.
```

---

## PROMPT 6 — ADD RUSSIAN LANGUAGE IMPROVEMENTS

```
Review all the Russian translations in urbancourt_menu_v2.html and improve them.

Current approach: every element has data-en and data-ru attributes, toggled by setLang().

Issues to fix:
1. Some item names are left in English in the Russian version (e.g. "Energy Mix", "Blue Banana", "Berry Mix", "Freddo Espresso", "Freddo Cappuccino") — these are brand names and should stay in English, but make sure their descriptions and subtitles are fully translated
2. Check all section headers, subsection labels, tags, and nav buttons are properly translated
3. The hero subtitle and button text should be in proper Russian
4. All tag text (e.g. "Antioxidant", "Post-Workout", "Zero Sugar") should have Russian equivalents in their data-ru attributes

Do a full audit and fix everything — do not miss anything.
```

---

## PROMPT 7 — ADD ANIMATED SECTION TRANSITIONS

```
Improve the section transition animation in urbancourt_menu_v2.html.

Currently when switching sections, there is a simple fadeIn/translateY animation. I want this to be more cinematic:

1. When a section exits: fade out + slight scale down (0.98) over 200ms
2. When a section enters: fade in + slide up from 15px below over 350ms, with a slight ease-out curve
3. The atmospheric background orbs in each section should also animate in separately — they should drift in from their corners with a longer 600ms transition, giving a depth effect
4. The section number ("01 — Bar", "02 — Bar" etc.) should appear with a slight delay after the section starts animating in
5. Do not use any libraries — pure CSS transitions and JS class toggling only

The total transition should feel smooth and premium, like flipping a page in a luxury magazine.
```

---

## PROMPT 8 — BUILD ADMIN PANEL (simple menu editor)

```
Create a separate file called urbancourt_admin.html — a simple password-protected admin panel for updating the menu.

Password: [YOU SET THIS]

Features:
1. Password screen on load — Urban Court branded, dark/gold style
2. After login, shows a list of all menu items from urbancourt_menu_v2.html
3. Admin can edit: item name (EN + RU), description (EN + RU), tags, and toggle items as "available" or "temporarily unavailable"
4. Items marked unavailable appear greyed out with a subtle "Currently unavailable" label on the guest-facing menu
5. An "Export" button that outputs an updated urbancourt_menu_v2.html with all changes applied
6. No backend needed — all state stored in localStorage for now

Style the admin panel in the same dark/gold aesthetic but more functional — think: a refined dashboard, not a consumer menu.
```

---

## PROMPT 9 — CONVERT TO REACT + VITE (Phase 2 migration)

```
I want to migrate urbancourt_menu_v2.html from a single HTML file to a proper React + Vite project.

Create the project structure:
- /src/components/MenuCard.jsx
- /src/components/BaseSelector.jsx  
- /src/components/SectionHeader.jsx
- /src/components/CategoryNav.jsx
- /src/data/menuData.js (all menu content as structured JSON)
- /src/i18n/en.js and /src/i18n/ru.js (all translations)
- /src/App.jsx
- /src/main.jsx
- /src/styles/globals.css (all CSS variables and base styles)

Preserve 100% of the visual design from the HTML file — same colours, fonts, animations, card styles, base selector behaviour.

The data layer in menuData.js should make it trivial to add, remove, or edit menu items without touching any component code.

Use Vite as the build tool. No TypeScript for now — plain JavaScript.
```

---

## PROMPT 10 — FULL REDESIGN WITH PHOTOS (future)

```
I now have high-quality photos for every section of the Urban Court menu. I want to do a full upgrade of urbancourt_menu_v2.html using these images.

For each section, I want:
1. A full-bleed section hero image at the top — the image fades into the black background at the bottom using a gradient mask, similar to how the VIP drinks menu uses bottle photography
2. Individual item cards can optionally have a small product image (50x50px, masked to fade edges) where I provide photos
3. The atmospheric colour orbs are now secondary to the real photography — reduce their opacity when a hero image is present
4. The hero landing screen should use a real photo of the Urban Court courts (I will provide this)

I am attaching all photos now. [ATTACH PHOTOS]

For each photo, use the CSS mask-image radial gradient technique from vip_menu_final.html — this creates the premium "floating in darkness" effect.
```

---

## NOTES FOR YOUR AI CODING ENVIRONMENT

- Always work on `urbancourt_menu_v2.html` as the primary file
- `vip_menu_final.html` is the design reference — look at its CSS for exact technique on photo masking, gold styling, card hover effects
- `CONTEXT.md` has the full brief — refer to it if uncertain about design decisions
- The guest never sees prices — if you accidentally add any, remove them
- The menu is EN/RU bilingual — any new text must have both `data-en` and `data-ru` attributes
- Mobile-first — always check how things look at 375px width before desktop
