<img width="1000" height="569" alt="image" src="https://github.com/user-attachments/assets/285647e2-c64c-4469-be86-2f5c54a713c0" />


<h2 align="center">🤝 Meet Our Team</h2>

<table align="center">
  <tr>
    <th>Team Member</th>
    <th>GitHub</th>
    <th>LinkedIn</th>
  </tr>
  <tr>
    <th> Ollila Simiyu — Project Lead</th>
    <td>
      <a href="https://github.com/YOUR_USERNAME">
        <img src="https://cdn.simpleicons.org/github/181717"
             width="45" height="45" alt="GitHub">
      </a>
    </td>
    <td>
      <a href="https://linkedin.com/in/YOUR_PROFILE">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linkedin/linkedin-original.svg"
             width="45" height="45" alt="LinkedIn">
      </a>
    </td>
  </tr>
  <tr>
    <th> Lilly Rutto </th>
    <td><a href="https://github.com/USER1">
      <img src="https://cdn.simpleicons.org/github/181717" width="45" alt="GitHub">
    </a></td>
    <td><a href="https://linkedin.com/in/USER1">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linkedin/linkedin-original.svg" width="45" alt="LinkedIn">
    </a></td>
  </tr>
  <tr>
    <th> Chemutai </th>
    <td><a href="https://github.com/USER2">
      <img src="https://cdn.simpleicons.org/github/181717" width="45" alt="GitHub">
    </a></td>
    <td><a href="https://linkedin.com/in/USER2">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linkedin/linkedin-original.svg" width="45" alt="LinkedIn">
    </a></td>
  </tr>
  <tr>
    <td>Collaborator 3</td>
    <td><a href="https://github.com/USER3">
      <img src="https://cdn.simpleicons.org/github/181717" width="45" alt="GitHub">
    </a></td>
    <td><a href="https://linkedin.com/in/USER3">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linkedin/linkedin-original.svg" width="45" alt="LinkedIn">
    </a></td>
  </tr>
</table>


<h2 align="center">⚡ Motion Detection App — Tech Stack </h2>

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,pytorch,opencv,docker,,githubactions,git,github&theme=dark" alt="Technology Stack"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Ray-028CF0?style=for-the-badge" alt="Ray"/>
  <img src="https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge" alt="MLflow"/>
  <img src="https://img.shields.io/badge/DVC-945DD6?style=for-the-badge" alt="DVC"/>
  <img src="https://img.shields.io/badge/MediaPipe-0097A7?style=for-the-badge" alt="MediaPipe"/>
</p>

# 📡 Motion Detection App

