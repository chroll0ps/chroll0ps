import html
import os
import xml.etree.ElementTree as ET

os.makedirs(os.path.join("assets", "headers"), exist_ok=True)

FILES = {}

# 1. HERO BANNER
FILES["assets/brutal-hero.svg"] = """<?xml version="1.0" encoding="UTF-8"?>
<svg viewBox="0 0 900 265" width="900" height="265" xmlns="[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)">
  <defs>
    <pattern id="brutalGrid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#E5E5E5" stroke-width="1.2"/>
    </pattern>
  </defs>
  <style><![CDATA[
    @keyframes barColorShift {
      0%, 22%   { fill: #FFE600; }
      25%, 47%  { fill: #00F0FF; }
      50%, 72%  { fill: #B8FF00; }
      75%, 97%  { fill: #FF5E7E; }
      100%      { fill: #FFE600; }
    }
    @keyframes accentShift {
      0%, 22%   { fill: #FF5E7E; }
      25%, 47%  { fill: #FFE600; }
      50%, 72%  { fill: #C084FC; }
      75%, 97%  { fill: #00F0FF; }
      100%      { fill: #FF5E7E; }
    }
    @keyframes blinkLed {
      0%, 49%   { opacity: 1; }
      50%, 100% { opacity: 0.15; }
    }
    @keyframes spinSlow {
      from { transform: rotate(0deg); }
      to   { transform: rotate(360deg); }
    }
    .topbar       { animation: barColorShift 10s linear infinite; }
    .accent-block { animation: accentShift 10s linear infinite; }
    .led          { animation: blinkLed 1.4s steps(1) infinite; }
    .spinner      { transform-origin: 792px 150px; animation: spinSlow 14s linear infinite; }
    .title        { font-family: 'Space Grotesk', 'Arial Black', Impact, sans-serif; font-weight: 900; letter-spacing: 3px; }
    .mono         { font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; font-weight: 800; }
  ]]></style>

  <rect x="16" y="16" width="874" height="238" fill="#000000" />
  <rect x="6" y="6" width="874" height="238" fill="#FFFDF5" stroke="#000000" stroke-width="4" />
  <rect x="8" y="48" width="870" height="194" fill="url(#brutalGrid)" />

  <rect class="topbar" x="6" y="6" width="874" height="42" stroke="#000000" stroke-width="4" />

  <rect x="24" y="18" width="16" height="16" fill="#FF5E7E" stroke="#000000" stroke-width="3" />
  <rect x="48" y="18" width="16" height="16" fill="#FFFFFF" stroke="#000000" stroke-width="3" />
  <rect x="72" y="18" width="16" height="16" fill="#000000" stroke="#000000" stroke-width="3" />

  <text x="108" y="32" class="mono" font-size="13" fill="#000000" letter-spacing="1.5">SYS://CHROLL0PS // FLAGSHIP_ARCHITECTURE_NODE</text>

  <rect x="706" y="14" width="156" height="25" fill="#0D0D0D" stroke="#000000" stroke-width="2" />
  <circle class="led" cx="722" cy="26.5" r="5" fill="#B8FF00" />
  <text x="736" y="31" class="mono" font-size="11.5" fill="#FFFFFF" letter-spacing="1">ONLINE // ACTIVE</text>

  <text x="48" y="144" class="title accent-block" font-size="78">ANAS</text>
  <text x="42" y="138" class="title" font-size="78" fill="#000000">ANAS</text>

  <rect x="336" y="96" width="142" height="32" fill="#000000" />
  <rect x="332" y="92" width="142" height="32" fill="#00F0FF" stroke="#000000" stroke-width="3" />
  <text x="403" y="113" text-anchor="middle" class="mono" font-size="13.5" fill="#000000">@CHROLL0PS</text>

  <rect x="48" y="168" width="560" height="42" fill="#000000" />
  <rect x="42" y="162" width="560" height="42" fill="#0D0D0D" stroke="#000000" stroke-width="3" />
  <text x="58" y="189" class="mono" font-size="15.5" fill="#FFE600" letter-spacing="1">AI &amp; DATA SYSTEMS ARCHITECT // FULL-STACK ENGINEER</text>

  <g class="spinner">
    <polygon points="792,92 806,132 848,128 816,154 834,192 792,172 750,192 768,154 736,128 778,132"
             fill="#FFE600" stroke="#000000" stroke-width="4" stroke-linejoin="miter" />
  </g>
  <circle cx="792" cy="150" r="18" fill="#000000" />
  <text x="792" y="155" text-anchor="middle" class="mono" font-size="12" fill="#B8FF00">AI</text>
</svg>
"""

