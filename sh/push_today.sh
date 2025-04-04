#!/bin/bash

DRY_RUN=false
DATE_TAG=false

while [[ "$1" != "" ]]; do
  case $1 in
    --dry-run ) DRY_RUN=true ;;
    --with-date ) DATE_TAG=true ;;
  esac
  shift
done

# Step 0: 自動 add 所有變動
git add .

# Step 1: 找出 staged README 中的題目行
lines=$(git diff --cached --unified=0 | grep '^+| [0-9]' | sed 's/^+//')

if [ -z "$lines" ]; then
  echo "❌ 沒有偵測到任何新增或修改的題目紀錄。"
  exit 1
fi

# Step 2: 從每一行中抓出題號與題目名稱
problems=()
while read -r line; do
  name=$(echo "$line" | cut -d '|' -f3 | grep -oP '\[(.*?)\]' | sed 's/\[//;s/\]//')
  problems+=("$name")
done <<< "$lines"

# Step 3: 組成 commit message
count=${#problems[@]}
summary="feat: solved $count problem"
[ "$count" -gt 1 ] && summary="${summary}s"
list=" - [${problems[*]}]"

# Optional 日期前綴
if [ "$DATE_TAG" = true ]; then
  today=$(date +%Y-%m-%d)
  summary="[$today] $summary"
fi

commit_msg="$summary$list"

# Step 4: 顯示或執行
echo "📦 Commit message will be:"
echo "$commit_msg"

if [ "$DRY_RUN" = false ]; then
  echo "🚀 正在推送..."
  git commit -m "$commit_msg"
  git push
  echo "✅ 推送完成。已提交題目："
  for p in "${problems[@]}"; do
    echo "- $p"
  done
else
  echo "🧪 Dry run 模式結束，未進行實際提交。"
fi
