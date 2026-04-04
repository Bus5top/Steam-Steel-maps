# 🛣️ Steam & Steel Planner — System Architecture

## Overview
Your Steam & Steel mapping tool is now a complete **community-driven platform** with interactive route planning, shared strategies, and guide contributions.

---

## 📁 File Structure

### Core Pages
- **`index.html`** — 🏠 Home hub with navigation to all tools
- **`planner.html`** — 🛣️ **Main interactive route planner** (select official map → draw routes)
- **`viewer.html`** — 🤝 Community plans gallery (browse & download shared routes)
- **`guide-contribute.html`** — 📖 Planning guide contribution form (add tips)
- **`editor.html`** — *(Legacy)* Old map editor, can be archived

### Data Files
- **`data/steam_steel_maps.json`** — Official maps database
- **`data/steam_steel_locomotives.json`** — Engine class reference
- **`docs/steam_steel_planner.md`** — Official planning guide

---

## 🎯 User Workflows

### 1️⃣ Route Planning (Main Feature)
```
index.html → [Start Planning Routes] 
  ↓ planner.html
  ├─ Select official map from list
  ├─ Draw routes (click-drag)
  ├─ Mark tunnels (click to place)
  ├─ Mark stations (click to place)
  ├─ Use colors for different route layers
  ├─ Undo/Clear tools
  ├─ Save locally (browser localStorage)
  └─ Export/Import plan codes (shareable)
```

### 2️⃣ Browse Community Plans
```
index.html → [Community Plans]
  ↓ viewer.html
  ├─ Search by title/creator
  ├─ Filter by map
  ├─ View shared route plans
  ├─ Download/import plans
  └─ Rate and review
```

### 3️⃣ Contribute to Guide
```
index.html → [Share Your Tips]
  ↓ guide-contribute.html
  ├─ Select map
  ├─ Choose tip category:
  │   ├─ Route Strategy
  │   ├─ Terrain & Grades
  │   ├─ Engine Selection
  │   ├─ Cargo Handling
  │   └─ General Tips
  ├─ Write detailed advice
  ├─ Optional: Sign your name
  └─ Stored in browser localStorage
```

---

## 🎨 Planner Features

### Drawing Tools
- **Route** — Draw rail lines with click-drag
- **Tunnel** — Mark tunnel locations (click)
- **Station** — Mark station locations (click)
- **Erase** — Remove routes near cursor (click)
- **Clear** — Remove all drawings

### Colors
- Blue (default), Red, Green, Orange, Purple, Black
- Use different colors for different route layers

### Controls
- **Ctrl+Z** / **Z key** — Undo last action
- **C key** — Clear all
- **Right-click** — Context menu
- **Click & drag** — Draw routes

### Save/Share
- **Save locally** — Saves to browser (persists between sessions)
- **Export plan** — Copy shareable code
- **Import plan** — Paste code to load shared plans

---

## 💾 Data Storage

### Local Storage (Browser)
- **`steamsteelplans`** — User's route plans (keyed by map name)
- **`steamsteelcontributions`** — Planning guide tips submitted
- **`steamsteelsharedplans`** — Community shared plans (demo data included)

### To Sync Plans
1. Export plan from planner as code
2. Share code with others
3. They import the code in their planner

---

## 🚀 Future Enhancements

### Backend Integration
- User accounts & authentication
- API to sync plans across devices
- Community rating/voting system
- Plan versioning & history
- Export to image/PDF

### Features to Add
- Image/map screenshot import
- Terrain elevation display
- Grade/curve calculator
- Distance measurements
- Multiplayer editing

---

## 📋 Quick Reference

| Page | Purpose | URL | Features |
|------|---------|-----|----------|
| Home | Navigation hub | `/` or `index.html` | Links to all tools |
| Planner | Draw routes | `/planner.html` | Interactive drawing, save/export |
| Community | Browse plans | `/viewer.html` | Search, filter, download |
| Contribute | Add tips | `/guide-contribute.html` | Form submissions, local storage |
| Guide | Official info | `/docs/steam_steel_planner.md` | Read-only reference |

---

## 🔧 Configuration

### Map Sources
- All stored in `data/steam_steel_maps.json`
- Add new maps by editing this file
- Each map needs: title, difficulty, roughness, starter_engine, display_money, initial_depot

### Vercel Deployment
- Static hosting configured in `vercel.json`
- All HTML/CSS/JS served from root
- No backend required (fully client-side)

---

## 👥 Community Flow

```
Player A
  creates route plan
  → export code
       ↓
Player B
  imports code
  → modifies route
  → exports new code
       ↓
Player C
  downloads from Community Plans
  → shares tips to guide
       ↓
Planning Guide grows!
```

---

**Ready to deploy! 🚀 All files are Vercel-ready and work completely offline (with localStorage).**
