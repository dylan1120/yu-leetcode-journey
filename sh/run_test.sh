#!/bin/bash

lang=""
id=""

while [[ "$1" != "" ]]; do
  case $1 in
    --lang ) shift; lang="$1" ;;
    --id ) shift; id="$1" ;;
  esac
  shift
done

if [[ -z "$lang" || -z "$id" ]]; then
  echo "❌ 使用方式: bash run_test.sh --lang <python/sql> --id <problem_id>"
  exit 1
fi

echo "🧪 Debug: lang=$lang, id=$id"
filename=$(printf "%04d" "$id")

if [[ "$lang" == "python" ]]; then
  shopt -s nullglob
  test_path=(python/tests/test_${filename}_*.py)
  if [[ ! -f "${test_path[0]}" ]]; then
    echo "❌ 找不到測試檔案: python/tests/test_${filename}_*.py"
    exit 1
  fi
  echo "🚀 Running Python test: ${test_path[0]}"
  python3 "${test_path[0]}"
elif [[ "$lang" == "sql" ]]; then
  if [[ ! -f scripts/run_sql_test.py ]]; then
    echo "❌ 找不到 run_sql_test.py，請確認腳本存在於 scripts/。"
    exit 1
  fi

  echo "🚀 Running SQL test for problem $id"
  echo "📤 SQL 查詢執行結果："

  solution_path=(sql/*/${filename}_*.sql)
  test_path=(sql/tests/test_${filename}_*.sql)

  if [[ ! -f "${solution_path[0]}" ]]; then
    echo "❌ 找不到 SQL 題目檔案: sql/*/${filename}_*.sql"
    exit 1
  fi
  if [[ ! -f "${test_path[0]}" ]]; then
    echo "❌ 找不到 SQL 測試檔案: sql/tests/test_${filename}_*.sql"
    exit 1
  fi

  echo "📂 題目檔案: ${solution_path[0]}"
  echo "🧪 測試檔案: ${test_path[0]}"
  python3 scripts/run_sql_test.py --solution "${solution_path[0]}" --test "${test_path[0]}"
else
  echo "❌ Unsupported language: $lang"
  exit 1
fi
