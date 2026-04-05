import re, os

def get_keys(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return re.findall(r'\[\"(.*?)\"\]\s*=', f.read())

def sync_file(file_name, translations={}):
    base = r"E:\Turtle Wow\Interface\AddOns\Atlas-TW\Locales"
    en_path = os.path.join(base, "enUS", file_name)
    es_path = os.path.join(base, "esES", file_name)
    
    if not os.path.exists(es_path): return
    
    en_keys = get_keys(en_path)
    es_keys = set(get_keys(es_path))
    
    missing = [k for k in en_keys if k not in es_keys]
    
    if not missing:
        print(f"Skipping {file_name}: No missing keys.")
        return

    with open(es_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Find the closing table bracket
    # We'll look for the last '})' and insert before it
    pos = content.rfind('})')
    if pos == -1:
        print(f"Error: Closing '}})' not in {file_name}")
        return

    # Add a comma to the last key if it's missing
    # We look backwards from pos
    before = content[:pos].rstrip()
    if before and before[-1] != ',':
        before += ','
    
    insertion = "\n    -- TW Additions (Synced)\n"
    for k in missing:
        val = translations.get(k, "true")
        if val == "true":
            insertion += f'    ["{k}"] = {val},\n'
        else:
            insertion += f'    ["{k}"] = "{val}",\n'
    
    new_content = before + "\n" + insertion + content[pos:]
    
    with open(es_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated {file_name}: Added {len(missing)} keys.")

# Boss Translations (Selection)
boss_translations = {
    "Ahgk'tos the Pure": "Ahgk'tos el Puro",
    "Ambassador Vortalus": "Embajador Vortalus",
    "Archdruid Kronn": "Archidruida Kronn",
    "Archlich Enkhraz": "Archiliche Enkhraz",
    "Battlemaster Ubukaz": "Maestro de batalla Ubukaz",
    "Bonespeaker Narlgom": "Hablahuesos Narlgom",
    "Broodcommander Axelus": "Comandante de la Prole Axelus",
    "Chieftaun Partath": "Jefe Partath",
    "Chieftain Shalk Blackwind": "Jefe Shalk Vientonegro",
    "Dagar the Glutton": "Dagar el Glotón",
    "Dark Reaver of Karazhan": "Segador Oscuro de Karazhan",
    "Duke Balor the IV": "Duque Balor IV",
    "Ezzel Darkbrewer": "Ezzel el Cervecero Oscuro",
    "Grand Elder Skystider": "Gran Sabio Caminalba",
    "Hailar The Frigid": "Hailar la Gélida",
    "Handler Oboka": "Adiestrador Oboka",
    "Juthza the Cunning": "Juthza la Astuta",
    "Kan'za The Seer": "Kan'za la Vidente",
    "Karrsh the Sentinel": "Karrsh el Centinela",
    "Kath'zen the Brutal": "Kath'zen el Brutal",
}

# Faction Translations
faction_translations = {
    "Draenei Exiles": "Exiliados Draenei",
    "Earthen Ring": "El Anillo de la Tierra",
}

# Zone Translations
zone_translations = {
    "Moonwhisper Coast": "Costa Susurro de Luna",
}

all_translations = {**boss_translations, **faction_translations, **zone_translations}

files = ["Bosses.lua", "Factions.lua", "ItemSets.lua", "MapData.lua", "Spells.lua", "Zones.lua"]
for f in files:
    sync_file(f, all_translations)
