# 🎬 YouTube Playlist Viewer

A Django web application that extracts and displays videos from a public YouTube playlist.

Users can paste a YouTube playlist URL and instantly view all videos in a clean table.

---

## 🚀 Live Demo

(Coming soon – deployed on Render)

---

## 📌 Features

- Extract videos from a public YouTube playlist
- Display video title and video URL
- Simple and clean web interface
- Input validation for playlist URLs
- Session storage for playlist data

---

## 🛠 Tech Stack

- Python
- Django
- YouTube Data API v3
- HTML / Bootstrap
- Render (for deployment)

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Outlier365/youtube-playlist-viewer.git
cd youtube-playlist-viewer
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create `.env` file

Create a `.env` file in the project root:

```
SECRET_KEY=your_secret_key
YOUTUBE_API_KEY=your_youtube_api_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

---

### 5. Run migrations

```bash
python manage.py migrate
```

---

### 6. Run the server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000
```

---

## 📷 Example

Paste a YouTube playlist URL like:

```
https://www.youtube.com/playlist?list=XXXX
```

The application will display:

- Video title
- Video URL

---

## 📚 Future Improvements

- Export playlist to CSV
- Search and filter videos
- Import videos into user's playlist via OAuth
- Playlist statistics

---

## 👨‍💻 Author

Jerry Shen