# 2. INFINITE MARQUEE TICKER
FILES["assets/brutal-marquee.svg"] = """<?xml version="1.0" encoding="UTF-8"?>
<svg viewBox="0 0 900 46" width="900" height="46" xmlns="[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)">
  <defs>
    <clipPath id="tickerClip">
      <rect x="6" y="4" width="888" height="38" />
    </clipPath>
  </defs>
  <style><![CDATA[
    @keyframes scrollTicker {
      0%   { transform: translateX(0px); }
      100% { transform: translateX(-1380px); }
    }
    .track { animation: scrollTicker 18s linear infinite; }
    .ticker-text {
      font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
      font-size: 13.5px;
      font-weight: 800;
      fill: #FFFFFF;
      letter-spacing: 1.5px;
    }
  ]]></style>

  <rect x="2" y="2" width="896" height="42" fill="#0D0D0D" stroke="#000000" stroke-width="4" />

  <g clip-path="url(#tickerClip)">
    <g class="track">
      <text x="0" y="28" textLength="1360" lengthAdjust="spacing" class="ticker-text">
        <tspan fill="#FFE600">&#x2726;</tspan> MEDALLION LAKEHOUSE  <tspan fill="#00F0FF">&#x2726;</tspan> KAFKA &amp; SPARK STREAMING  <tspan fill="#B8FF00">&#x2726;</tspan> DATABRICKS GENAI  <tspan fill="#FF5E7E">&#x2726;</tspan> OCI &amp; AWS CLOUD  <tspan fill="#C084FC">&#x2726;</tspan> PRODUCTION RAG &amp; SQL  <tspan fill="#FFE600">&#x2726;</tspan> TYPESCRIPT COMPILERS
      </text>
      <text x="1380" y="28" textLength="1360" lengthAdjust="spacing" class="ticker-text">
        <tspan fill="#FFE600">&#x2726;</tspan> MEDALLION LAKEHOUSE  <tspan fill="#00F0FF">&#x2726;</tspan> KAFKA &amp; SPARK STREAMING  <tspan fill="#B8FF00">&#x2726;</tspan> DATABRICKS GENAI  <tspan fill="#FF5E7E">&#x2726;</tspan> OCI &amp; AWS CLOUD  <tspan fill="#C084FC">&#x2726;</tspan> PRODUCTION RAG &amp; SQL  <tspan fill="#FFE600">&#x2726;</tspan> TYPESCRIPT COMPILERS
      </text>
    </g>
  </g>
</svg>
"""

# 3. LIVE COLOR-SHIFTING MANIFESTO SLAB
FILES["assets/brutal-manifesto.svg"] = """<?xml version="1.0" encoding="UTF-8"?>
<svg viewBox="0 0 900 205" width="900" height="205" xmlns="[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)">
  <style><![CDATA[
    @keyframes slabColorShift {
      0%, 17%  { fill: #FFE600; }
      20%, 37% { fill: #00F0FF; }
      40%, 57% { fill: #B8FF00; }
      60%, 77% { fill: #FF5E7E; }
      80%, 97% { fill: #C084FC; }
      100%     { fill: #FFE600; }
    }
    @keyframes badgeColorShift {
      0%, 17%  { fill: #FF5E7E; }
      20%, 37% { fill: #FFE600; }
      40%, 57% { fill: #00F0FF; }
      60%, 77% { fill: #B8FF00; }
      80%, 97% { fill: #FFE600; }
      100%     { fill: #FF5E7E; }
    }
    .shifting-bg     { animation: slabColorShift 12s ease-in-out infinite; }
    .shifting-accent { animation: badgeColorShift 12s ease-in-out infinite; }
    .mono            { font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; font-weight: 800; }
    .quote           { font-family: 'Space Grotesk', 'Arial Black', Helvetica, Arial, sans-serif; font-weight: 900; }
  ]]></style>

  <rect x="16" y="16" width="874" height="178" fill="#000000" />
  <rect class="shifting-bg" x="6" y="6" width="874" height="178" stroke="#000000" stroke-width="4" />

  <rect x="30" y="24" width="224" height="28" fill="#000000" />
  <text x="44" y="43" class="mono" font-size="12" fill="#FFFFFF" letter-spacing="2">MANIFESTO // 001</text>

  <rect class="shifting-accent" x="826" y="24" width="28" height="28" stroke="#000000" stroke-width="3" />

  <text x="443" y="96" text-anchor="middle" class="quote" font-size="22" fill="#000000" letter-spacing="0.4">
    &#x201C;GOOD ARCHITECTURE MAKES THE HARD THINGS POSSIBLE;
  </text>
  <text x="443" y="128" text-anchor="middle" class="quote" font-size="22" fill="#000000" letter-spacing="0.4">
    GREAT ARCHITECTURE MAKES THE RIGHT THINGS INEVITABLE.&#x201D;
  </text>

  <rect x="572" y="148" width="286" height="26" fill="#000000" />
  <rect x="568" y="144" width="286" height="26" fill="#FFFFFF" stroke="#000000" stroke-width="3" />
  <text x="711" y="162" text-anchor="middle" class="mono" font-size="12" fill="#000000" letter-spacing="1.2">&#x2014; ANAS &#x00B7; AI &amp; DATA SYSTEMS</text>
</svg>
"""

