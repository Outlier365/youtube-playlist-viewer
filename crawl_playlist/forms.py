from django import forms
from urllib.parse import urlparse, parse_qs


class PlaylistForm(forms.Form):
    playlist_url = forms.URLField(
        label="YouTube 播放清單網址",
        max_length=500,
        error_messages={
            "required": "請輸入 YouTube 播放清單網址",
            "invalid": "請輸入有效的網址格式",
        }
    )

    def clean_playlist_url(self):
        url = self.cleaned_data["playlist_url"].strip()

        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)

        if parsed_url.netloc not in ["www.youtube.com", "youtube.com"]:
            raise forms.ValidationError("請輸入正確的 YouTube 播放清單網址")

        # if parsed_url.path != "/playlist":
        #     raise forms.ValidationError("這不是 YouTube 播放清單網址")

        playlist_ids = query_params.get("list")
        if not playlist_ids or not playlist_ids[0]:
            raise forms.ValidationError("網址中找不到播放清單 ID（list 參數）")

        return url

    def get_playlist_id(self):
        url = self.cleaned_data["playlist_url"].strip()
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        return query_params["list"][0]