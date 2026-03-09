from django.shortcuts import render
from .forms import PlaylistForm
from .services import get_playlist_videos


def home(request):
    message = ""
    videos = request.session.get("videos", [])

    if request.method == "POST":
        form = PlaylistForm(request.POST)

        if form.is_valid():
            playlist_id = form.get_playlist_id()
            result = get_playlist_videos(playlist_id)

            if result["success"]:
                videos = result["videos"]
                request.session["videos"] = videos
                request.session.set_expiry(300)   # 5分鐘後過期
                message = f"成功載入 {len(videos)} 筆資料。"
            else:
                message = result["error"]
    else:
        form = PlaylistForm()

    return render(request, "home.html", {
        "form": form,
        "message": message,
        "videos": videos,
    })