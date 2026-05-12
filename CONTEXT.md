# Urban Court — Digital Menu Project
## Complete Context Document

---

## 1. The Venue

**Name:** Urban Court (STARTRIBE / UrbanCourt)
**Location:** Limassol, Cyprus
**Hours:** 07:00 – 22:00, seven days a week
**Type:** High-end, private fitness and wellness venue — padel, tennis, racquet sports
**Clientele:** VIP / private members only. Not a public venue.
**WiFi:** Network: `Urban Court` · Password: `Tennis-2026`

**Key detail:** Everything on the menu is **complimentary** — there are NO prices. The menu is a curated catalog of the bar offering for VIP guests. It should never feel like a restaurant menu. It should feel like being handed a private club's editorial book.

---

## 2. Menu Tiers

### Tier 1 — General VIP Menu (THIS PROJECT)
For all VIP guests at the venue. Accessed via QR code. Mobile-first web app.

### Tier 2 — Super VIP Drinks Menu (ALREADY BUILT)
A separate, highly exclusive drinks menu for the top clients. Already exists as `vip_menu_final.html`.
- 8 premium drinks: Ruinart Champagne, Bottega Gold Prosecco, Chablis, Primitivo di Manduria, Monkey 47 Gin, Macallan 12, Zacapa 23 Rum, Don Julio Reposado
- Design: near-black #080808, gold #c9a84c, Cormorant Garamond + Montserrat
- This is the DESIGN REFERENCE for the general menu

---

## 3. Design System

### Aesthetic Direction
**Dark luxury editorial** — extends the VIP menu's design language to the full offering.
NOT a sports-app aesthetic. NOT a green/white "padel club" look.
Feels like: Annabel's Members Club x Nobu x private luxury catalog.

### Colours (from VIP menu — KEEP THESE EXACTLY)
```css
--gold: #c9a84c
--gold-light: #e8d08a
--gold-dim: #7a6230
--black: #080808
--card: #111111 (or #121212)
--border: rgba(201,168,76,0.13)
--text: #e8e0d0
--muted: #5a5040
--muted2: #8a7a60
```

### Typography (from VIP menu — KEEP THESE EXACTLY)
- **Headings / item names:** `Cormorant Garamond` — weights 300, 400, 600; italic variants
- **Body / labels / tags:** `Montserrat` — weights 200, 300, 400, 500
- Google Fonts CDN: `https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Montserrat:wght@200;300;400;500&display=swap`

### Section Atmospheric Backgrounds
Each menu section has a unique colour "glow" bleeding into the black background.
Implemented as absolutely-positioned blurred radial-gradient orbs behind content.

| Section | Orb colours |
|---|---|
| Drinks / Smoothies | Berry purple `rgba(130,30,80,0.22)` + deep blue `rgba(50,20,120,0.18)` + red `rgba(180,40,40,0.14)` |
| Coffee | Espresso brown `rgba(110,55,15,0.25)` + dark amber `rgba(80,35,10,0.18)` |
| Tea | Jade green `rgba(30,80,45,0.22)` + olive `rgba(90,110,30,0.16)` |
| Beer | Golden amber `rgba(180,120,15,0.2)` + dark amber `rgba(140,80,10,0.14)` |
| Snacks | Warm orange `rgba(160,80,20,0.18)` |

### Current State: `urbancourt_menu_v2.html`
- Full hero landing screen with animated drifting gold orbs
- Sticky gold nav with section tabs and EN/RU language toggle
- All 5 menu sections: Drinks, Coffee, Tea, Beer, Snacks
- Cormorant Garamond item names, gold accent borders, ornamental dividers
- **Smoothie base selector** (see below) built and working
- No prices anywhere (complimentary)
- Bilingual: full EN/RU via `data-en` / `data-ru` attributes on every element

---

## 4. Complete Menu Content

### DRINKS — Non-Alcoholic

**Water**
- Evian Still — Natural mineral water, French Alps
- Evian Sparkling — Natural sparkling mineral water

**Soft Drinks**
- Coca-Cola (Classic, 330ml)
- Coca-Cola Zero (Zero Sugar, 330ml)
- Red Bull (Energy, 250ml)
- Red Bull Zero (Zero Sugar Energy, 250ml)

**Fresh Juices** (Freshly squeezed)
- Orange Fresh
- Grapefruit Fresh
- Orange & Grapefruit Mix (signature blend)

**Smoothies** (see base selector section below)
- Energy Mix — Banana · Strawberry · Blueberry
- Blue Banana — Banana · Blueberry
- Strawberry Banana — Banana · Strawberry
- Berry Mix — Blueberry · Strawberry

**Functional Drinks**
- Coconut Water (natural isotonic)
- Oshee Zero Sugar Lemon (electrolyte drink)
- Oshee Zero Sugar Multifruit (electrolyte drink)
- Powerade Mountain Blast (sports isotonic)
- Powerade Orange (sports isotonic)

---

### COFFEE

All milk-based drinks available with these milk options:
**Regular (3%) · Lactose-free · Oat · Almond · Coconut · Soy**

**Hot / Espresso Based**
- Espresso (single, 30ml)
- Double Espresso (60ml)
- Americano (200ml)
- Cappuccino (180ml)
- Latte (240ml)

**Iced / Cold**
- Freddo Espresso (Greek-style, shaken over ice)
- Freddo Cappuccino (cold espresso + iced milk foam)
- Iced Latte (espresso over ice + cold milk)
- Iced Strawberry Latte (with strawberry syrup)

---

### TEA

**Classic Leaf Teas**
- Earl Grey — Black tea, natural bergamot
- Huang Shan Mao Feng — Chinese green tea, Anhui Province. Floral, delicate, one of China's 10 most famous teas.

