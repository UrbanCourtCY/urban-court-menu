"""
PART 5 — Move price-badge into the card eyebrow row.

Uses NO DOTALL mode. Each pattern is line-aware and uses indentation
backreferences so it cannot bleed across card boundaries.
"""
import re
from pathlib import Path

FILE = Path(__file__).parent / "index.html"


# ── Pattern A: drink/tea/beer cards WITH card-text AND card-origin ─────────
# Indentation: 6sp price/inner, 8sp card-text, 10sp origin/name
PATTERN_A = re.compile(
    r'([ ]{6})<div class="price-badge">(.*?)</div>\n'
    r'\1<div class="card-inner"><div class="card-accent"></div><div class="card-body">\n'
    r'\1  <div class="card-text">\n'
    r'\1    (<div class="card-origin"[^\n]*</div>)\n'
    r'\1    (<div class="card-name")'
)

def replace_A(m):
    ind = m.group(1)
    price = m.group(2)
    origin = m.group(3)
    name_open = m.group(4)
    return (
        f'{ind}<div class="card-inner"><div class="card-accent"></div><div class="card-body">\n'
        f'{ind}  <div class="card-text">\n'
        f'{ind}    <div class="card-eyebrow">{origin}<div class="price-badge">{price}</div></div>\n'
        f'{ind}    {name_open}'
    )


# ── Pattern B: drink/tea cards WITHOUT card-origin (Earl Grey, Chamomile) ──
PATTERN_B = re.compile(
    r'([ ]{6})<div class="price-badge">(.*?)</div>\n'
    r'\1<div class="card-inner"><div class="card-accent"></div><div class="card-body">\n'
    r'\1  <div class="card-text">\n'
    r'\1    (<div class="card-name")'
)

def replace_B(m):
    ind = m.group(1)
    price = m.group(2)
    name_open = m.group(3)
    return (
        f'{ind}<div class="card-inner"><div class="card-accent"></div><div class="card-body">\n'
        f'{ind}  <div class="card-text">\n'
        f'{ind}    <div class="card-eyebrow"><div class="price-badge">{price}</div></div>\n'
        f'{ind}    {name_open}'
    )


# ── Pattern C: coffee/matcha cards (coffee-img-wrap + card-origin, 8sp) ────
PATTERN_C = re.compile(
    r'([ ]{6})<div class="price-badge">(.*?)</div>\n'
    r'\1<div class="card-inner"><div class="card-accent"></div><div class="card-body">\n'
    r'\1  (<div class="coffee-img-wrap[^\n]*</div>)\n'
    r'\1  (<div class="card-origin"[^\n]*</div>)\n'
    r'\1  (<div class="card-name")'
)

def replace_C(m):
    ind = m.group(1)
    price = m.group(2)
    imgwrap = m.group(3)
    origin = m.group(4)
    name_open = m.group(5)
    return (
        f'{ind}<div class="card-inner"><div class="card-accent"></div><div class="card-body">\n'
        f'{ind}  {imgwrap}\n'
        f'{ind}  <div class="card-eyebrow">{origin}<div class="price-badge">{price}</div></div>\n'
        f'{ind}  {name_open}'
    )


# ── Pattern D: snack cards (card-origin at 8sp, no card-text wrapper) ──────
PATTERN_D = re.compile(
    r'([ ]{6})<div class="price-badge">(.*?)</div>\n'
    r'\1<div class="card-inner"><div class="card-accent"></div><div class="card-body">\n'
    r'\1  (<div class="card-origin">[^\n]*</div>)\n'
    r'\1  (<div class="card-name")'
)

def replace_D(m):
    ind = m.group(1)
    price = m.group(2)
    origin = m.group(3)
    name_open = m.group(4)
    return (
        f'{ind}<div class="card-inner"><div class="card-accent"></div><div class="card-body">\n'
        f'{ind}  <div class="card-eyebrow">{origin}<div class="price-badge">{price}</div></div>\n'
        f'{ind}  {name_open}'
    )


# ── Pattern E: beer cards (card-origin + card-text, same as A) ─────────────
# Same as A but cards have different closing; same pattern works.

# ── Also handle cards with dual-price badge (Cappuccino, Latte) ────────────
# The (.*?) in patterns handles multi-line badge content without DOTALL
# because dual-price badge is: €1.00<br><span...>alt €1.50</span>
# The </div> match picks the FIRST </div> — but span closes before div!
# So (.*?) should correctly capture the full badge content including <br><span>.
# HOWEVER, [^\n]* in the coffee-img-wrap will fail if the span is on the same line.
# Dual-price cards (Cappuccino, Latte) ARE coffee cards, so they hit Pattern C.
# The (.*?) for price stops at first </div> — which is the badge's own </div>. ✓


def main():
    html = FILE.read_text(encoding="utf-8")
    orig = html

    # Apply patterns in order — C before A/B to handle coffee cards first
    html, n_c = PATTERN_C.subn(replace_C, html)
    html, n_a = PATTERN_A.subn(replace_A, html)
    html, n_b = PATTERN_B.subn(replace_B, html)
    html, n_d = PATTERN_D.subn(replace_D, html)

    total = html.count('<div class="price-badge">')
    print(f"Pattern A (drink+origin): {n_a}")
    print(f"Pattern B (no origin):    {n_b}")
    print(f"Pattern C (coffee):       {n_c}")
    print(f"Pattern D (snack):        {n_d}")
    print(f"price-badge divs total:   {total}")
    print(f"double card-eyebrow:      {html.count('<div class=\"card-eyebrow\"><div class=\"card-eyebrow\">')}")

    FILE.write_text(html, encoding="utf-8")
    print("Done.")


if __name__ == "__main__":
    main()
