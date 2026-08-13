from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Soccer Video AI backend is running"})

@app.route("/process-video", methods=["POST"])
def process_video():
    video_key = next(
    (key for key in request.files.keys() if key.strip() == "video"),
    None
)

if video_key is None:
    return jsonify({
        "error": "No video uploaded",
        "files_received": [repr(k) for k in request.files.keys()],
        "form_received": list(request.form.keys()),
        "content_type": request.content_type
    }), 400

video = request.files[video_key]

    return jsonify({
        "success": True,
        "message": "Video received successfully",
        "filename": video.filename
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
