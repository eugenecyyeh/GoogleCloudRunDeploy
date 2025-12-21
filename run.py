import os

# 定義檔案內容
files = {
    "main.py": """from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Cloud Run! 部署成功！"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
""",
    
    "requirements.txt": """Flask==3.0.0
gunicorn==21.2.0
""",

    "Dockerfile": """FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 main:app
""",

    "README.md": """# Google Cloud Run 部署教學

## 快速開始

1. 登入 Google Cloud:
   gcloud auth login

2. 設定專案:
   gcloud config set project [YOUR_PROJECT_ID]

3. 部署:
   gcloud run deploy my-first-service --source .
"""
}

def create_files():
    # 建立部署用的程式檔案
    print("正在建立專案檔案...")
    for filename, content in files.items():
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ 已建立: {filename}")
    
    print("\n所有檔案已準備完成！")
    print("現在您可以依照 README.md 的指示進行部署，")
    print("或是打開 presentation.html 觀看簡報。")

if __name__ == "__main__":
    create_files()