An AI-powered motion detection app that watches a camera feed, detects movement, understands what happened, and sends alerts.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge) ![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge) ![Firebase](https://img.shields.io/badge/Firebase-FFA000?style=for-the-badge) ![OpenAI](https://img.shields.io/badge/OpenAI-10A37F?style=for-the-badge) ![Claude](https://img.shields.io/badge/Claude-D97757?style=for-the-badge) ![n8n](https://img.shields.io/badge/n8n-EA4B71?style=for-the-badge) ![Solidity](https://img.shields.io/badge/Solidity-5C6BC0?style=for-the-badge) ![Ethereum](https://img.shields.io/badge/Ethereum-627EEA?style=for-the-badge) ![Solana](https://img.shields.io/badge/Solana-9945FF?style=for-the-badge)

## Tech Stack

<p align="center">
  <img src="./tech-stack.svg" alt="Animated tech stack: Python, Supabase, Firebase, OpenAI, Claude, n8n, Solidity, Ethereum, Solana" width="100%">
</p>

| Tool | Role in the project |
|------|---------------------|
| **Python** | Core logic and motion detection |
| **Supabase** | Database, auth and storage |
| **Firebase** | Realtime alerts and push notifications |
| **OpenAI** | Vision and scene understanding |
| **Claude** | Reasoning and smart alert summaries |
| **n8n** | Workflow automation |
| **Solidity** | Smart contracts |
| **Ethereum** | Tamper-proof event records |
| **Solana** | Fast, low-cost on-chain logging |

**Pipeline:** `Capture → Detect → Analyze → Alert → Record`

## Adding or removing a tool

1. Open `motion-detection-app.html` in any text editor.
2. Find the `TOOLS` list. Each tool is one line: delete a line to remove a tool, copy a line to add one.
3. Update the table above to match.

> **Note:** GitHub READMEs don’t run JavaScript, so the animation above is an animated SVG (`tech-stack.svg`). The full interactive version is the HTML file below. Download it and open it in a browser.

<details>
<summary><b>📄 Full source: <code>motion-detection-app.html</code></b> (click to expand)</summary>

````html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Motion Detection App — Tech Stack</title>
<style>
:root{--bg:#f6f3ec;--fg:#1f1d19;--muted:#6b665c;--card:#fff;--line:#e3ddd0}
@media (prefers-color-scheme:dark){:root{--bg:#0f1115;--fg:#f1efe9;--muted:#9a978f;--card:#191c22;--line:#2a2e36}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font-family:ui-monospace,Menlo,Consolas,monospace;min-height:100vh;overflow-x:hidden}
main{max-width:1000px;margin:0 auto;padding:28px 18px 40px}
.live{display:inline-flex;align-items:center;gap:8px;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.live i{width:9px;height:9px;border-radius:50%;background:#ef4444;animation:blink 1.2s infinite}
h1{font-family:system-ui,Segoe UI,sans-serif;font-size:clamp(26px,5vw,42px);margin:10px 0 6px;line-height:1.1;
background:linear-gradient(90deg,#3776AB,#10A37F,#D97757,#EA4B71,#9945FF,#3776AB);background-size:200% 100%;
-webkit-background-clip:text;background-clip:text;color:transparent;animation:flow 6s linear infinite}
.sub{color:var(--muted);font-size:14px;margin:0}
.radar{display:block;width:min(260px,70%);margin:18px auto 8px}
.sweep{transform-origin:100px 100px;animation:spin 4s linear infinite}
.blip{animation:blip 4s infinite}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:18px;margin:26px 0}
.tile{position:relative;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:18px 12px 16px;text-align:center;
animation:float 4s ease-in-out infinite;animation-delay:calc(var(--i)*.35s);transition:transform .25s,box-shadow .4s,border-color .4s}
.tile::after{content:"";position:absolute;inset:-7px;border:2px solid var(--c);border-radius:23px;opacity:0;transform:scale(1.1);transition:.4s;pointer-events:none}
.tile.on{border-color:var(--c);box-shadow:0 0 28px 4px color-mix(in srgb,var(--c) 50%,transparent)}
.tile.on::after{opacity:1;transform:scale(1)}
.tile:hover{transform:translateY(-6px) scale(1.04)}
.tile:hover .ico{transform:rotate(-8deg) scale(1.1)}
.ico{width:72px;height:72px;margin:0 auto 12px;border-radius:20px;display:grid;place-items:center;
background:color-mix(in srgb,var(--c) 16%,var(--card));transition:transform .3s;color:var(--c);font:700 24px system-ui,sans-serif}
.ico svg{width:42px;height:42px}
.tile b{display:block;font-family:system-ui,sans-serif;font-size:16px;color:var(--c)}
.tile span{display:block;font-size:11.5px;color:var(--muted);margin-top:5px;line-height:1.4}
.flow{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:8px;font-size:12px}
.flow em{font-style:normal;padding:7px 12px;border-radius:99px;border:1px solid var(--line);background:var(--card);transition:.4s}
.flow em.on{background:color-mix(in srgb,#10A37F 30%,var(--card));border-color:#10A37F}
.flow u{text-decoration:none;color:var(--muted)}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes blink{50%{opacity:.2}}
@keyframes flow{to{background-position:200% 0}}
@keyframes float{50%{translate:0 -7px}}
@keyframes blip{0%,100%{opacity:.15}12%{opacity:1}40%{opacity:.15}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
</style>
</head>
<body>
<main>
<span class="live"><i></i>Scanning for motion</span>
<h1>Motion Detection App — Tech Stack</h1>
<p class="sub">Every tool we’ll use to build the app, and the job each one does.</p>

<svg class="radar" viewBox="0 0 200 200" aria-hidden="true">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#10A37F" stop-opacity="0"/><stop offset="1" stop-color="#10A37F" stop-opacity=".75"/></linearGradient></defs>
<g fill="none" stroke="var(--line)" stroke-width="1.5"><circle cx="100" cy="100" r="92"/><circle cx="100" cy="100" r="62"/><circle cx="100" cy="100" r="32"/><path d="M8 100h184M100 8v184"/></g>
<g class="sweep"><path d="M100 100L100 8A92 92 0 0 1 165 35Z" fill="url(#g)"/><path d="M100 100L165 35" stroke="#10A37F" stroke-width="2"/></g>
<circle class="blip" cx="140" cy="62" r="4" fill="#EA4B71" style="animation-delay:.4s"/>
<circle class="blip" cx="70" cy="130" r="4" fill="#FFA000" style="animation-delay:1.4s"/>
<circle class="blip" cx="128" cy="140" r="4" fill="#9945FF" style="animation-delay:2.4s"/>
<circle class="blip" cx="60" cy="70" r="4" fill="#3ECF8E" style="animation-delay:3.2s"/>
</svg>

<div class="grid" id="grid"></div>
<div class="flow" id="flow"></div>
</main>

<script>
/* ============================================================
   EDIT HERE — this list is the only thing you need to change.
   ADD a tool:    copy one line below, paste it in the list, edit it.
   REMOVE a tool: delete its line.
   icon: an inline <svg>…</svg>, or 'text:CV' to show initials.
   color: any hex color (tints the card, name and glow).
   Animation timing adjusts automatically.
   ============================================================ */
const TOOLS = [
 {name:'Python',   role:'Core logic and motion detection',       color:'#3776AB', icon:`<svg viewBox="0 0 48 48"><rect x="9" y="6" width="22" height="22" rx="8" fill="#3776AB"/><rect x="17" y="20" width="22" height="22" rx="8" fill="#FFD43B"/><circle cx="17" cy="13" r="2" fill="#fff"/><circle cx="31" cy="35" r="2" fill="#3776AB"/></svg>`},
 {name:'Supabase', role:'Database, auth and storage',            color:'#3ECF8E', icon:`<svg viewBox="0 0 48 48"><path d="M27 4L8 27h14l-2 17 20-25H26z" fill="#3ECF8E"/><path d="M27 4L8 27h14z" fill="#1fa86c" opacity=".55"/></svg>`},
 {name:'Firebase', role:'Realtime alerts and push notifications',color:'#FFA000', icon:`<svg viewBox="0 0 48 48"><path d="M24 5c2 8 11 12 11 24a11 11 0 0 1-22 0c0-5 3-8 5-11 1 3 2 4 4 4-1-6 0-11 2-17z" fill="#FF9100"/><path d="M24 24c3 3 6 5 6 9a6 6 0 0 1-12 0c0-3 3-5 6-9z" fill="#FFCA28"/></svg>`},
 {name:'OpenAI',   role:'Vision and scene understanding',        color:'#10A37F', icon:`<svg viewBox="0 0 48 48" fill="none" stroke-width="3.5"><rect x="12" y="15" width="24" height="18" rx="9" stroke="#10A37F"/><rect x="12" y="15" width="24" height="18" rx="9" transform="rotate(60 24 24)" stroke="#0ea5e9"/><rect x="12" y="15" width="24" height="18" rx="9" transform="rotate(120 24 24)" stroke="#6366f1"/></svg>`},
 {name:'Claude',   role:'Reasoning and smart alert summaries',   color:'#D97757', icon:`<svg viewBox="0 0 48 48" stroke="#D97757" stroke-width="3.5" stroke-linecap="round"><path d="M24 5v38"/><path d="M24 5v38" transform="rotate(30 24 24)"/><path d="M24 5v38" transform="rotate(60 24 24)"/><path d="M24 5v38" transform="rotate(90 24 24)"/><path d="M24 5v38" transform="rotate(120 24 24)"/><path d="M24 5v38" transform="rotate(150 24 24)"/></svg>`},
 {name:'n8n',      role:'Workflow automation',                   color:'#EA4B71', icon:`<svg viewBox="0 0 48 48"><path d="M13 24h6M29 22l6-6M29 26l6 6" stroke="#EA4B71" stroke-width="3" stroke-linecap="round"/><g fill="#EA4B71"><circle cx="9" cy="24" r="5"/><circle cx="24" cy="24" r="5"/><circle cx="39" cy="13" r="5"/><circle cx="39" cy="35" r="5"/></g></svg>`},
 {name:'Solidity', role:'Smart contracts',                       color:'#5C6BC0', icon:`<svg viewBox="0 0 48 48"><path d="M24 4l8 8-8 8-8-8z" fill="#4FC3F7"/><path d="M24 20l8 8-8 8-8-8z" fill="#7C4DFF"/><path d="M24 34l8 5-8 5-8-5z" fill="#26C6DA"/></svg>`},
 {name:'Ethereum', role:'Tamper-proof event records',            color:'#627EEA', icon:`<svg viewBox="0 0 48 48"><path d="M24 3L12 24l12 7z" fill="#8FA2F5"/><path d="M24 3l12 21-12 7z" fill="#627EEA"/><path d="M12 27l12 7v11z" fill="#8FA2F5"/><path d="M36 27l-12 7v11z" fill="#4A63C9"/></svg>`},
 {name:'Solana',   role:'Fast, low-cost on-chain logging',       color:'#9945FF', icon:`<svg viewBox="0 0 48 48"><defs><linearGradient id="sol" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#9945FF"/><stop offset="1" stop-color="#14F195"/></linearGradient></defs><g fill="url(#sol)"><path d="M12 10h28l-4 7H8z"/><path d="M8 20.5h28l4 7H12z"/><path d="M12 31h28l-4 7H8z"/></g></svg>`},
 // Example of adding one with initials instead of a logo (remove the // to use):
 // {name:'OpenCV', role:'Frame analysis and motion tracking', color:'#FF5722', icon:'text:CV'},
];

// The pipeline strip at the bottom — edit the words freely.
const FLOW = ['Capture','Detect','Analyze','Alert','Record'];
/* ============================================================ */

const grid = document.getElementById('grid');
grid.innerHTML = TOOLS.map((t,i)=>`
  <div class="tile" style="--c:${t.color};--i:${i}">
    <div class="ico">${t.icon.startsWith('text:') ? t.icon.slice(5) : t.icon}</div>
    <b>${t.name}</b><span>${t.role}</span>
  </div>`).join('');

document.getElementById('flow').innerHTML =
  FLOW.map(w=>`<em>${w}</em>`).join('<u>→</u>');

function cycle(nodes, ms){
  if(!nodes.length) return;
  let i = 0;
  setInterval(()=>{
    nodes.forEach(n=>n.classList.remove('on'));
    nodes[i % nodes.length].classList.add('on');
    i++;
  }, ms);
}
cycle([...document.querySelectorAll('.tile')], 1100);
cycle([...document.querySelectorAll('.flow em')], 1500);
</script>
</body>
</html>

````

</details>

## Getting started

```bash
git clone <your-repo-url>
cd motion-detection-app
open motion-detection-app.html   # or just double-click the file
```

