from flask import Flask, render_template, request, jsonify
import os
import sqlite3
# Google Drive 側のフォルダ指定
base_dir = "C:\\Users\\toki1703\\Downloads\\kadai1" #　ローカルでの実装 デプロイ先は'/content/drive/MyDrive/kadai1'
template_dir = os.path.join(base_dir, 'templates')
static_dir = os.path.join(base_dir, 'static')

# DBファイルのパスを base_dir へ従わせる
db_path = os.path.join(base_dir, "video.db")

def get_db():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

# ここまで

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# ルーティングの指定
# それぞれの設定に応じて変える

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/videos')
def api_videos():
    member = request.args.get("member")
    db = get_db()

    if member:
        rows = db.execute(
            "SELECT * FROM videos WHERE member = ?",
            (member,)
        ).fetchall()
    else:
        rows = db.execute("SELECT * FROM videos").fetchall()

    return jsonify([dict(r) for r in rows])

@app.route('/about')
def kadai():
    return render_template('about.html')

# サーバーの実行
if __name__ == '__main__':
    app.run(debug=True)
