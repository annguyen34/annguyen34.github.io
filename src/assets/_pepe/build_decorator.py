# -*- coding: utf-8 -*-
"""Cover cho bai python-decorator: ba tang hàm long nhau + pepe."""
import sys
sys.path.insert(0, '.')
from gen_pepe import *

BLUE, YELLOW, RED = "#0b6f9c", "#a17a06", "#c8433a"

# ---- ba tang long nhau ----
OX, OY, OW, OH = 90, 136, 610, 330          # tang 1: retry(config)
MX, MY, MW, MH = 114, 184, 562, 258         # tang 2: decorator(func)
IX, IY, IW, IH = 138, 228, 514, 190         # tang 3: wrapper(*args)
CX, CY, CW, CH = 162, 272, 466, 122         # ham goc

def layer(x, y, w, h, fill, stroke, num, label, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'''
  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}"
        stroke="{stroke}" stroke-width="5"{d}/>
  <circle cx="{x+30}" cy="{y+26}" r="17" fill="{stroke}"/>
  <text x="{x+30}" y="{y+35}" font-family="DejaVu Sans" font-size="22" font-weight="bold"
        fill="#fbfaf6" text-anchor="middle">{num}</text>
  <text x="{x+58}" y="{y+35}" font-family="DejaVu Sans Mono" font-size="24"
        fill="{stroke}">{label}</text>'''

cover = HEAD + f'''
  {python_badge(56, 44, 0.9)}

  <rect x="{OX+8}" y="{OY+12}" width="{OW}" height="{OH}" rx="14" fill="#00000018"/>
  {layer(OX, OY, OW, OH, "#fbfaf6", BLUE,   1, "retry(max_attempts=3, delay=2)")}
  {layer(MX, MY, MW, MH, "#f4eee0", YELLOW, 2, "decorator(func)")}
  {layer(IX, IY, IW, IH, "#efe6d2", RED,    3, "wrapper(*args, **kwargs)")}

  <!-- ham goc o trong cung -->
  <rect x="{CX}" y="{CY}" width="{CW}" height="{CH}" rx="12" fill="{SHIRT}" stroke="{SHIRT_D}" stroke-width="5"/>
  <text x="{CX+CW/2}" y="{CY+56}" font-family="DejaVu Sans Mono" font-size="31" font-weight="bold"
        fill="#fbfaf6" text-anchor="middle">fetch_order_status</text>
  <text x="{CX+CW/2}" y="{CY+94}" font-family="DejaVu Sans" font-size="21"
        fill="#cfe2f7" text-anchor="middle">logic thật, không bị sửa một dòng</text>

  <text x="{OX+4}" y="502" font-family="DejaVu Sans Mono" font-size="29"
        fill="#6b6257">@deco  ->  f = deco(f)</text>

  <!-- badge @ -->
  <circle cx="1006" cy="168" r="82" fill="{SHIRT}" stroke="{SHIRT_D}" stroke-width="6"/>
  <text x="1006" y="216" font-family="DejaVu Sans" font-size="124" font-weight="bold"
        fill="#fbfaf6" text-anchor="middle">@</text>

  <!-- mui tui tu badge @ tro ve hop ngoai cung -->
  <path d="M 920 202 C 852 246, 782 220, 722 194" fill="none" stroke="{SHIRT_D}"
        stroke-width="7" stroke-linecap="round"/>
  <path d="M 736 176 L 714 192 L 738 204 Z" fill="{SHIRT_D}"/>

  <!-- pepe: tro tay vao dong wrapper -->
  {pepe(962, 432, 1.16, "smug")}
  {arm("M 856 504 C 808 470, 764 440, 744 414", (738, 408, 28), 1.08)}
</svg>'''

open('cover-decorator.svg', 'w', encoding='utf-8').write(cover)
print("built cover-decorator.svg")
