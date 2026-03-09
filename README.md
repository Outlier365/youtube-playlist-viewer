# 🎬 YouTube 播放清單影片擷取工具

這是一個使用 **Django** 開發的網站工具。  
使用者只需要貼上 **公開的 YouTube 播放清單網址**，系統就會自動擷取播放清單中的所有影片，並在網頁上以表格形式顯示影片資訊。

---

## 🚀 專案功能

- 輸入 YouTube 播放清單網址
- 自動擷取播放清單中的所有影片
- 顯示影片標題 (Title)
- 顯示影片網址 (URL)
- 表格化呈現影片資料
- 基本的網址格式驗證
- 使用 Session 暫存資料

---

## 🛠 技術架構

- Python
- Django
- YouTube Data API v3
- HTML
- Bootstrap
- Render（部署平台）

---

## 📌 使用方式

### 1️⃣ 輸入公開的播放清單網址

例如：
https://www.youtube.com/watch?v=e-ORhEE9VVg&list=PLplXQ2cg9B_qrCVd1J_iId5SvP8Kf_BfS

### 2️⃣ 系統會擷取播放清單內容

並顯示：

| 影片標題 | 影片網址 |
|--------|--------|
| Video Title | https://youtube.com/watch?v=xxx |
