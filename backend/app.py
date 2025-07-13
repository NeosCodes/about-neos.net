from flask import Flask, jsonify
from flask_cors import CORS
from spotify_service import get_access_token, get_now_playing, REFRESH_TOKEN

app = Flask(__name__)
CORS(app)

@app.route("/now-playing")
def now_playing():
    try:
        access_token = get_access_token(REFRESH_TOKEN)
        track_info = get_now_playing(access_token)
        return jsonify(track_info)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
