# -*- coding: utf-8 -*-
"""Cover cho 2 bai series Fluent Python (index + chapter 1 - Data Model)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_pepe import *

SANS = "DejaVu Sans, Helvetica, Arial, sans-serif"
MONO = "DejaVu Sans Mono, Menlo, Monaco, monospace"

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))

def txt(x, y, s, size, fill, family=SANS, weight="normal", anchor="start"):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>')

def card(x, y, w, h, rank, suit):
    """La bai phang, nam doc. suit: spade (den) | heart (do)"""
    col = "#c8433a" if suit == "heart" else "#1b1b1b"
    suit_path = (
        "M 0 -6 C -3 -16, -20 -22, -20 -32 C -20 -42, -8 -46, 0 -36 "
        "C 8 -46, 20 -42, 20 -32 C 20 -22, 3 -16, 0 -6 Z"
        "M 0 -6 L -7 4 L 7 4 Z" if suit == "spade" else
        "M 0 -40 C -14 -58, -30 -40, 0 -12 C 30 -40, 14 -58, 0 -40 Z"
        "M 0 -16 L -8 -4 L 8 -4 Z")
    return f'''<g transform="translate({x},{y})">
  <rect x="6" y="8" width="{w}" height="{h}" rx="11" fill="#00000018"/>
  <rect x="0" y="0" width="{w}" height="{h}" rx="11" fill="#fbfaf6" stroke="{LINE}" stroke-width="5"/>
  {txt(14, 34, rank, 27, col, MONO, "bold")}
  <g transform="translate({w/2},{h/2+14}) scale(0.62)">
    <path d="{suit_path}" fill="{col}" stroke="{LINE}" stroke-width="4"/>
  </g>
</g>'''

def no_ai_badge(x, y, s=1.0):
    """Badge 'no AI' co gach che."""
    return f'''<g transform="translate({x},{y}) scale({s})">
  <rect x="0" y="0" width="176" height="58" rx="14" fill="#1f2937"/>
  {txt(24, 40, "no AI", 30, "#fbfaf6", SANS, "bold")}
  <circle cx="146" cy="29" r="19" fill="none" stroke="#c8433a" stroke-width="6"/>
  <path d="M 133 16 L 159 42" stroke="#c8433a" stroke-width="6" stroke-linecap="round"/>
</g>'''

# =====================================================================
# COVER 1: fluent-python-ch00-index  (doc sach, 5 phan, no AI)
# =====================================================================
LX, RX, TY = 150, 790, 176          # trang trai/phai, dinh
SPINE_L, SPINE_R = 452, 488         # chan sach
BY = 452                            # day trang

c1 = HEAD + f'''
  {python_badge(56, 44, 0.9)}

  <!-- bia sach duoi trang -->
  <path d="M {LX-18} {TY+18} C {LX+80} {TY-12}, {SPINE_L-20} {TY-6}, {SPINE_L} {TY+8}
           L {SPINE_R} {TY+8} C {SPINE_R+20} {TY-6}, {RX-80} {TY-12}, {RX+18} {TY+18}
           L {RX+18} {BY+22} C {RX-80} {BY+52}, {SPINE_R+20} {BY+46}, {SPINE_R} {BY+32}
           L {SPINE_L} {BY+32} C {SPINE_L-20} {BY+46}, {LX-80} {BY+52}, {LX-18} {BY+22} Z"
        fill="#c8433a" stroke="#8f2f28" stroke-width="5.5"/>

  <!-- trang trai -->
  <path d="M {LX} {TY+8} C {LX+90} {TY-16}, {SPINE_L-30} {TY-8}, {SPINE_L} {TY+14}
           L {SPINE_L} {BY+8} C {SPINE_L-30} {BY-14}, {LX+90} {BY-6}, {LX} {BY+18} Z"
        fill="#fbfaf6" stroke="{LINE}" stroke-width="5"/>
  {txt(232, 268, "Fluent", 54, "#1f3b56", SANS, "bold")}
  {txt(232, 322, "Python", 54, "#c8433a", SANS, "bold")}
  {txt(234, 362, "Luciano Ramalho", 21, "#8a8175")}
  {txt(234, 392, "O'Reilly 2022 · 2e", 21, "#8a8175")}

  <!-- trang phai: 5 phan -->
  <path d="M {RX} {TY+8} C {RX-90} {TY-16}, {SPINE_R+30} {TY-8}, {SPINE_R} {TY+14}
           L {SPINE_R} {BY+8} C {SPINE_R+30} {BY-14}, {RX-90} {BY-6}, {RX} {BY+18} Z"
        fill="#fbfaf6" stroke="{LINE}" stroke-width="5"/>
  {txt(530, 240, "24 chương · 5 phần", 23, "#8a8175")}
  {txt(530, 284, "I", 26, "#0b6f9c", MONO, "bold")}
  {txt(586, 284, "Data structures", 22, "#1f3b56")}
  {txt(530, 320, "II", 26, "#a17a06", MONO, "bold")}
  {txt(586, 320, "Functions", 22, "#1f3b56")}
  {txt(530, 356, "III", 26, "#c8433a", MONO, "bold")}
  {txt(586, 356, "Class &amp; protocol", 22, "#1f3b56")}
  {txt(530, 392, "IV", 26, "#2f8f4e", MONO, "bold")}
  {txt(586, 392, "Async", 22, "#1f3b56")}
  {txt(530, 428, "V", 26, "#7a5aa0", MONO, "bold")}
  {txt(586, 428, "Metaprogramming", 22, "#1f3b56")}

  {no_ai_badge(962, 74, 1.0)}

  <!-- pepe dang doc sach, tay tro vao goc phai cua sach -->
  {pepe(1040, 474, 1.1, "smug")}
  {arm("M 934 552 C 890 526, 848 488, 822 462", (816, 456, 26), 1.0)}
</svg>'''

with open(os.path.join(OUT_DIR, "cover-fluent-python.svg"), "w", encoding="utf-8") as f:
    f.write(c1)

# =====================================================================
# COVER 2: fluent-python-ch01-data-model (len(x) vs x.len(), la bai)
# =====================================================================
WX, WY, WW, WH = 96, 132, 636, 288    # whiteboard

def row(y, num, left, right, eq, eq_col):
    return f'''
  <circle cx="{WX+30}" cy="{y-8}" r="17" fill="#1f3b56"/>
  {txt(WX+30, y, num, 21, "#fbfaf6", SANS, "bold", "middle")}
  {txt(WX+60, y, left, 25, "#0b6f9c", MONO, "bold")}
  {txt(WX+318, y, "->", 25, "#8a8175", MONO)}
  {txt(WX+376, y, right, 25, "#a17a06", MONO, "bold")}
  {txt(WX+WW-24, y, eq, 25, eq_col, MONO, "bold", "end")}'''

c2 = HEAD + f'''
  {python_badge(56, 44, 0.9)}

  <!-- whiteboard -->
  <rect x="{WX+8}" y="{WY+10}" width="{WW}" height="{WH}" rx="10" fill="#00000018"/>
  <rect x="{WX}" y="{WY}" width="{WW}" height="{WH}" rx="10" fill="#fbfaf6" stroke="{LINE}" stroke-width="5"/>
  <rect x="{WX+WW/2-90}" y="{WY+WH}" width="180" height="13" rx="6" fill="#cdc2ab" stroke="{LINE}" stroke-width="4"/>
  {txt(WX+30, WY+46, "Python Data Model · dunder = contract", 21, "#8a8175")}

  {row(WY+112, "1", "len(deck)", "__len__()", "52", "#2f8f4e")}
  {row(WY+188, "2", "deck[0]", "__getitem__(0)", "A", "#2f8f4e")}
  {row(WY+252, "3", "for c in deck", "__getitem__()", "+1", "#c8433a")}

  {txt(WX+4, 502, "special method = interpreter tự gọi", 23, "#6b6257", MONO)}

  <!-- la bai bay ra tu deck -->
  {card(786, 96, 96, 136, "A", "spade")}
  {card(906, 118, 96, 136, "Q", "heart")}

  <!-- pepe tay tro vao whiteboard, tay kia giu la bai -->
  {pepe(1000, 470, 1.14, "smug")}
  {arm("M 894 548 C 836 522, 796 496, 772 476", (766, 470, 27), 1.02)}
  {arm("M 1112 552 C 1156 528, 1170 490, 1152 452", (1150, 444, 26), 0.98)}
  {card(1112, 318, 84, 120, "K", "spade")}
</svg>'''

with open(os.path.join(OUT_DIR, "cover-fluent-python-data-model.svg"), "w", encoding="utf-8") as f:
    f.write(c2)

print("built cover-fluent-python.svg + cover-fluent-python-data-model.svg")
