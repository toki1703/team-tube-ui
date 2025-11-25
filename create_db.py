import sqlite3
import os

base_dir = "C:\\Users\\toki1703\\Downloads\\kadai1" #　ローカルでの実装 デプロイ先は'/content/drive/MyDrive/kadai1'
# video.db のパス
db_path = os.path.join(base_dir, "video.db")

# ディレクトリ確認（なければ作る）
os.makedirs(base_dir, exist_ok=True)

# DB 作成 & 接続
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# テーブル作成
cur.execute("""
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    title TEXT NOT NULL,
    artist TEXT NOT NULL,
    member TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("✓ SQLite データベースと videos テーブルを作成しました！")
print("場所:", db_path)
