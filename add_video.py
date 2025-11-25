import sqlite3
import os

base_dir = "C:\\Users\\toki1703\\Downloads\\kadai1" #　ローカルでの実装 デプロイ先は'/content/drive/MyDrive/kadai1'
# video.db のパス
db_path = os.path.join(base_dir, "video.db")

def add_video(url, title, artist, member):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO videos (url, title, artist, member)
        VALUES (?, ?, ?, ?)
    """, (url, title, artist, member))
    conn.commit()
    conn.close()

# 使用例
add_video(
    "https://www.youtube.com/watch?v=Soy4jGPHr3g",
    "テトリス",
    "柊マグネタイト",
    "toki"
)