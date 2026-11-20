import html
import os

OUTPUT_DIR = os.path.join("assets", "headers")
os.makedirs(OUTPUT_DIR, exist_ok=True)

SECTIONS = [
    ("sec-01-summary.svg",    "01", "EXECUTIVE SUMMARY",                      "#FFE600", "#00F0FF", "#B8FF00"),
    ("sec-02-focus.svg",      "02", "CURRENT FOCUS & ENGINEERING SCALE",      "#00F0FF", "#B8FF00", "#FF5E7E"),
    ("sec-03-tech.svg",       "03", "TECHNOLOGY ECOSYSTEM",                   "#B8FF00", "#FF5E7E", "#C084FC"),
    ("sec-04-projects.svg",   "04", "FLAGSHIP ARCHITECTURES & FEATURED WORK", "#FF5E7E", "#C084FC", "#FFE600"),
    ("sec-05-impact.svg",     "05", "IMPACT & ENGINEERING FOOTPRINT",         "#C084FC", "#FFE600", "#00F0FF"),
    ("sec-06-telemetry.svg",  "06", "LIVE GITHUB TELEMETRY & ANIMATIONS",     "#FFE600", "#FF5E7E", "#00F0FF"),
    ("sec-07-certs.svg",      "07", "VERIFIED CERTIFICATIONS & RECOGNITION",  "#00F0FF", "#C084FC", "#B8FF00"),
    ("sec-08-philosophy.svg", "08", "ENGINEERING PHILOSOPHY",                 "#B8FF00", "#FFE600", "#FF5E7E"),
    ("sec-09-connect.svg",    "09", "LET'S BUILD SOMETHING ICONIC",           "#FF5E7E", "#00F0FF", "#FFE600"),
]

SVG_TEMPLATE = """<svg viewBox="0 0 900 72" width="900" height="72" xmlns="http://www.w3.org/2000/svg">
  <style>
    @keyframes slabShift {{
      0%, 28%  {{ fill: {c1}; }}
      33%, 61% {{ fill: {c2}; }}
      66%, 94% {{ fill: {c3}; }}
      100%     {{ fill: {c1}; }}
    }}
    @keyframes scanBeam {{
      0%   {{ transform: translateX(-180px); }}
      100% {{ transform: translateX(800px); }}
    }}
    @keyframes barPulse {{
      0%, 100% {{ opacity: 0.25; }}
      50%      {{ opacity: 1; }}
    }}
    .idx-box {{ animation: slabShift 9s linear infinite; }}
    .scanner {{ animation: scanBeam 3.6s linear infinite; }}
    .b1      {{ animation: barPulse 1.5s ease-in-out infinite 0.0s; }}
    .b2      {{ animation: barPulse 1.5s ease-in-out infinite 0.3s; }}
    .b3      {{ animation: barPulse 1.5s ease-in-out infinite 0.6s; }}
    .mono    {{ font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; font-weight: 800; }}
    .heading {{ font-family: 'Space Grotesk', 'Arial Black', Impact, sans-serif; font-weight: 900; letter-spacing: 1.6px; }}
  </style>

  <!-- Hard Unblurred Neo-Brutalist Shadow -->
  <rect x="11" y="11" width="882" height="54" fill="#000000" />

  <!-- Obsidian Main Slab -->
  <rect x="4" y="4" width="882" height="54" fill="#0D0D0D" stroke="#000000" stroke-width="4" />

  <!-- Animated Color-Shifting Index Block -->
  <rect class="idx-box" x="4" y="4" width="96" height="54" stroke="#000000" stroke-width="4" />
  <text x="52" y="38" text-anchor="middle" class="mono" font-size="20" fill="#000000">[ {num} ]</text>

  <!-- Section Title -->
  <text x="122" y="38" class="heading" font-size="19.5" fill="#FFFFFF">{title}</text>

  <!-- Gliding Bottom Neon Scanner -->
  <clipPath id="scanClip">
    <rect x="102" y="51" width="782" height="5" />
  </clipPath>
  <g clip-path="url(#scanClip)">
    <rect class="scanner" x="102" y="52" width="160" height="4" fill="{c1}" />
  </g>

  <!-- Animated 3-Bar Right Telemetry Pulse -->
  <rect class="b1" x="820" y="16" width="12" height="28" fill="{c1}" />
  <rect class="b2" x="838" y="16" width="12" height="28" fill="{c2}" />
  <rect class="b3" x="856" y="16" width="12" height="28" fill="{c3}" />
</svg>
"""

for filename, num, title, c1, c2, c3 in SECTIONS:
    svg_content = SVG_TEMPLATE.format(
        num=num,
        title=html.escape(title),
        c1=c1,
        c2=c2,
        c3=c3,
    )
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated: {filepath}")