**Herbal & Botanical**
- Chamomile — Pure chamomile blossoms, caffeine-free, calming
- Meditation Tea — Apple · Lemongrass · Rosehip · Chamomile · Lavender · Mint (caffeine-free)

**Fruit Puree Teas**
- Mango Passion — Mango · Passion fruit · Orange · Cinnamon
- Raspberry Citrus — Raspberry · Orange · Cinnamon

---

### BEER

**With Alcohol (330ml bottles)**
- Heineken — Dutch lager, 5% ABV, since 1873
- Corona — Mexican lager, 4.5% ABV, since 1925

**Alcohol Free (330ml bottles)**
- Heineken 0%
- Corona 0%

---

### FUNCTIONAL SNACKS

**Protein Bars**
- Power Pro Classic Chocolate Fudge — 20g protein
- Kellogg's Special K High Protein — cereal bar, high protein content

---

## 5. Smoothie Base Selector — Key Feature

Every smoothie card has an inline base selector. The guest picks their preferred base before ordering from a member of staff.

**Two groups of options:**

**Group 1 — Milk**
Regular (3%) · Lactose-free · Oat · Almond · Coconut · Soy

**Group 2 — Alternative Base**
Coconut Water · Still Water · Sparkling Water · Ice

**UX behaviour:** Tap a pill → it highlights in gold. One selection per group. Pills styled as small text buttons with gold border. Visible but subtle — does not disrupt the card's editorial feel.

**Implementation:** Currently using `onclick="selectBase(this,'group-id')"` JS function + `.selected` CSS class.

---

## 6. Technical Architecture

### Current Format
Single self-contained `.html` file. No framework. Vanilla HTML/CSS/JS.
Can be hosted on:
- **Cloudflare Pages** (free, instant deploy from GitHub)
- **Vercel** (free)
- **Netlify** (free)
- Served via QR code pointing to the hosted URL

### Bilingual System
All text elements have `data-en="..."` and `data-ru="..."` attributes.
`setLang(l)` function swaps all content on toggle.

### Navigation / Section Switching
`show(id, btn)` function shows/hides sections and updates active nav tab.

### Planned Architecture (Phase 2 onwards)
Migrate to **React + Vite** or **Next.js** for:
- Component-based item cards
- CMS-style JSON data layer (easy menu updates)
- Court ordering system (see Phase 2)

---

## 7. Phase Roadmap

### Phase 1 — Menu Catalog (current)
✅ Full menu with all items
✅ Dark luxury editorial design
✅ Bilingual EN/RU
✅ Smoothie base selector
✅ No prices (complimentary)
🔲 Real photography integrated (see Photo Brief)
🔲 Hosted and live with QR code

### Phase 2 — Court Ordering
Guest selects their court number → builds their order → sends to staff.
No POS required. Notification can go to:
- WhatsApp (via WhatsApp Business API)
- A simple admin dashboard page
- Email/SMS

Flow: Browse menu → Add items to order → Select court (Court 1–6 dropdown) → Confirm → Order sent to bar staff

### Phase 3 — CRM Integration
Client preferences stored. When a known guest scans QR, their preferred base/milk is pre-selected. Connects to the STARTRIBE CRM system being developed internally.

---

## 8. Photography Brief

When real photos are taken, they replace the atmospheric gradient backgrounds.
The technique used in the VIP menu (CSS `mask-image` radial gradient to fade bottle images into black) should be used for product shots.

**Priority shots:**

| Shot | Description | Usage |
|---|---|---|
| Hero image | Courts at dusk/evening from slightly elevated angle. Dramatic ambient lighting. NOT the red front doors. | Hero section background |
| Smoothie hero | 2-3 smoothies in tall clear glasses, fresh fruit scattered on dark marble/stone surface, dramatic side lighting | Smoothies section background / card images |
| Coffee hero | Close-up of a perfect latte art or cappuccino. Dark background. Steam. Macro. | Coffee section |
| Tea hero | Glass teapot or cup with fruit puree tea glowing against black surface | Tea section |
| Beer hero | Condensation droplets on a Heineken bottle, dark background, dramatic lighting | Beer section |
| Snacks | Bars arranged on dark stone surface, simple still life | Snacks section |
| Bar setup | The actual bar area at Urban Court — wide shot showing premium feel | About / venue section |

**Shooting notes:**
- Always dark or black background (or easy to mask)
- Dramatic side/rim lighting preferred — makes product glow against dark
- iPhone camera fine, use Portrait mode or Pro mode with manual exposure
- Shoot RAW if possible, JPG is fine
- Wet glass / condensation adds a lot of luxury feel

---

## 9. Files in This Package

| File | Description |
|---|---|
| `CONTEXT.md` | This document — full project context |
| `PROMPTS.md` | Ready-to-use prompts for continuing in any AI coding environment |
| `urbancourt_menu_v2.html` | Current working version of the general VIP menu |
| `vip_menu_final.html` | The Super VIP drinks menu — design reference |

---

## 10. Key Decisions Made

- No prices anywhere on the general menu (complimentary)
- Design extends the VIP menu's dark/gold aesthetic — NOT the green/white sport-wellness look
- Single HTML file for Phase 1 (simplest hosting path)
- The red front-door image from OddMenu is not used — courts/bar setup is the right hero
- The general menu and VIP menu are deliberately different tiers — the VIP menu stays exclusive
- EN/RU bilingual (Cyprus VIP clientele is heavily Russian-speaking)
- Smoothie base selector is "incognito but visible" — integrated into the card, not a popup
