import os
import re

def extract_entries(readme_path, lang):
    entries = []
    if not os.path.exists(readme_path):
        return entries
    with open(readme_path, 'r') as f:
        for line in f:
            if line.startswith('|') and 'Code' in line:
                parts = line.strip().split('|')
                if len(parts) >= 7:
                    id_ = parts[1].strip()
                    title = parts[2].strip()
                    topic = parts[3].strip()
                    level = parts[4].strip()
                    tags = parts[5].strip()
                    link = parts[6].strip()
                    entries.append((id_, title, lang.capitalize(), level, topic, tags, link))
    return entries

def parse_global_existing_entries(global_path):
    entries = {}
    if not os.path.exists(global_path):
        return entries
    with open(global_path, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith('|'):
            parts = line.strip().split('|')
            if len(parts) >= 7:
                try:
                    id_ = int(parts[1].strip())
                    entries[id_] = line
                except ValueError:
                    continue
    return entries

def update_global_readme():
    global_readme = 'global_readme.md'
    existing_map = parse_global_existing_entries(global_readme)

    for lang in os.listdir():
        readme_path = os.path.join(lang, 'README.md')
        if os.path.isdir(lang) and os.path.exists(readme_path):
            entries = extract_entries(readme_path, lang)
            for entry in entries:
                entry_id = int(entry[0])
                if entry_id not in existing_map:
                    new_line = f"| {entry[0]} | {entry[1]} | {entry[2]} | {entry[3]} | {entry[4]} | {entry[5]} | {entry[6]} |\n"
                    existing_map[entry_id] = new_line

    final_entries = [existing_map[k] for k in sorted(existing_map.keys())]

    with open(global_readme, 'r') as f:
        content = f.read()

    marker = '<!-- ADD_NEW_PROBLEM_HERE -->'
    if marker not in content:
        print("❌ Marker not found in global_readme.md")
        return

    before, _ = content.split(marker)
    new_content = before + marker + '\n' + ''.join(final_entries)

    with open(global_readme, 'w') as f:
        f.write(new_content)

    print("✅ global_readme.md updated: all existing + new entries preserved and deduplicated")

if __name__ == '__main__':
    update_global_readme()
