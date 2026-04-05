import re, os

def get_keys(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return set(re.findall(r'\[\"(.*?)\"\]\s*=', f.read()))

def audit(file_name):
    base = r"E:\Turtle Wow\Interface\AddOns\Atlas-TW\Locales"
    en = os.path.join(base, "enUS", file_name)
    es = os.path.join(base, "esES", file_name)
    if not os.path.exists(es): return
    
    en_keys = get_keys(en)
    es_keys = get_keys(es)
    missing = sorted(list(en_keys - es_keys))
    
    print(f"--- {file_name} ---")
    for k in missing:
        print(f'    ["{k}"] = true,')

files = ["Bosses.lua", "Factions.lua", "ItemSets.lua", "MapData.lua", "Spells.lua", "Zones.lua"]
for f in files:
    audit(f)
