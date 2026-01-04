# Google Cloud Run 部署教學系列

這是一個完整的 Google Cloud Run 部署教學系列，分為兩個專案，讓您循序漸進地學習雲端部署與 LINE Bot 整合。

## 📚 教學專案

### [專案一：Google Cloud Run 基礎部署](./Project1-BasicCloudRun/)

**學習目標：**
- 建立 Flask 應用程式
- Docker 容器化
- 部署到 Google Cloud Run
- 測試 REST API

**適合對象：** 初學者，想學習雲端部署的開發者

**預計時間：** 30-45 分鐘

---

### [專案二：LINE Bot 整合](./Project2-LINEBot/)

**學習目標：**
- LINE Messaging API 設定
- Webhook 接收與處理
- 訊息回覆功能
- LINE Bot 部署到 Cloud Run

**適合對象：** 完成專案一，想開發 LINE Bot 的開發者

**預計時間：** 45-60 分鐘

## 🎓 建議學習順序

1. **先完成專案一** - 熟悉 Cloud Run 部署流程
2. **測試部署成功** - 確保能正常訪問部署的服務
3. **再進行專案二** - 在專案一的基礎上加入 LINE Bot 功能

## 🛠️ 環境需求

- Python 3.9 或以上
- Google Cloud SDK
- Docker（選用，Cloud Build 會自動處理）
- LINE Developer 帳號（專案二需要）

## 📖 使用方式

### 克隆專案

```bash
git clone https://github.com/YourUsername/GoogleCloudRunDeploy.git
cd GoogleCloudRunDeploy
```

### 開始學習

```bash
# 進入專案一
cd Project1-BasicCloudRun
# 閱讀 README.md 開始學習

# 完成後進入專案二
cd ../Project2-LINEBot
# 閱讀 README.md 繼續學習
```

## 💡 學習建議

- **不要跳過專案一**：即使您熟悉 Flask，專案一的部署流程也是專案二的基礎
- **保留專案一的部署**：可以作為測試環境，確保部署流程沒問題
- **遇到問題先檢查日誌**：使用 `gcloud run services logs read` 查看錯誤訊息
- **善用 Issues**：遇到問題歡迎在 GitHub Issues 提問

## 🔗 相關資源

- [Google Cloud Run 官方文件](https://cloud.google.com/run/docs)
- [LINE Messaging API 文件](https://developers.line.biz/en/docs/messaging-api/)
- [Flask 官方文件](https://flask.palletsprojects.com/)

## 📝 專案結構

```
GoogleCloudRunDeploy/
├── README.md                          # 本文件（主目錄說明）
├── Project1-BasicCloudRun/           # 專案一：基礎部署
│   ├── README.md                     # 專案一教學文件
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .dockerignore
└── Project2-LINEBot/                 # 專案二：LINE Bot
    ├── README.md                     # 專案二教學文件
    ├── app.py
    ├── requirements.txt
    ├── Dockerfile
    ├── .dockerignore
    └── .env.example
```

## 🤝 貢獻

歡迎提出改進建議！您可以：
- 提交 Issue 回報問題
- 發送 Pull Request 改進教學內容
- 分享您的學習心得

## 📄 授權

MIT License - 歡迎自由使用與修改

## ✨ 致謝

感謝所有使用本教學的學習者，您的反饋讓教學更完善！

---

**準備好了嗎？** 👉 [開始專案一](./Project1-BasicCloudRun/README.md)