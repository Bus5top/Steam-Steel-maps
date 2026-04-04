# Steam & Steel Map Planner

This repository now contains a structured planner extraction from the Steam & Steel fandom wiki.
It combines map details with starter engine grade data so you can plan which map to build and which locomotive grade is expected.

## Data files
- `data/steam_steel_maps.json` — map metadata, starter engine, terrain roughness, starting money, cargo adjustment, and initial depot config.
- `data/steam_steel_locomotives.json` — locomotive grade data and stats for Steam & Steel engine classes.
- `scripts/fetch_wiki_data.py` — fetches the wiki pages and regenerates the datasets.

## Map planning overview

| Map | Difficulty | Roughness | Starter Engine | Starting Money | Cargo Adj | Build note |
|---|---|---|---|---|---|---|
| Badlands | Medium | Low/Medium | Class C | $30000 | +0% | Desert map, moderate hills, starter Class C works well. |
| Coal Valley | Easy | Low | Class C | $20000 | +0% | Flat, beginner-friendly, easy expansion and gentle slopes. |
| Gold Rush | Hard | High | Class C | $40000 | +15% | Mountain desert; steep grades require careful route planning. |
| Hazel Sierra | Hard | High | Class D1 | 30,000 $ | Unknown | Mix of valley and mountain industries, use tender-equipped starter engines. |
| Maple Ridge | Medium | Medium | Class A2 | 40,000 $ | +23% | Hilly map with many industries; curve and grade placement matter for efficiency. |
| Misty Summit | Hard - Very Hard | Very high | Class A0 | 60,000 $ | +200% | Very steep winter mountain; strong starter engine and tender are recommended. |
| Scarlet Heights | Very Hard | Very High | Class C | $60000 | +23% | Extreme slopes; grade settings are critical, avoid overly steep inclines. |
| Stormy Coast | Medium | Medium/High | Class A1 | $40000 | -31% | Island terrain with rocky hills and longer industry distances. |

## Planning tips

- **Starter engine grade**: use the provided `starter_engine` per map to know which locomotive class is viable from the depot.
- **Roughness** helps estimate how much grade/curve work you'll need; `High` and `Very High` maps need more careful track layout.
- **Scarlet Heights** has an explicit grade warning in its wiki notes: slow, sloped routing is more reliable than steep direct climbs.
- **Misty Summit** and **Gold Rush** are the hardest terrain maps; consider tender-equipped engines for longer runs.

## How to use this repo

1. Run `python3 scripts/fetch_wiki_data.py` to refresh data from the wiki.
2. Open `data/steam_steel_maps.json` to inspect map-grade planning fields.
3. Open `data/steam_steel_locomotives.json` to compare engine classes and build criteria.

Use these files as the base for building a route planner, choosing engines, or exporting a visual map planning tool.
