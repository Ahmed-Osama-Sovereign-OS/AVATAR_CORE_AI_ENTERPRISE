from flask import Flask, request, jsonify, send_from_directory
from core_brain import brain
from tts_stt import speak
from dashboard import log_message, get_report

app = Flask(__name__, static_folder=".")

@app.route("/")
def ui():
    return send_from_directory(".", "ui.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")
    reply = brain(message)
    log_message("user")
    speak(reply)
    return jsonify({"reply": reply})

@app.route("/dashboard", methods=["GET"])
def dashboard():
    return jsonify(get_report())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
