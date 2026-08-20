# -*- coding: utf-8 -*-
"""Sinh cover pepe (SVG) cho 2 bai blog. Pepe la component tai su dung."""

GREEN, GREEN_D, LINE = "#74a244", "#66913a", "#2f4a1c"
EYE_W, SKIN = "#fbfaf6", "#a1786c"
SHIRT, SHIRT_D = "#2f6fb5", "#22364d"
BG, BG_FLOOR = "#efe9dd", "#e4dbc9"

def pepe(x, y, s, expr="sad", shirt=SHIRT, shirt_d=SHIRT_D, accessory=None):
    """expr: sad | smug | shock   accessory: None | glasses"""
    E, R, CY = 54, 34, -44          # eye offset, radius, center-y
    cfg = {
        "sad":   dict(sag=-46, py=-32, pr=14, lid=True),
        "smug":  dict(sag=-40, py=-30, pr=14, lid=True),
        "shock": dict(sag=-60, py=-40, pr=11, lid=False),
    }[expr]
    sag, py, pr, lid = cfg["sag"], cfg["py"], cfg["pr"], cfg["lid"]

    def lid_path(cx):
        if not lid:
            return ""
        return (f'<path d="M {cx-R} {CY} A {R} {R} 0 0 1 {cx+R} {CY} '
                f'C {cx+18} {sag}, {cx-18} {sag}, {cx-R} {CY} Z" '
                f'fill="{GREEN_D}" stroke="{LINE}" stroke-width="4.5"/>')

    if expr == "shock":
        mouth = (f'<path d="M -96 18 C -60 4, 60 4, 96 18 C 92 46, 54 62, 0 62 '
                 f'C -54 62, -92 46, -96 18 Z" fill="{SKIN}" stroke="{LINE}" stroke-width="5"/>'
                 f'<ellipse cx="0" cy="36" rx="58" ry="20" fill="#5b3b34" stroke="{LINE}" stroke-width="4"/>')
    else:
        mouth = (f'<path d="M -106 22 C -66 6, 66 6, 106 22 C 102 36, 56 48, 0 48 '
                 f'C -56 48, -102 36, -106 22 Z" fill="{SKIN}" stroke="{LINE}" stroke-width="5"/>'
                 f'<path d="M -106 22 C -60 34, 60 34, 106 22" fill="none" stroke="{LINE}" stroke-width="4.5"/>')

    if accessory == "glasses":
        acc = ('<g stroke="#111820" stroke-width="4.5" stroke-linejoin="round">'
               '<rect x="-96" y="-76" width="84" height="64" rx="13" fill="#1f2937"/>'
               '<rect x="12" y="-76" width="84" height="64" rx="13" fill="#1f2937"/>'
               '<path d="M -12 -54 L 12 -54" stroke-width="8"/>'
               '<path d="M -96 -60 L -118 -64" stroke-width="7"/>'
               '<path d="M 96 -60 L 118 -64" stroke-width="7"/>'
               '</g>'
               '<path d="M -88 -34 L -66 -68" stroke="#ffffff" stroke-opacity="0.28" stroke-width="7" stroke-linecap="round"/>'
               '<path d="M 20 -34 L 42 -68" stroke="#ffffff" stroke-opacity="0.28" stroke-width="7" stroke-linecap="round"/>')
    else:
        acc = ""

    return f'''<g transform="translate({x},{y}) scale({s})" stroke-linecap="round" stroke-linejoin="round">
  <path d="M -74 44 C -124 74, -146 134, -150 210 L 150 210 C 146 134, 124 74, 74 44 Z"
        fill="{shirt}" stroke="{shirt_d}" stroke-width="5"/>
  <path d="M -118 -10 C -118 -62, -70 -88, 0 -88 C 70 -88, 118 -62, 118 -10
           C 118 26, 96 52, 56 64 C 36 70, -36 70, -56 64 C -96 52, -118 26, -118 -10 Z"
        fill="{GREEN}" stroke="{LINE}" stroke-width="5.5"/>
  <circle cx="-{E}" cy="{CY}" r="{R}" fill="{EYE_W}" stroke="{LINE}" stroke-width="5"/>
  <circle cx="{E}"  cy="{CY}" r="{R}" fill="{EYE_W}" stroke="{LINE}" stroke-width="5"/>
  <circle cx="-47" cy="{py}" r="{pr}" fill="#1b1b1b"/>
  <circle cx="47"  cy="{py}" r="{pr}" fill="#1b1b1b"/>
  {lid_path(-E)}{lid_path(E)}
  {acc}
  <ellipse cx="-16" cy="4" rx="4.5" ry="3.2" fill="{LINE}"/>
  <ellipse cx="16"  cy="4" rx="4.5" ry="3.2" fill="{LINE}"/>
  {mouth}
</g>'''

