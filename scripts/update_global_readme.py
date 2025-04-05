import os

LANGUAGES = ["python", "sql", "java", "cpp", "go", "javascript"]
GLOBAL_README_PATH = "global_readme.md"
MARKER = "<!-- ADD_NEW_PROBLEM_HERE -->"

HEADER = """# 🧠 LeetCode Problem Archive

This is an auto-generated summary of all problems in this repository.

| 題號 | 題目名稱                             | 類別   | 難度  | Tags | 程式碼連結                                     |
|------|--------------------------------------|--------|--------|------|------------------------------------------------|
"""

def collect_all_entries():
    entries = {}
    for lang in LANGUAGES:
        readme_path = os.path.join(lang, "README.md")
        if not os.path.exists(readme_path):
            continue
        with open(readme_path, "r") as f:
            for line in f:
                if line.startswith("| ") and "[Code](./" in line:
                    try:
                        problem_id = int(line.split("|")[1].strip())
                        entries[problem_id] = line
                    except Exception:
                        continue
    return dict(sorted(entries.items()))

def update_global_readme():
    entries = collect_all_entries()
    entry_text = "".join(entries.values())

    if os.path.exists(GLOBAL_README_PATH):
        with open(GLOBAL_README_PATH, "r") as f:
            content = f.read()
        if MARKER in content:
            before, _ = content.split(MARKER, 1)
            new_content = before + MARKER + "\n\n" + HEADER + entry_text + "\n"
        else:
            new_content = HEADER + entry_text
    else:
        new_content = HEADER + entry_text

    with open(GLOBAL_README_PATH, "w") as f:
        f.write(new_content)
    print("✅ global_readme.md updated with", len(entries), "problems.")

if __name__ == "__main__":
    update_global_readme()