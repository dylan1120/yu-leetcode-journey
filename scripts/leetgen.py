import os
import argparse

README_TEMPLATE = """| 題號 | 題目名稱                             | 類別   | 難度  | Tags | 程式碼連結                                     |
|------|--------------------------------------|--------|--------|------|------------------------------------------------|
"""

ENTRY_TEMPLATE = "| {id} | [{title}]({url}) | {topic} | {level} | {tags} | [Code](./{topic_folder}/{filename}) |\n"

EXTENSIONS = {
    'python': '.py',
    'sql': '.sql',
    'java': '.java',
    'cpp': '.cpp',
    'c': '.c',
    'javascript': '.js',
    'go': '.go',
    'rust': '.rs',
    'txt': '.txt',  # fallback
}

PYTHON_TEST_TEMPLATE = """from {import_path} import Solution

def test():
    s = Solution()
    # TODO: Add test cases
    print('✅ Test template ready')

if __name__ == '__main__':
    test()
"""

SQL_TEST_TEMPLATE = """-- Test Case Template for LeetCode {id}: {title}
-- Schema and sample data for testing

-- CREATE TABLE Example (...);
-- INSERT INTO Example VALUES (...);

-- Test Query
-- SELECT * FROM Example;
"""


def format_filename(problem_id: int, title: str, ext: str) -> str:
    kebab_title = title.lower().replace(" ", "-").replace(",", "").replace("'", "")
    return f"{problem_id:04d}-{kebab_title}{ext}"


def generate_code_template(problem_id: int, title: str, url: str, lang: str) -> str:
    if lang == 'python':
        return f"""# LeetCode {problem_id}: {title}
# {url}

class Solution:
    def TODO(self):
        pass
"""
    elif lang == 'sql':
        return f"-- LeetCode {problem_id}: {title}\n-- {url}\n\n-- Your SQL here\n"
    else:
        return f"// LeetCode {problem_id}: {title}\n// {url}\n\n// Your {lang} solution here\n"


def read_existing_ids_from_all():
    ids = set()
    for lang in os.listdir():
        if os.path.isdir(lang) and os.path.exists(os.path.join(lang, "README.md")):
            with open(os.path.join(lang, "README.md"), 'r') as f:
                for line in f:
                    if line.startswith('|'):
                        parts = line.split('|')
                        if len(parts) > 1:
                            try:
                                ids.add(int(parts[1].strip()))
                            except ValueError:
                                continue
    return ids


def update_readme(readme_path: str, entry: str, problem_id: int):
    if not os.path.exists(readme_path):
        with open(readme_path, 'w') as f:
            f.write(README_TEMPLATE)

    with open(readme_path, 'r') as f:
        content = f.read()
        if f"| {problem_id} " in content:
            print(f"⚠️  Problem ID {problem_id} already exists in {readme_path}. Skipping entry.")
            return

    with open(readme_path, 'a') as f:
        f.write(entry)


def create_test_file(lang: str, test_dir: str, test_filename: str, import_path: str, problem_id: int, title: str):
    os.makedirs(test_dir, exist_ok=True)
    test_path = os.path.join(test_dir, test_filename)
    if os.path.exists(test_path):
        return
    if lang == 'python':
        with open(test_path, 'w') as f:
            f.write(PYTHON_TEST_TEMPLATE.format(import_path=import_path))
    elif lang == 'sql':
        with open(test_path, 'w') as f:
            f.write(SQL_TEST_TEMPLATE.format(id=problem_id, title=title))
    else:
        with open(test_path, 'w') as f:
            f.write(f"// TODO: Add test cases for LeetCode {problem_id}: {title}\n")


def main():
    parser = argparse.ArgumentParser(description="Create LeetCode solution scaffold.")
    parser.add_argument('--lang', required=True, help='Language (e.g., python, sql, cpp, java)')
    parser.add_argument('--id', type=int, required=True)
    parser.add_argument('--title', type=str, required=True)
    parser.add_argument('--level', type=str, required=True)
    parser.add_argument('--topic', type=str, required=True)
    parser.add_argument('--tags', type=str, default='')
    args = parser.parse_args()

    lang = args.lang.strip().lower()
    problem_id = args.id
    title = args.title.strip()
    topic = args.topic.strip().lower()
    level = args.level.capitalize()
    tags = args.tags.strip()

    topic_folder = os.path.join(lang, topic)
    os.makedirs(topic_folder, exist_ok=True)

    ext = EXTENSIONS.get(lang, '.txt')
    filename = format_filename(problem_id, title, ext=ext)
    filepath = os.path.join(topic_folder, filename)
    url = f"https://leetcode.com/problems/{title.lower().replace(' ', '-')}/"

    # Global ID check
    all_existing_ids = read_existing_ids_from_all()
    if problem_id in all_existing_ids:
        print(f"❌ Problem ID {problem_id} already exists in project (across all languages). Skipping operation.")
        return

    # Create code file
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            f.write(generate_code_template(problem_id, title, url, lang))
    else:
        print(f"⚠️  Code file already exists: {filepath}")

    # Create test file
    test_dir = os.path.join(lang, 'tests')
    test_filename = f"test_{filename}"
    import_path = f"{lang}.{topic}.{filename[:-len(ext)]}"
    create_test_file(lang, test_dir, test_filename, import_path, problem_id, title)

    # Update README
    readme_path = os.path.join(lang, 'README.md')
    entry = ENTRY_TEMPLATE.format(
        id=problem_id,
        title=title,
        url=url,
        topic=topic.capitalize(),
        level=level,
        tags=tags,
        topic_folder=topic,
        filename=filename
    )
    update_readme(readme_path, entry, problem_id)

    print(f"✅ Finished processing problem {problem_id}: {title} for language: {lang}")


if __name__ == '__main__':
    main()