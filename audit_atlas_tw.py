import os
import re

def audit_atlas_tw():
    base_path = r"E:\Turtle Wow\Interface\AddOns\Atlas-TW\Locales"
    en_path = os.path.join(base_path, "enUS")
    es_path = os.path.join(base_path, "esES")
    
    files = ["Bosses.lua", "Classes.lua", "Core.lua", "Factions.lua", "ItemSets.lua", "MapData.lua", "QuestData.lua", "Spells.lua", "Zones.lua"]
    
    results = {}
    
    for file in files:
        en_file = os.path.join(en_path, file)
        es_file = os.path.join(es_path, file)
        
        if not os.path.exists(en_file):
            continue
            
        with open(en_file, "r", encoding="utf-8", errors="ignore") as f:
            en_content = f.read()
            
        with open(es_file, "r", encoding="utf-8", errors="ignore") as f:
            es_content = f.read()
            
        # Extract keys using a simple regex for ["key"] = ...
        keys = re.findall(r'\["(.*?)"\]\s*=', en_content)
        es_keys = re.findall(r'\["(.*?)"\]\s*=', es_content)
        
        missing = [k for k in keys if k not in es_keys]
        results[file] = {
            "total_en": len(keys),
            "total_es": len(es_keys),
            "missing": missing
        }
        
    for file, data in results.items():
        print(f"File: {file}")
        print(f"  EN Keys: {data['total_en']}")
        print(f"  ES Keys: {data['total_es']}")
        print(f"  Missing in ES: {len(data['missing'])}")
        if data['missing']:
            print(f"  Sample missing: {data['missing'][:5]}")
        print("-" * 20)

if __name__ == "__main__":
    audit_atlas_tw()
