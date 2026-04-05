import re, os

def clean_quest_data_regex():
    es_path = r"E:\Turtle Wow\Interface\AddOns\Atlas-TW\Locales\esES\QuestData.lua"
    if not os.path.exists(es_path): return
    
    with open(es_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Pattern for Portuguese line at 8514
    # Aim = "Procure no Pântano por um dragão vermelho dispuesto a ouvir você.",
    pattern = r'Aim\s*=\s*\"Procure\s+no\s+P\xe2ntano.*?voc\xea\.\",'
    # Let's be more generic to catch it even with weird encoding
    pattern_generic = r'Aim\s*=\s*\"Procure\s+no\s+.+?dispu?esto\s+a\s+ouvir\s+.+?\",'
    
    new_text = 'Aim = "Busca en el Pantano un dragón rojo dispuesto a escucharte.",'
    
    content, count = re.subn(pattern_generic, new_text, content, flags=re.IGNORECASE | re.UNICODE)
    
    if count > 0:
        with open(es_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {count} Portuguese fragments in QuestData.lua.")
    else:
        print("Regex didn't match any Portuguese fragments. Checking line 8514 manually.")
        lines = content.splitlines()
        if len(lines) >= 8514:
            print(f"Line 8514: {lines[8513]}")

clean_quest_data_regex()
