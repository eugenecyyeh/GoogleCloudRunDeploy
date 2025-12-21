# Google Cloud Run 部署教學

## 快速開始

### 1️⃣ 登入 Google Cloud
```bash
gcloud auth login
```

---

### 2️⃣ 列出你有權限的所有專案
（確認有哪些專案可以使用）
```bash
gcloud projects list
```

---

### 3️⃣ 查看目前使用中的專案
（⚠️ 非常重要，避免部署到錯的專案）
```bash
gcloud config get-value project
```

---

### 4️⃣ 設定 / 切換專案
```bash
gcloud config set project [YOUR_PROJECT_ID]
```

切換後請再次確認：
```bash
gcloud config get-value project
```

---

### 5️⃣ 部署到 Cloud Run
```bash
gcloud run deploy my-first-service --source .
```

部署成功後，終端機會顯示：
```
Service URL: https://xxxxx.a.run.app
```

---

## 🔍（選用）確認服務部署在哪個專案

```bash
gcloud run services list --region asia-east1
```

---

## 🧠 工程師小提醒

> 每次部署前，請務必先執行：
```bash
gcloud config get-value project
```

確認目前專案正確，再進行部署，避免誤部署到 production。
