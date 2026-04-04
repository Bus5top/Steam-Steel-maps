#!/usr/bin/env python3
import json
import re
import requests
from pathlib import Path

BASE_URL = 'https://steam-steel.fandom.com/api.php'
HEADERS = {'User-Agent': 'Mozilla/5.0'}
MAP_TITLES = [
    'Badlands',
    'Coal Valley',
    'Gold Rush',
    'Hazel Sierra',
    'Maple Ridge',
    'Misty Summit',
    'Scarlet Heights',
    'Stormy Coast',
]
LOCO_TITLES = [
    'Bee',
    'Class A',
    'Class A0',
    'Class A1',
    'Class A2',
    'Class B',
    'Class B2',
    'Class C',
    'Class D1',
    'Class D2',
    'Class E',
    'Class F',
    'Class G',
    'Class H',
    'Class H2',
    'Class I',
    'Class J2',
    'Class K1',
    'Class K2',
    'Class N',
    'Class P',
    'Coffeepot',
]
OUTPUT_DIR = Path(__file__).resolve().parent.parent / 'data'
OUTPUT_DIR.mkdir(exist_ok=True)


def fetch_wikitext(title: str) -> str:
    params = {
        'action': 'query',
        'format': 'json',
        'titles': title,
        'prop': 'revisions',
        'rvprop': 'content',
    }
    resp = requests.get(BASE_URL, params=params, headers=HEADERS)
    resp.raise_for_status()
    data = resp.json()
    pages = data['query']['pages']
    page = next(iter(pages.values()))
    if 'missing' in page:
        raise RuntimeError(f'Missing page: {title}')
    return page['revisions'][0]['*']


def clean_link(value: str) -> str:
    value = value.strip()
    if value.startswith('[[') and value.endswith(']]'):
        inner = value[2:-2]
        return inner.split('|')[-1].strip()
    return value


def parse_template(template_name: str, text: str) -> dict:
    pattern = re.compile(r'\{\{\s*' + re.escape(template_name) + r'(?:[ _][^|\}]+)?\s*\|(.+?)\}\}', re.S | re.I)
    match = pattern.search(text)
    if not match:
        return {}
    body = match.group(1)
    fields = {}
    for part in re.split(r'\|(?=[^\|]*=)', body):
        if '=' not in part:
            continue
        key, value = part.split('=', 1)
        fields[key.strip()] = value.strip()
    return fields


def parse_map_page(title: str, text: str) -> dict:
    detail = {'title': title}
    diff = parse_template('Difficulty', text)
    detail.update({
        'starter_engine': clean_link(diff.get('StarterEngine', '')),
        'starting_money': diff.get('Money', '').strip(),
        'roughness': diff.get('Roughness', '').strip(),
        'difficulty': diff.get('difficulty', '').strip() or diff.get('Difficulty', '').strip(),
    })
    info = parse_template('Map info', text)
    if not info:
        info = parse_template('Map_info', text)
    if info:
        cargo_value = info.get('cargo', '').strip()
        cargo_value = re.sub(r'\{\{.*?\}\}', '', cargo_value)
        cargo_value = re.sub(r'\{\{.*', '', cargo_value)
        detail.update({
            'creator': info.get('creator', '').strip(),
            'date_added': info.get('Date', '').strip(),
            'display_money': info.get('money', '').strip(),
            'display_difficulty': info.get('difficulty', '').strip(),
            'cargo_adjustment': cargo_value.strip(),
        })
    if not detail.get('difficulty') and detail.get('display_difficulty'):
        detail['difficulty'] = detail['display_difficulty']
    if not detail.get('starting_money') and detail.get('display_money'):
        detail['starting_money'] = detail['display_money']
    depot_match = re.search(r'==+\s*Initial Depot Configuration\s*==+(.*?)(?:==|$)', text, re.S | re.I)
    if depot_match:
        depot = depot_match.group(1).strip()
        depot_items = re.findall(r'\*\s*(.+)', depot)
        detail['initial_depot'] = depot_items
    note_lines = []
    for line in text.splitlines():
        if re.search(r'grade|curve', line, re.I):
            note_lines.append(line.strip())
    detail['grade_curve_notes'] = note_lines
    return detail
    # initial depot configuration and grade notes
    depot_match = re.search(r'==+\s*Initial Depot Configuration\s*==+(.*?)(?:==|$)', text, re.S | re.I)
    if depot_match:
        depot = depot_match.group(1).strip()
        depot_items = re.findall(r'\*\s*(.+)', depot)
        detail['initial_depot'] = depot_items
    # grade/curve-specific planning note
    note_lines = []
    for line in text.splitlines():
        if re.search(r'grade|curve', line, re.I):
            note_lines.append(line.strip())
    detail['grade_curve_notes'] = note_lines
    return detail


def parse_loco_page(title: str, text: str) -> dict:
    detail = {'title': title}
    info = parse_template('Loco info', text)
    if not info:
        info = parse_template('Loco_Info', text)
    detail.update({
        'name': info.get('title1', title).strip(),
        'weight': info.get('weight', '').strip(),
        'tractive_effort': info.get('tractive', '').strip(),
        'top_speed': info.get('speed', '').strip(),
        'coal_capacity': info.get('coal', '').strip(),
        'cost': info.get('cost', '').strip(),
    })
    return detail


def main():
    maps = []
    for title in MAP_TITLES:
        text = fetch_wikitext(title)
        maps.append(parse_map_page(title, text))

    locos = []
    for title in LOCO_TITLES:
        text = fetch_wikitext(title)
        locos.append(parse_loco_page(title, text))

    OUTPUT_DIR.mkdir(exist_ok=True)
    with open(OUTPUT_DIR / 'steam_steel_maps.json', 'w', encoding='utf-8') as f:
        json.dump({'maps': maps}, f, indent=2)
    with open(OUTPUT_DIR / 'steam_steel_locomotives.json', 'w', encoding='utf-8') as f:
        json.dump({'locomotives': locos}, f, indent=2)
    print(f'Wrote {OUTPUT_DIR / "steam_steel_maps.json"} and {OUTPUT_DIR / "steam_steel_locomotives.json"}')


if __name__ == '__main__':
    main()
