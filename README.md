# Steam-Steel-maps

This repository extracts Steam & Steel map and locomotive data from the fandom wiki to support planning and building.

## Included files
- `scripts/fetch_wiki_data.py`: fetches the latest wiki content and generates structured planner data.
- `data/steam_steel_maps.json`: extracted map metadata including starter engine, difficulty, roughness, starting money, and depot setup.
- `data/steam_steel_locomotives.json`: extracted locomotive class stats for engine grading and build planning.
- `docs/steam_steel_planner.md`: a planner guide that summarizes each map and its build considerations.

## Usage
Run:

```bash
python3 scripts/fetch_wiki_data.py
```

Then inspect the JSON data or the planner guide in `docs/steam_steel_planner.md`.
