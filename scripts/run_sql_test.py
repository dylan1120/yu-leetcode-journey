import sqlite3
from pathlib import Path
import sys
import argparse

def run_sql_test(solution_path: str, test_path: str):
    solution_file = Path(solution_path)
    test_file = Path(test_path)

    if not solution_file.exists():
        print(f"❌ 找不到題目 SQL 檔案：{solution_file}")
        return
    if not test_file.exists():
        print(f"❌ 找不到測試 SQL 檔案：{test_file}")
        return

    print(f"📂 初始化測試資料：{test_file}")
    print(f"🚀 執行題目查詢：{solution_file}\n")

    with open(test_file, "r") as f:
        test_sql = f.read()
    with open(solution_file, "r") as f:
        solution_sql = f.read()

    try:
        with sqlite3.connect(":memory:") as conn:
            cursor = conn.cursor()
            cursor.executescript(test_sql)

            # 過濾所有註解行 '--' 並取得查詢語句
            clean_lines = [line for line in solution_sql.splitlines() if not line.strip().startswith("--")]
            last_select = "\n".join(clean_lines).strip()

            print("📄 擷取到的 SELECT 查詢內容：\n" + last_select)

            cursor.execute(last_select)
            cols = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            print(" | ".join(cols))
            for row in rows:
                print(" | ".join(str(col) for col in row))
            return rows

    except Exception as e:
        print(f"❌ 執行失敗：{e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--solution", required=True, help="題目 SQL 檔案路徑")
    parser.add_argument("--test", required=True, help="測試 SQL 檔案路徑")
    args = parser.parse_args()

    run_sql_test(args.solution, args.test)
