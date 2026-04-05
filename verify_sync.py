import re, os

def get_keys(path):
    if not os.path.exists(path): return set()
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return set(re.findall(r'\[\"(.*?)\"\]\s*=', f.read()))

def audit():
    base = r"E:\Turtle Wow\Interface\AddOns\Atlas-TW\Locales"
    files = ["Bosses.lua", "Factions.lua", "ItemSets.lua", "MapData.lua", "Spells.lua", "Zones.lua"]
    
    results = []
    for f in files:
        en = os.path.join(base, "enUS", f)
        es = os.path.join(base, "esES", f)
        
        en_keys = get_keys(en)
        es_keys = get_keys(es)
        
        missing = en_keys - es_keys
        results.append(f"{f} | enUS: {len(en_keys)} | esES: {len(es_keys)} | Missing: {len(missing)}")
    
    return "\n".join(results)

print(audit())
