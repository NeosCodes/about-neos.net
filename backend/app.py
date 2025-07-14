from flask import Flask, jsonify
from spotify_service import get_access_token, get_now_playing, REFRESH_TOKEN

app = Flask(__name__)

@app.route("/now-playing", methods=["GET"])
def now_playing():
    try:
        access_token = get_access_token()
        track_info = get_now_playing(access_token)
        return jsonify(track_info)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)