# 4. DUAL-PANE ANIMATED FLAGSHIP TERMINAL (SVG 1.1 SAFE)
FILES["assets/brutal-terminal.svg"] = """<?xml version="1.0" encoding="UTF-8"?>
<svg viewBox="0 0 900 415" width="900" height="415" xmlns="[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)">
  <defs>
    <pattern id="termGrid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#181818" stroke-width="1"/>
    </pattern>
    <clipPath id="leftClip">
      <rect x="8" y="48" width="582" height="347" />
    </clipPath>
  </defs>
  <style><![CDATA[
    @keyframes titleBarShift {
      0%, 23%  { fill: #FFE600; }
      25%, 48% { fill: #00F0FF; }
      50%, 73% { fill: #B8FF00; }
      75%, 98% { fill: #FF5E7E; }
      100%     { fill: #FFE600; }
    }
    @keyframes bootIn {
      0%   { opacity: 0; transform: translateY(4px); }
      100% { opacity: 1; transform: translateY(0px); }
    }
    @keyframes blinkBlock {
      0%, 49%   { opacity: 1; }
      50%, 100% { opacity: 0; }
    }
    @keyframes scanSweep {
      0%   { transform: translateY(0px); opacity: 0.14; }
      50%  { opacity: 0.25; }
      100% { transform: translateY(345px); opacity: 0.05; }
    }
    @keyframes barGrow {
      0%   { transform: scaleX(0); }
      100% { transform: scaleX(1); }
    }
    @keyframes eqBounce1 { 0%, 100% { transform: scaleY(0.35); } 50% { transform: scaleY(1); } }
    @keyframes eqBounce2 { 0%, 100% { transform: scaleY(0.85); } 50% { transform: scaleY(0.25); } }
    @keyframes eqBounce3 { 0%, 100% { transform: scaleY(0.5); }  50% { transform: scaleY(0.95); } }

    .topbar  { animation: titleBarShift 12s linear infinite; }
    .cursor  { animation: blinkBlock 1s steps(1) infinite; }
    .led     { animation: blinkBlock 1.4s steps(1) infinite; }
    .scanner { animation: scanSweep 5.5s linear infinite; }

    .b-step-1 { opacity: 0; animation: bootIn 0.25s ease-out forwards 0.15s; }
    .b-step-2 { opacity: 0; animation: bootIn 0.30s ease-out forwards 0.45s; }
    .b-step-3 { opacity: 0; animation: bootIn 0.25s ease-out forwards 0.85s; }
    .b-step-4 { opacity: 0; animation: bootIn 0.25s ease-out forwards 1.15s; }
    .b-step-5 { opacity: 0; animation: bootIn 0.25s ease-out forwards 1.45s; }
    .b-step-6 { opacity: 0; animation: bootIn 0.25s ease-out forwards 1.75s; }
    .b-step-7 { opacity: 0; animation: bootIn 0.25s ease-out forwards 2.05s; }
    .b-step-8 { opacity: 0; animation: bootIn 0.25s ease-out forwards 2.35s; }
    .b-step-9 { opacity: 0; animation: bootIn 0.25s ease-out forwards 2.65s; }

    .bar-fill {
      transform-box: fill-box;
      transform-origin: left center;
      animation: barGrow 1.2s cubic-bezier(0.22, 1, 0.36, 1) forwards;
    }

    .eq  { transform-box: fill-box; transform-origin: bottom center; }
    .eq1 { animation: eqBounce1 1.1s ease-in-out infinite 0.0s; }
    .eq2 { animation: eqBounce2 0.9s ease-in-out infinite 0.15s; }
    .eq3 { animation: eqBounce3 1.3s ease-in-out infinite 0.3s; }
    .eq4 { animation: eqBounce1 0.85s ease-in-out infinite 0.45s; }
    .eq5 { animation: eqBounce2 1.2s ease-in-out infinite 0.2s; }
    .eq6 { animation: eqBounce3 1.0s ease-in-out infinite 0.5s; }
    .eq7 { animation: eqBounce1 0.95s ease-in-out infinite 0.1s; }
    .eq8 { animation: eqBounce2 1.15s ease-in-out infinite 0.35s; }

    .mono { font-family: 'JetBrains Mono', 'Fira Code', Consolas, 'Courier New', monospace; }
    .bold { font-weight: 800; }
  ]]></style>

  <rect x="14" y="14" width="876" height="391" fill="#000000" />
  <rect x="6" y="6" width="876" height="391" fill="#0D0D0D" stroke="#000000" stroke-width="4" />
  <rect x="8" y="46" width="872" height="349" fill="url(#termGrid)" />

  <rect class="topbar" x="6" y="6" width="876" height="40" stroke="#000000" stroke-width="4" />

  <rect x="22" y="17" width="16" height="16" fill="#FF5E7E" stroke="#000000" stroke-width="3" />
  <rect x="44" y="17" width="16" height="16" fill="#FFFFFF" stroke="#000000" stroke-width="3" />
  <rect x="66" y="17" width="16" height="16" fill="#000000" stroke="#000000" stroke-width="3" />

  <text x="98" y="31" class="mono bold" font-size="13" fill="#000000" letter-spacing="1.2">TERM://CHROLL0PS_OS v4.2 &#x2014; ./boot_flagship.sh --mode=architect</text>

  <rect x="748" y="13" width="120" height="24" fill="#0D0D0D" stroke="#000000" stroke-width="2" />
  <circle class="led" cx="764" cy="25" r="4.5" fill="#B8FF00" />
  <text x="776" y="29" class="mono bold" font-size="11" fill="#FFFFFF" letter-spacing="1">SYS // LIVE</text>

  <line x1="592" y1="46" x2="592" y2="397" stroke="#000000" stroke-width="4" />
  <line x1="594" y1="46" x2="594" y2="397" stroke="#2A2A2A" stroke-width="1" />

  <g clip-path="url(#leftClip)">
    <rect class="scanner" x="8" y="48" width="582" height="3" fill="#00F0FF" />
  </g>

  <g class="b-step-1">
    <text x="24" y="72" class="mono bold" font-size="12.5">
      <tspan fill="#B8FF00">root@chroll0ps:~#</tspan>
      <tspan fill="#FFFFFF"> ./whoami --flagship</tspan>
    </text>
  </g>

  <g class="b-step-2">
    <rect x="28" y="88" width="546" height="82" fill="#000000" />
    <rect x="24" y="84" width="546" height="82" fill="#141414" stroke="#FFE600" stroke-width="2.5" />
    <rect x="24" y="84" width="8" height="82" fill="#FFE600" />
    <text x="44" y="106" class="mono" font-size="12.5">
      <tspan fill="#FFE600" class="bold">IDENTITY  :</tspan>
      <tspan fill="#FFFFFF" class="bold"> ANAS</tspan>
      <tspan fill="#00F0FF"> [@chroll0ps]</tspan>
    </text>
    <text x="44" y="128" class="mono" font-size="12.5">
      <tspan fill="#FFE600" class="bold">ARCHITECT :</tspan>
      <tspan fill="#FFFFFF"> AI &amp; Data Systems // Full-Stack Eng</tspan>
    </text>
    <text x="44" y="150" class="mono" font-size="12.5">
      <tspan fill="#FFE600" class="bold">LOCATION  :</tspan>
      <tspan fill="#CBD5E1"> Marrakech, Morocco </tspan>
      <tspan fill="#B8FF00">[31.63&#x00B0;N, 7.98&#x00B0;W]</tspan>
    </text>
  </g>

  <g class="b-step-3">
    <text x="24" y="192" class="mono bold" font-size="12.5">
      <tspan fill="#B8FF00">root@chroll0ps:~#</tspan>
      <tspan fill="#FFFFFF"> cat /sys/core_stack.json</tspan>
    </text>
  </g>

  <g class="b-step-4">
    <text x="34" y="214" class="mono" font-size="12">
      <tspan fill="#00F0FF" class="bold">"ai_genai"  </tspan><tspan fill="#64748B">: </tspan><tspan fill="#FFE600">["PyTorch", "Groq", "Gemini", "RAG", "MLflow"]</tspan>
    </text>
    <text x="34" y="232" class="mono" font-size="12">
      <tspan fill="#00F0FF" class="bold">"data_eng"  </tspan><tspan fill="#64748B">: </tspan><tspan fill="#B8FF00">["Kafka", "Spark", "Airflow", "Databricks"]</tspan>
    </text>
  </g>
  <g class="b-step-5">
    <text x="34" y="250" class="mono" font-size="12">
      <tspan fill="#00F0FF" class="bold">"fullstack" </tspan><tspan fill="#64748B">: </tspan><tspan fill="#FF5E7E">["TypeScript", "Next.js", "FastAPI", "React"]</tspan>
    </text>
    <text x="34" y="268" class="mono" font-size="12">
      <tspan fill="#00F0FF" class="bold">"cloud_ops" </tspan><tspan fill="#64748B">: </tspan><tspan fill="#C084FC">["AWS", "OCI", "Azure", "Docker", "K8s"]</tspan>
    </text>
  </g>

  <g class="b-step-6">
    <text x="24" y="296" class="mono bold" font-size="12.5">
      <tspan fill="#B8FF00">root@chroll0ps:~#</tspan>
      <tspan fill="#FFFFFF"> ./verify_credentials.sh --all</tspan>
    </text>
  </g>

  <g class="b-step-7">
    <text x="34" y="317" class="mono" font-size="12">
      <tspan fill="#B8FF00" class="bold">[PASS]</tspan><tspan fill="#F8FAFC"> Databricks GenAI &amp; AI Security Fundamentals</tspan>
    </text>
    <text x="34" y="335" class="mono" font-size="12">
      <tspan fill="#00F0FF" class="bold">[PASS]</tspan><tspan fill="#F8FAFC"> OCI Architect &amp; Foundations | AWS Cloud</tspan>
    </text>
  </g>
  <g class="b-step-8">
    <text x="34" y="353" class="mono" font-size="12">
      <tspan fill="#FFE600" class="bold">[PROD]</tspan><tspan fill="#F8FAFC"> Enterprise Systems Shipped @ OCP &amp; Radees</tspan>
    </text>
  </g>

  <g class="b-step-9">
    <text x="24" y="381" class="mono bold" font-size="12.5">
      <tspan fill="#B8FF00">root@chroll0ps:~#</tspan>
      <tspan fill="#00F0FF"> ready --build="high-impact-systems"</tspan>
    </text>
    <rect class="cursor" x="456" y="368" width="9" height="15" fill="#FFE600" />
  </g>

  <!-- RIGHT PANE: LIVE PIPELINE TOPOLOGY -->
  <rect x="612" y="64" width="254" height="114" fill="#000000" />
  <rect x="608" y="60" width="254" height="114" fill="#141414" stroke="#00F0FF" stroke-width="2.5" />
  <rect x="608" y="60" width="254" height="22" fill="#00F0FF" />
  <text x="618" y="75" class="mono bold" font-size="11" fill="#000000" letter-spacing="1">LIVE PIPELINE TOPOLOGY</text>

  <path d="M 654 106 L 820 106 L 820 129 L 654 129 L 654 152 L 820 152" fill="none" stroke="#334155" stroke-width="2" stroke-dasharray="4 3" />

  <rect x="-4" y="-4" width="8" height="8" fill="#FFE600" stroke="#000000" stroke-width="1.5">
    <animateMotion dur="3.6s" repeatCount="indefinite" path="M 654 106 L 737 106 L 820 106 L 820 129 L 654 129 L 654 152 L 737 152 L 820 152" />
  </rect>
  <rect x="-4" y="-4" width="8" height="8" fill="#B8FF00" stroke="#000000" stroke-width="1.5">
    <animateMotion dur="3.6s" begin="1.8s" repeatCount="indefinite" path="M 654 106 L 737 106 L 820 106 L 820 129 L 654 129 L 654 152 L 737 152 L 820 152" />
  </rect>

  <rect x="622" y="94" width="64" height="24" fill="#0D0D0D" stroke="#FFE600" stroke-width="2" />
  <text x="654" y="110" text-anchor="middle" class="mono bold" font-size="10.5" fill="#FFE600">KAFKA</text>

  <rect x="705" y="94" width="64" height="24" fill="#0D0D0D" stroke="#FF5E7E" stroke-width="2" />
  <text x="737" y="110" text-anchor="middle" class="mono bold" font-size="10.5" fill="#FF5E7E">SPARK</text>

  <rect x="788" y="94" width="64" height="24" fill="#0D0D0D" stroke="#00F0FF" stroke-width="2" />
  <text x="820" y="110" text-anchor="middle" class="mono bold" font-size="10.5" fill="#00F0FF">LAKE</text>

  <rect x="622" y="140" width="64" height="24" fill="#0D0D0D" stroke="#C084FC" stroke-width="2" />
  <text x="654" y="156" text-anchor="middle" class="mono bold" font-size="10.5" fill="#C084FC">RAG</text>

  <rect x="705" y="140" width="64" height="24" fill="#0D0D0D" stroke="#B8FF00" stroke-width="2" />
  <text x="737" y="156" text-anchor="middle" class="mono bold" font-size="10.5" fill="#B8FF00">API</text>

  <rect x="788" y="140" width="64" height="24" fill="#0D0D0D" stroke="#FFFFFF" stroke-width="2" />
  <text x="820" y="156" text-anchor="middle" class="mono bold" font-size="10.5" fill="#FFFFFF">UI</text>

  <!-- RIGHT PANE: KERNEL LOAD -->
  <rect x="612" y="192" width="254" height="122" fill="#000000" />
  <rect x="608" y="188" width="254" height="122" fill="#141414" stroke="#FFE600" stroke-width="2.5" />
  <rect x="608" y="188" width="254" height="22" fill="#FFE600" />
  <text x="618" y="203" class="mono bold" font-size="11" fill="#000000" letter-spacing="1">CORE KERNEL LOAD</text>

  <text x="618" y="228" class="mono bold" font-size="10.5" fill="#FFFFFF">AI / RAG</text>
  <rect x="688" y="218" width="128" height="11" fill="#222222" stroke="#000000" stroke-width="1.5" />
  <rect class="bar-fill" x="689" y="219" width="122" height="9" fill="#FFE600" />
  <text x="824" y="228" class="mono bold" font-size="10.5" fill="#FFE600">96%</text>

  <text x="618" y="252" class="mono bold" font-size="10.5" fill="#FFFFFF">DATA ENG</text>
  <rect x="688" y="242" width="128" height="11" fill="#222222" stroke="#000000" stroke-width="1.5" />
  <rect class="bar-fill" x="689" y="243" width="118" height="9" fill="#00F0FF" />
  <text x="824" y="252" class="mono bold" font-size="10.5" fill="#00F0FF">94%</text>

  <text x="618" y="276" class="mono bold" font-size="10.5" fill="#FFFFFF">FULL-STK</text>
  <rect x="688" y="266" width="128" height="11" fill="#222222" stroke="#000000" stroke-width="1.5" />
  <rect class="bar-fill" x="689" y="267" width="115" height="9" fill="#B8FF00" />
  <text x="824" y="276" class="mono bold" font-size="10.5" fill="#B8FF00">92%</text>

  <text x="618" y="300" class="mono bold" font-size="10.5" fill="#FFFFFF">CLOUD</text>
  <rect x="688" y="290" width="128" height="11" fill="#222222" stroke="#000000" stroke-width="1.5" />
  <rect class="bar-fill" x="689" y="291" width="112" height="9" fill="#FF5E7E" />
  <text x="824" y="300" class="mono bold" font-size="10.5" fill="#FF5E7E">90%</text>

  <!-- RIGHT PANE: SIGNAL EQUALIZER -->
  <rect x="612" y="328" width="254" height="58" fill="#000000" />
  <rect x="608" y="324" width="254" height="58" fill="#141414" stroke="#B8FF00" stroke-width="2.5" />

  <text x="620" y="347" class="mono bold" font-size="11" fill="#B8FF00">STATUS : OPTIMAL</text>
  <text x="620" y="368" class="mono" font-size="10.5" fill="#CBD5E1">UPTIME : 99.98%</text>

  <rect class="eq eq1" x="768" y="336" width="7" height="34" fill="#FFE600" />
  <rect class="eq eq2" x="779" y="336" width="7" height="34" fill="#00F0FF" />
  <rect class="eq eq3" x="790" y="336" width="7" height="34" fill="#B8FF00" />
  <rect class="eq eq4" x="801" y="336" width="7" height="34" fill="#FF5E7E" />
  <rect class="eq eq5" x="812" y="336" width="7" height="34" fill="#C084FC" />
  <rect class="eq eq6" x="823" y="336" width="7" height="34" fill="#FFE600" />
  <rect class="eq eq7" x="834" y="336" width="7" height="34" fill="#00F0FF" />
  <rect class="eq eq8" x="845" y="336" width="7" height="34" fill="#B8FF00" />
</svg>
"""

