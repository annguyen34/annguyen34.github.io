# -*- coding: utf-8 -*-
import sys, math
sys.path.insert(0, '.')
from gen_pepe import *

def octagon(cx, cy, r):
    pts = []
    for k in range(8):
        a = math.pi/8 + k*math.pi/4
        pts.append(f"{cx + r*math.cos(a):.1f},{cy + r*math.sin(a):.1f}")
    return " ".join(pts)

# ============ COVER: claude-code-hooks ============
FX, FY, FW, FH = 700, 118, 442, 272
c1 = HEAD + f'''
  {claude_badge(120, 84, 0.86)}

  <!-- file card .env bi chan -->
  <rect x="{FX+8}" y="{FY+12}" width="{FW}" height="{FH}" rx="12" fill="#00000018"/>
  <rect x="{FX}" y="{FY}" width="{FW}" height="{FH}" rx="12" fill="#fbfaf6" stroke="{LINE}" stroke-width="5"/>
  <path d="M {FX} {FY+52} L {FX+FW} {FY+52}" stroke="{LINE}" stroke-width="4.5"/>
  <circle cx="{FX+28}" cy="{FY+27}" r="7" fill="#c8433a"/>
  <circle cx="{FX+50}" cy="{FY+27}" r="7" fill="#e0a92e"/>
  <circle cx="{FX+72}" cy="{FY+27}" r="7" fill="#2f8f4e"/>
  <text x="{FX+FW/2}" y="{FY+35}" font-family="DejaVu Sans Mono" font-size="24"
        font-weight="bold" fill="#4a5566" text-anchor="middle">.env</text>

  <rect x="{FX+34}" y="{FY+86}" width="250" height="15" rx="7" fill="#cfd5dc"/>
  <rect x="{FX+34}" y="{FY+120}" width="330" height="15" rx="7" fill="#cfd5dc"/>
  <rect x="{FX+34}" y="{FY+154}" width="196" height="15" rx="7" fill="#cfd5dc"/>
  <rect x="{FX+34}" y="{FY+188}" width="286" height="15" rx="7" fill="#cfd5dc"/>

  <!-- dau X do de len file -->
  <g stroke="#c8433a" stroke-width="17" stroke-linecap="round" opacity="0.9">
    <path d="M {FX+62} {FY+82} L {FX+FW-62} {FY+206}"/>
    <path d="M {FX+FW-62} {FY+82} L {FX+62} {FY+206}"/>
  </g>

  <!-- pill: exit code 2 -->
  <rect x="{FX+72}" y="{FY+FH+24}" width="298" height="52" rx="26"
        fill="#c8433a" stroke="{LINE}" stroke-width="4.5"/>
  <text x="{FX+FW/2}" y="{FY+FH+59}" font-family="DejaVu Sans Mono" font-size="25"
        font-weight="bold" fill="#fbfaf6" text-anchor="middle">blocked · exit 2</text>

  <!-- pepe gatekeeper: tay gio bien STOP -->
  {pepe(296, 386, 1.42, "smug")}
  {arm("M 462 512 C 512 496, 556 452, 574 424", (582, 414, 34), 1.25)}
  <g>
    <polygon points="{octagon(604, 372, 62)}" fill="#c8433a" stroke="#fbfaf6" stroke-width="7"/>
    <polygon points="{octagon(604, 372, 62)}" fill="none" stroke="{LINE}" stroke-width="4.5"/>
    <text x="604" y="384" font-family="DejaVu Sans" font-size="30" font-weight="bold"
          fill="#fbfaf6" text-anchor="middle">STOP</text>
  </g>

  <!-- chip PreToolUse canh pepe -->
  <rect x="120" y="172" width="216" height="48" rx="12" fill="#1f2937" stroke="#0f172380" stroke-width="4"/>
  <text x="228" y="205" font-family="DejaVu Sans Mono" font-size="22" fill="#ffa176" text-anchor="middle">PreToolUse</text>
</svg>'''

# ============ COVER: use-claude-code-like-a-pro ============
BX, BY, BW, BH = 690, 108, 452, 292
c2 = HEAD + f'''
  {claude_badge(120, 84, 0.86)}

  <!-- board: context gauge -->
  <rect x="{BX+8}" y="{BY+12}" width="{BW}" height="{BH}" rx="12" fill="#00000018"/>
  <rect x="{BX}" y="{BY}" width="{BW}" height="{BH}" rx="12" fill="#fbfaf6" stroke="{LINE}" stroke-width="5"/>

  <text x="{BX+34}" y="{BY+52}" font-family="DejaVu Sans" font-size="24" fill="#8a8175">context còn lại</text>
  <rect x="{BX+34}" y="{BY+72}" width="{BW-68}" height="34" rx="17" fill="#e6e1d6" stroke="{LINE}" stroke-width="4"/>
  <rect x="{BX+34}" y="{BY+72}" width="{(BW-68)*0.42:.0f}" height="34" rx="17" fill="#ff7a4d" stroke="{LINE}" stroke-width="4"/>
  <text x="{BX+BW-34}" y="{BY+138}" font-family="DejaVu Sans Mono" font-size="26"
        font-weight="bold" fill="#c86a3a" text-anchor="end">42%</text>

  <rect x="{BX+34}" y="{BY+164}" width="150" height="46" rx="12" fill="#1f2937"/>
  <text x="{BX+109}" y="{BY+195}" font-family="DejaVu Sans Mono" font-size="22" fill="#ffa176" text-anchor="middle">/compact</text>
  <rect x="{BX+198}" y="{BY+164}" width="184" height="46" rx="12" fill="#1f2937"/>
  <text x="{BX+290}" y="{BY+195}" font-family="DejaVu Sans Mono" font-size="22" fill="#ffa176" text-anchor="middle">plan mode</text>

  <rect x="{BX+34}" y="{BY+228}" width="348" height="46" rx="12" fill="#2f8f4e" stroke="{LINE}" stroke-width="4"/>
  <text x="{BX+208}" y="{BY+259}" font-family="DejaVu Sans Mono" font-size="22"
        font-weight="bold" fill="#fbfaf6" text-anchor="middle">✓ 18 tests passed</text>

  <!-- pepe pro: kinh ram + ly ca phe -->
  {pepe(300, 386, 1.42, "smug", accessory="glasses")}
  {arm("M 466 512 C 514 500, 552 468, 568 444", (576, 436, 34), 1.25)}
  <g transform="translate(600,424)">
    <path d="M 30 -12 C 54 -12, 54 22, 30 22" fill="none" stroke="{LINE}" stroke-width="8"/>
    <rect x="-30" y="-26" width="62" height="62" rx="9" fill="#fbfaf6" stroke="{LINE}" stroke-width="5"/>
    <rect x="-30" y="-26" width="62" height="16" rx="7" fill="#8a5a3c" stroke="{LINE}" stroke-width="4"/>
    <path d="M -12 -44 C -4 -56, -18 -64, -10 -76" fill="none" stroke="#b9b2a3" stroke-width="5" stroke-linecap="round"/>
    <path d="M 12 -44 C 20 -56, 6 -64, 14 -76" fill="none" stroke="#b9b2a3" stroke-width="5" stroke-linecap="round"/>
  </g>
</svg>'''

open('cover-hooks.svg','w',encoding='utf-8').write(c1)
open('cover-pro.svg','w',encoding='utf-8').write(c2)
print("2 svg written")
