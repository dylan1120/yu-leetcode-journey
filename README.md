# yu-leetcode-journey
Yu’s personal LeetCode notebook — organized by topic, built for growth.

## 📄 Project Structure

The project is organized as follows:

```bash
leetcode/
├── python/             # Python solutions and topic classification
│   ├── string/
│   ├── array/
│   └── README.md        # Language-specific description
├── sql/                # SQL solutions and topic classification
│   ├── aggregation/
│   ├── joins/
│   └── README.md        # Language-specific description
├── global_readme.md     # A comprehensive overview of all problems and solutions
├── README.md            # Project overview, setup, and instructions
├── scripts/             # Python tools for automating tasks (e.g., problem creation, readme updates)
├── sh/                  # Shell tools for managing tasks
└── Makefile             # Optional, if needed to automate build/run tasks
```

## 🧑‍💻 Usage

To add a new problem solution:

```bash
bash sh/add_problem.sh
```

To update the global readme with the latest problems:

```bash
bash sh/update_readme.sh
```

To search for problems by tag, topic, or difficulty:

```bash
bash sh/search_problem.sh --tag <tag_name>
```

To push today's solved problems to GitHub:

```bash
bash sh/push_today.sh
```

## ✨ Features

- Multi-language solutions: Python, SQL, Java, etc.
- Organized by problem topics such as arrays, dynamic programming, etc.
- Automatic update of the global problem index in `global_readme.md`

## 📋 Tags

Problems are tagged with keywords to make searching easier. Some common tags include:
- `array`
- `dynamic programming`
- `graph`
- `string`
- `prefix`

Feel free to explore and contribute!

## 📄 License

This project is licensed under the MIT License.