# 5. FOOTER
FILES["assets/brutal-footer.svg"] = """<?xml version="1.0" encoding="UTF-8"?>
<svg viewBox="0 0 900 92" width="900" height="92" xmlns="[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)">
  <style><![CDATA[
    @keyframes footerStripe {
      0%, 24%  { fill: #FFE600; }
      25%, 49% { fill: #00F0FF; }
      50%, 74% { fill: #B8FF00; }
      75%, 99% { fill: #FF5E7E; }
      100%     { fill: #FFE600; }
    }
    .stripe { animation: footerStripe 8s linear infinite; }
    .mono   { font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; font-weight: 800; }
  ]]></style>

  <rect x="12" y="12" width="880" height="72" fill="#000000" />
  <rect x="4" y="4" width="880" height="72" fill="#0D0D0D" stroke="#000000" stroke-width="4" />
  <rect class="stripe" x="4" y="4" width="880" height="14" stroke="#000000" stroke-width="4" />

  <text x="444" y="52" text-anchor="middle" class="mono" font-size="16" fill="#FFFFFF" letter-spacing="3">
    ENGINEERED FOR SCALE <tspan fill="#FFE600">&#x2726;</tspan> DESIGNED FOR CLARITY
  </text>
</svg>
"""

# 6. ALL 9 ANIMATED SECTION HEADERS
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

