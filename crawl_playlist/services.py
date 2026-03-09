import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")


def get_youtube_service():
    return build("youtube", "v3", developerKey=YOUTUBE_API_KEY)


def get_playlist_videos(playlist_id):
    youtube = get_youtube_service()
    videos = []
    next_page_token = None

    try:
        while True:
            request = youtube.playlistItems().list(
                part="snippet",
                playlistId=playlist_id,
                maxResults=50,
                pageToken=next_page_token
            )
            response = request.execute()

            for item in response.get("items", []):
                snippet = item.get("snippet", {})
                resource = snippet.get("resourceId", {})

                video_id = resource.get("videoId")
                video_title = snippet.get("title")

                if not video_id or not video_title:
                    continue

                video_url = f"https://www.youtube.com/watch?v={video_id}"

                videos.append({
                    "title": video_title,
                    "url": video_url,
                })

            next_page_token = response.get("nextPageToken")
            if not next_page_token:
                break

    except HttpError as e:
        return {"success": False, "error": f"YouTube API 錯誤：{e}"}
    except Exception as e:
        return {"success": False, "error": f"發生錯誤：{e}"}

    return {"success": True, "videos": videos}