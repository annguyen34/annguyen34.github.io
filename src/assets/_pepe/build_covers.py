# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '.')
from gen_pepe import *

# ================= COVER 1: pytest-optimize =================
WX, WY, WW, WH = 646, 84, 500, 300
bars = "".join(
    f'<rect x="{WX+40+i*52}" y="{WY+220}" width="40" height="16" rx="8" fill="#2f8f4e" opacity="0.88"/>'
    for i in range(8))

c1 = HEAD + f'''
  <!-- whiteboard -->
  <rect x="{WX+8}" y="{WY+10}" width="{WW}" height="{WH}" rx="10" fill="#00000018"/>
  <rect x="{WX}" y="{WY}" width="{WW}" height="{WH}" rx="10" fill="#fbfaf6" stroke="{LINE}" stroke-width="5"/>
  <rect x="{WX+160}" y="{WY+WH}" width="180" height="13" rx="6" fill="#cdc2ab" stroke="{LINE}" stroke-width="4"/>

  <text x="{WX+34}" y="{WY+58}" font-family="DejaVu Sans" font-size="21" fill="#8a8175">runtime / suite</text>

  <text x="{WX+30}" y="{WY+142}" font-family="DejaVu Sans" font-size="60" font-weight="bold" fill="#c8433a">20:34</text>
  <path d="M {WX+22} {WY+122} L {WX+206} {WY+118}" stroke="#c8433a" stroke-width="7" stroke-linecap="round"/>

  <path d="M {WX+222} {WY+122} L {WX+256} {WY+122}" stroke="#2f8f4e" stroke-width="7" stroke-linecap="round"/>
  <path d="M {WX+248} {WY+110} L {WX+266} {WY+122} L {WX+248} {WY+134} Z" fill="#2f8f4e"/>

  <text x="{WX+290}" y="{WY+142}" font-family="DejaVu Sans" font-size="60" font-weight="bold" fill="#2f8f4e">1:58</text>
  <ellipse cx="{WX+366}" cy="{WY+120}" rx="82" ry="38" fill="none" stroke="#2f8f4e"
           stroke-width="6" transform="rotate(-4 {WX+366} {WY+120})"/>

  <text x="{WX+34}" y="{WY+208}" font-family="DejaVu Sans" font-size="20" fill="#8a8175">8 workers</text>
  {bars}

  {pytest_logo(132, 108, 0.86)}

  <!-- pepe: tay ra NGOAI than, khong cat mat -->
  {pepe(300, 380, 1.42, "smug")}
  {arm("M 466 506 C 512 492, 556 458, 574 436", (580, 428, 34), 1.25)}

  <!-- stopwatch trong tay -->
  <g transform="translate(596,414)">
    <rect x="-11" y="-64" width="22" height="18" rx="6" fill="#9aa2a8" stroke="{LINE}" stroke-width="4"/>
    <circle cx="0" cy="0" r="46" fill="#d9dee1" stroke="{LINE}" stroke-width="5.5"/>
    <circle cx="0" cy="0" r="35" fill="#fbfaf6" stroke="{LINE}" stroke-width="4"/>
    <path d="M 0 0 L 21 -23" stroke="#c8433a" stroke-width="6" stroke-linecap="round"/>
    <circle cx="0" cy="0" r="5" fill="{LINE}"/>
  </g>

  {sweat(238, 262, 1.05)}
  {sweat(492, 300, 0.85)}
</svg>'''

# ================= COVER 2: python-immutable-mutable =================
# box o TREN GIUA, hai pepe hai ben duoi -> khong chong lan
BX, BY, BW, BH = 452, 92, 300, 148

def tag(x, y, label):
    return (f'<rect x="{x-36}" y="{y}" width="72" height="48" rx="12" fill="#fbfaf6" '
            f'stroke="{LINE}" stroke-width="4.5"/>'
            f'<text x="{x}" y="{y+34}" font-family="DejaVu Sans Mono" font-size="31" '
            f'font-weight="bold" fill="#1f3b56" text-anchor="middle">{label}</text>')

c2 = HEAD + f'''
  {python_badge(56, 44, 0.9)}

  <!-- box: MOT object duy nhat -->
  <rect x="{BX+8}" y="{BY+12}" width="{BW}" height="{BH}" rx="10" fill="#00000018"/>
  <rect x="{BX}" y="{BY}" width="{BW}" height="{BH}" rx="10" fill="#cda06d" stroke="#6b4f2e" stroke-width="5.5"/>
  <path d="M {BX} {BY+40} L {BX+BW} {BY+40}" stroke="#6b4f2e" stroke-width="4.5"/>
  <path d="M {BX+BW/2} {BY} L {BX+BW/2} {BY+40}" stroke="#6b4f2e" stroke-width="4.5"/>
  <rect x="{BX+26}" y="{BY+64}" width="{BW-52}" height="56" rx="10" fill="#fbfaf6" stroke="#6b4f2e" stroke-width="4"/>
  <text x="{BX+BW/2}" y="{BY+102}" font-family="DejaVu Sans Mono" font-size="34"
        font-weight="bold" fill="#1f3b56" text-anchor="middle">[1, 2, 99]</text>

  <text x="600" y="474" font-family="DejaVu Sans" font-size="27"
        fill="#6b6257" text-anchor="middle">một object duy nhất</text>

  <!-- day: hai tay cung tro ve MOT box -->
  <path d="M 402 356 C 420 320, 436 276, {BX+18} {BY+BH+14}" fill="none"
        stroke="#7a6647" stroke-width="7" stroke-linecap="round"/>
  <path d="M 802 356 C 784 320, 768 276, {BX+BW-18} {BY+BH+14}" fill="none"
        stroke="#7a6647" stroke-width="7" stroke-linecap="round"/>

  <!-- pepe a -->
  {pepe(228, 476, 1.14, "sad")}
  {arm("M 342 556 C 378 520, 396 400, 400 366", (400, 356, 27), 1.0)}
  {tag(228, 568, "a")}

  <!-- pepe b: soc -->
  {pepe(976, 476, 1.14, "shock")}
  {arm("M 862 556 C 826 520, 808 400, 804 366", (804, 356, 27), 1.0)}
  {tag(976, 568, "b")}

  <!-- dau ! canh dau pepe b -->
  <g transform="translate(1092,284)">
    <path d="M 0 0 L 8 44 L -8 44 Z" fill="#c8433a" stroke="{LINE}" stroke-width="3.5"/>
    <circle cx="0" cy="60" r="8" fill="#c8433a" stroke="{LINE}" stroke-width="3.5"/>
  </g>
</svg>'''

open('cover-pytest.svg','w',encoding='utf-8').write(c1)
open('cover-python.svg','w',encoding='utf-8').write(c2)
print("rebuilt")