def arm(d, hand, s=1.0, shirt=SHIRT):
    """d = path cua tay (sleeve), hand = (cx,cy,r) ban tay xanh"""
    hx, hy, hr = hand
    return (f'<path d="{d}" fill="none" stroke="{SHIRT_D}" stroke-width="{26*s}" stroke-linecap="round"/>'
            f'<path d="{d}" fill="none" stroke="{shirt}" stroke-width="{18*s}" stroke-linecap="round"/>'
            f'<circle cx="{hx}" cy="{hy}" r="{hr}" fill="{GREEN}" stroke="{LINE}" stroke-width="4.5"/>')

def sweat(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<path d="M 0 0 C -9 14, -11 26, 0 26 C 11 26, 9 14, 0 0 Z" '
            f'fill="#7fd0ee" stroke="#2f6f86" stroke-width="3.5"/></g>')

def pytest_logo(x, y, s=1.0):
    """3 thanh mau + wordmark, xap xi logo pytest"""
    return f'''<g transform="translate({x},{y}) scale({s})">
  <rect x="-4" y="-6" width="86" height="13" rx="6" fill="#009fe3"/>
  <rect x="4"  y="6"  width="19" height="58" rx="9" fill="#009fe3"/>
  <rect x="29" y="6"  width="19" height="46" rx="9" fill="#fcc21b"/>
  <rect x="54" y="6"  width="19" height="34" rx="9" fill="#e1523d"/>
  <text x="96" y="52" font-family="DejaVu Sans" font-size="52" font-weight="bold" fill="#1f3b56">py</text>
  <text x="158" y="52" font-family="DejaVu Sans" font-size="52" fill="#6d97ad">test</text>
</g>'''

def python_badge(x, y, s=1.0):
    return f'''<g transform="translate({x},{y}) scale({s})">
  <rect x="0" y="0" width="196" height="62" rx="14" fill="#1f2937" stroke="#0f172380" stroke-width="4"/>
  <text x="22" y="43" font-family="DejaVu Sans Mono" font-size="30" font-weight="bold" fill="#4b8bbe">py</text>
  <text x="62" y="43" font-family="DejaVu Sans Mono" font-size="30" font-weight="bold" fill="#ffd43b">thon</text>
</g>'''

HEAD = ('<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">'
        f'<rect width="1200" height="630" fill="{BG}"/>'
        f'<path d="M 0 520 L 1200 520 L 1200 630 L 0 630 Z" fill="{BG_FLOOR}"/>'
        f'<path d="M 0 520 L 1200 520" stroke="#cdc2ab" stroke-width="4"/>')


def claude_badge(x, y, s=1.0):
    return f'''<g transform="translate({x},{y}) scale({s})">
  <rect x="0" y="0" width="252" height="62" rx="14" fill="#1f2937" stroke="#0f172380" stroke-width="4"/>
  <circle cx="34" cy="31" r="13" fill="#ff7a4d"/>
  <text x="60" y="43" font-family="DejaVu Sans" font-size="27" font-weight="bold" fill="#ffa176">claude code</text>
</g>'''
