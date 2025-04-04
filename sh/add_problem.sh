
#!/bin/bash

# 使用 scripts 內的 leetgen.py
echo "🗣 題目語言 (e.g., python/sql/java):"
read lang
echo "🔢 題號 (e.g., 1768):"
read id
echo "📘 題目標題 (e.g., Merge Strings Alternately):"
read title
echo "🏷️ 難度 (Easy/Medium/Hard):"
read level
echo "📂 主題分類 (e.g., array/string/aggregation):"
read topic
echo "🔖 題目標籤 (用逗號分隔, optional):"
read tags

echo "🚀 建立題目中..."
python scripts/leetgen.py --lang "$lang" --id "$id" --title "$title" --level "$level" --topic "$topic" --tags "$tags"