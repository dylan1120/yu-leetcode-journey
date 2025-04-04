import os
import argparse
import re

def parse_global_readme():
    entries = []
    path = 'global_readme.md'
    if not os.path.exists(path):
        return []

    with open(path, 'r') as f:
        for line in f:
            if line.startswith('|') and 'Code' in line:
                parts = line.strip().split('|')
                if len(parts) >= 7:
                    entries.append({
                        'id': parts[1].strip(),
                        'title': parts[2].strip(),
                        'lang': parts[3].strip(),
                        'level': parts[4].strip(),
                        'topic': parts[5].strip(),
                        'tags': parts[6].strip(),
                        'link': parts[7].strip()
                    })
    return entries

def search_entries(entries, lang=None, topic=None, level=None, tag=None):
    result = []
    for entry in entries:
        if lang and lang.lower() != entry['lang'].lower():
            continue
        if topic and topic.lower() not in entry['topic'].lower():
            continue
        if level and level.lower() != entry['level'].lower():
            continue
        if tag and tag.lower() not in entry['tags'].lower():
            continue
        result.append(entry)
    return result

def main():
    parser = argparse.ArgumentParser(description='Search problems from global_readme.md')
    parser.add_argument('--lang', type=str, help='Language (e.g., Python)')
    parser.add_argument('--topic', type=str, help='Topic (e.g., array)')
    parser.add_argument('--level', type=str, help='Difficulty level (e.g., Easy)')
    parser.add_argument('--tag', type=str, help='Tag keyword (e.g., prefix)')
    args = parser.parse_args()

    entries = parse_global_readme()
    filtered = search_entries(entries, args.lang, args.topic, args.level, args.tag)

    print(f"\n🔍 Found {len(filtered)} result(s):\n")
    for e in filtered:
        print(f"[{e['id']}] {e['title']} | {e['lang']} | {e['level']} | {e['topic']} | Tags: {e['tags']}\n  ↳ {e['link']}")

if __name__ == '__main__':
    main()