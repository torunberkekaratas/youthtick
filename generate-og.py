"""
YouthTICK OG Image Generator
Creates 1200x630px social preview images for each page.
Run: python3 generate-og.py
"""

from PIL import Image, ImageDraw, ImageFont
import os

# ── Brand colours ─────────────────────────────────────────────────────────────
NAVY_DEEP  = (10,  24,  40)   # --navy-deep  #0A1828
NAVY       = (22,  37,  64)   # --navy       #162540
BLUE_VIVID = (37,  99, 235)   # --blue-vivid #2563EB
BLUE_MID   = (59, 130, 246)   # --blue-mid   #3B82F6
GOLD       = (184,138,  40)   # --gold       #B88A28
CREAM      = (245,239,224)    # --cream      #F5EFE0
WHITE      = (255,255,255)
GRAY_LIGHT = (180,192,210)

# ── Fonts ─────────────────────────────────────────────────────────────────────
FONT_BOLD   = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
FONT_NORMAL = '/System/Library/Fonts/Supplemental/Arial.ttf'

W, H = 1200, 630

def make_og(filename, eyebrow, title, subtitle, accent_color=BLUE_VIVID):
    img  = Image.new('RGB', (W, H), NAVY_DEEP)
    draw = ImageDraw.Draw(img)

    # ── Gradient overlay (manual vertical bands) ──────────────────────────────
    for y in range(H):
        t = y / H
        r = int(NAVY_DEEP[0] + (NAVY[0] - NAVY_DEEP[0]) * t * 0.6)
        g = int(NAVY_DEEP[1] + (NAVY[1] - NAVY_DEEP[1]) * t * 0.6)
        b = int(NAVY_DEEP[2] + (NAVY[2] - NAVY_DEEP[2]) * t * 0.6)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # ── Decorative geometry ───────────────────────────────────────────────────
    # Large faint circle — top right
    cx, cy, cr = 1050, -80, 340
    for r in range(cr, cr - 4, -1):
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], outline=(37, 99, 235, 15))

    # Accent bar — left edge
    draw.rectangle([0, 0, 6, H], fill=accent_color)

    # Thin horizontal rule
    draw.rectangle([72, 140, W - 72, 142], fill=(*BLUE_VIVID, 60))

    # ── Dot grid (subtle) ─────────────────────────────────────────────────────
    for gx in range(800, W - 40, 30):
        for gy in range(40, 200, 30):
            draw.ellipse([gx, gy, gx+2, gy+2], fill=(255,255,255,18))

    # ── Text ──────────────────────────────────────────────────────────────────
    try:
        f_eyebrow = ImageFont.truetype(FONT_BOLD,   22)
        f_title   = ImageFont.truetype(FONT_BOLD,   68)
        f_title_sm= ImageFont.truetype(FONT_BOLD,   54)
        f_sub     = ImageFont.truetype(FONT_NORMAL, 28)
        f_brand   = ImageFont.truetype(FONT_BOLD,   26)
        f_url     = ImageFont.truetype(FONT_NORMAL, 22)
    except Exception:
        f_eyebrow = f_title = f_title_sm = f_sub = f_brand = f_url = ImageFont.load_default()

    # Brand name — top left
    draw.text((72, 52), 'YouthTICK', font=f_brand, fill=WHITE)
    # Gold dot after brand name
    brand_w = draw.textlength('YouthTICK', font=f_brand)
    draw.ellipse([72 + brand_w + 8, 62, 72 + brand_w + 14, 68], fill=GOLD)

    # Eyebrow label
    draw.text((72, 162), eyebrow.upper(), font=f_eyebrow, fill=(*accent_color,))

    # Title — auto-size if too long
    title_font = f_title if len(title) < 30 else f_title_sm

    # Word-wrap title to 2 lines max
    words      = title.split()
    lines      = []
    current    = ''
    max_w      = W - 160
    for word in words:
        test = (current + ' ' + word).strip()
        if draw.textlength(test, font=title_font) < max_w:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)

    y_title = 230
    line_h  = int(title_font.size * 1.15)
    for line in lines[:2]:
        draw.text((72, y_title), line, font=title_font, fill=WHITE)
        y_title += line_h

    # Subtitle
    if subtitle:
        draw.text((72, y_title + 24), subtitle, font=f_sub, fill=GRAY_LIGHT)

    # URL — bottom left
    draw.text((72, H - 56), 'youthtick.org', font=f_url, fill=(*GRAY_LIGHT, 160))

    # Erasmus+ badge — bottom right
    badge_text = 'Erasmus+ Oriented'
    bw = draw.textlength(badge_text, font=f_url) + 24
    bx = W - bw - 72
    draw.rounded_rectangle([bx, H-60, W-72, H-32], radius=20,
                            fill=(*BLUE_VIVID, 40), outline=(*BLUE_VIVID, 80))
    draw.text((bx + 12, H - 56), badge_text, font=f_url, fill=(*WHITE, 180))

    # ── Save ──────────────────────────────────────────────────────────────────
    out = os.path.join(os.path.dirname(__file__), filename)
    img.save(out, 'JPEG', quality=90, optimize=True)
    print(f'  ✓  {filename}')

# ── Page definitions ──────────────────────────────────────────────────────────
pages = [
    ('og-image.jpg',         'YouthTICK',             'Opening doors for young people',        'Erasmus+ Youth Initiative · Yalova, Türkiye',     BLUE_VIVID),
    ('og-index.jpg',         'Home',                   'Opening doors for young people',        'Erasmus+ Youth Initiative · Yalova, Türkiye',     BLUE_VIVID),
    ('og-blog.jpg',          'Blog & Articles',        'Erasmus+, Civic Participation',         'In-depth guides written by youth practitioners',   GOLD),
    ('og-opportunities.jpg', 'European Opportunities', 'The doors are open.',                   'Erasmus+, ESC, EU youth funding for young Turks',  BLUE_MID),
    ('og-about.jpg',         'About YouthTICK',        'A new kind of youth organization.',     'Building bridges across Europe since 2026',        BLUE_VIVID),
    ('og-focus.jpg',         'Programs & Focus Areas', 'Six pillars of youth action.',          'Erasmus+, Participation, Sustainability & more',   BLUE_MID),
    ('og-projects.jpg',      'Our Projects',           'Where ideas become programs.',          'Civic engagement & international cooperation',     GOLD),
    ('og-partnership.jpg',   'Partner With Us',        'Real partnerships. Real impact.',       'Join YouthTICK\'s European partner network',       GOLD),
    ('og-team.jpg',          'Meet the Team',          'The people behind YouthTICK.',         'Youth workers & civic leaders from Yalova, TR',    BLUE_VIVID),
    ('og-contact.jpg',       'Contact YouthTICK',      'Let\'s talk.',                          'Reach us at info@youthtick.org',                   BLUE_MID),
    ('og-volunteer.jpg',     'Join YouthTICK',         'Be part of something real.',            'Volunteer, intern or partner with our team',       BLUE_VIVID),
]

print('Generating OG images...')
for filename, eyebrow, title, subtitle, color in pages:
    make_og(filename, eyebrow, title, subtitle, color)

print(f'\nDone — {len(pages)} images generated.')
