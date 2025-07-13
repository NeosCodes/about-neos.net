import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')

def get_access_token(refresh_token: str) -> str:
    auth_str = f"{CLIENT_ID}:{CLIENT_SECRET}"
    b64_auth = base64.b64encode(auth_str.encode()).decode()

    headers = {
        "Authorization": f"Basic {b64_auth}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
    response.raise_for_status()
    return response.json().get("access_token")

def get_now_playing(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get("https://api.spotify.com/v1/me/player/currently-playing", headers=headers)
    if response.status_code != 200 or not response.json():
        return {"title": "---", "artist": "---", "progress_ms": 0, "duration_ms": 0, "cover": ""}
    data = response.json()
    item = data.get("item")
    if not item:
        return {"title": "---", "artist": "---", "progress_ms": 0, "duration_ms": 0, "cover": ""}
    title = item["name"]
    artist = ", ".join([a["name"] for a in item["artists"]])
    progress_ms = data.get("progress_ms", 0)
    duration_ms = item.get("duration_ms", 0)
    cover = ""
    if "album" in item and "images" in item["album"] and item["album"]["images"]:
        cover = item["album"]["images"][0]["url"]
    return {
        "title": title,
        "artist": artist,
        "progress_ms": progress_ms,
        "duration_ms": duration_ms,
        "cover": cover
    }