HEADER_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<svg viewBox="0 0 900 72" width="900" height="72" xmlns="[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)">
  <defs>
    <clipPath id="scanClip">
      <rect x="102" y="51" width="782" height="5" />
    </clipPath>
  </defs>
  <style><![CDATA[
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
  ]]></style>

  <rect x="11" y="11" width="882" height="54" fill="#000000" />
  <rect x="4" y="4" width="882" height="54" fill="#0D0D0D" stroke="#000000" stroke-width="4" />
  <rect class="idx-box" x="4" y="4" width="96" height="54" stroke="#000000" stroke-width="4" />
  <text x="52" y="38" text-anchor="middle" class="mono" font-size="20" fill="#000000">[ {num} ]</text>
  <text x="122" y="38" class="heading" font-size="19.5" fill="#FFFFFF">{title}</text>

  <g clip-path="url(#scanClip)">
    <rect class="scanner" x="102" y="52" width="160" height="4" fill="{c1}" />
  </g>

  <rect class="b1" x="820" y="16" width="12" height="28" fill="{c1}" />
  <rect class="b2" x="838" y="16" width="12" height="28" fill="{c2}" />
  <rect class="b3" x="856" y="16" width="12" height="28" fill="{c3}" />
</svg>
"""

for fname, num, title, c1, c2, c3 in SECTIONS:
    FILES[f"assets/headers/{fname}"] = HEADER_TEMPLATE.format(
        num=num, title=html.escape(title), c1=c1, c2=c2, c3=c3
    )

# WRITE & STRICTLY XML-VALIDATE EVERY FILE
for path, content in FILES.items():
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content.strip() + "\n")
    try:
        ET.parse(path)
        print(f"[OK] {path}")
    except ET.ParseError as e:
        print(f"[XML ERROR] {path}: {e}")
