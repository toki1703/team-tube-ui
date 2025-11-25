import sqlite3
import os

base_dir = "C:\\Users\\toki1703\\Downloads\\kadai1" #　ローカルでの実装 デプロイ先は'/content/drive/MyDrive/kadai1'
# video.db のパス
db_path = os.path.join(base_dir, "video.db")

conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute("SELECT * FROM videos")

for row in cur.fetchall():
    print(row)

conn.close()
