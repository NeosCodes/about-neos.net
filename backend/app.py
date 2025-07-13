from spotify_service import get_access_token, get_now_playing, REFRESH_TOKEN
from workers import Response

async def on_request(request, env, ctx):
    if request.method == "GET" and request.path == "/now-playing":
        try:
            access_token = get_access_token(env.CLIENT_ID, env.CLIENT_SECRET, REFRESH_TOKEN)
            track_info = get_now_playing(access_token)
            return Response.json(track_info)
        except Exception as e:
            return Response.json({"error": str(e)}, status=500)
    return Response("Not found", status=404)