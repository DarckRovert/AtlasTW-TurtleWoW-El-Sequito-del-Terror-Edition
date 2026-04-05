import re, os

def clean_quest_data():
    es_path = r"E:\Turtle Wow\Interface\AddOns\Atlas-TW\Locales\esES\QuestData.lua"
    if not os.path.exists(es_path): return
    
    with open(es_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Define the fragments to fix
    replacements = {
        'Aim = "Procure no Pântano por um dragão vermelho dispuesto a ouvir você."': 'Aim = "Busca en el Pantano un dragón rojo dispuesto a escucharte."',
        'Aim = "Procure no Pântano por um dragão rojo dispuesto a ouvir você."': 'Aim = "Busca en el Pantano un dragón rojo dispuesto a escucharte."',
    }

    modified = False
    for old, new in replacements.items():
        if old in content:
            content = content.replace(old, new)
            modified = True
            print(f"Fixed fragment: {old[:50]}...")

    if modified:
        with open(es_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated QuestData.lua with language fixes.")
    else:
        print("No Portuguese fragments found in QuestData.lua using direct matching.")

clean_quest_data()
