import re, os

def count_keys(path):
    if not os.path.exists(path): return 0
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        return len(re.findall(r'\[\"(.*?)\"\]\s*=', content))

base = r"E:\Turtle Wow\Interface\AddOns\Atlas-TW\Locales"
en_path = os.path.join(base, "enUS", "Bosses.lua")
es_path = os.path.join(base, "esES", "Bosses.lua")

print(f"enUS: {count_keys(en_path)}")
print(f"esES: {count_keys(es_path)}")
