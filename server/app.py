from flask import Flask, request, jsonify, send_from_directory
import librosa
import numpy as np
import joblib
import os
import json
from datetime import datetime
from flask_cors import CORS

app = Flask(
    __name__,
    static_folder=os.path.join(os.path.dirname(__file__), "../frontend_static"),
    static_url_path="/"
)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "ML_Model", "genre_classifier.pkl")
model = joblib.load(MODEL_PATH)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
HISTORY_FILE = os.path.join(BASE_DIR, "prediction_history.json")

def save_prediction(filename, genre):
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                history = []

    new_entry = {
        "filename": filename,
        "genre": genre,
        "timestamp": datetime.now().isoformat()
    }

    history.append(new_entry)
    print("Saving to:", os.path.abspath(HISTORY_FILE))

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

    return new_entry


@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    filename = file.filename
    filepath = "temp.wav"
    file.save(filepath)

    try:
        y, sr = librosa.load(filepath, duration=30)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
        mfcc_mean = np.mean(mfcc.T, axis=0)

        prediction = model.predict([mfcc_mean])[0]
        os.remove(filepath)

        saved_entry = save_prediction(filename, prediction)
        return jsonify({"genre": prediction, "history": saved_entry})
    

    except Exception as e:
        if os.path.exists(filepath):
            os.remove(filepath)
        return jsonify({"error": str(e)}), 500



@app.route("/history", methods=["GET"])
def get_history():
    if not os.path.exists(HISTORY_FILE):
        return jsonify([])

    with open(HISTORY_FILE, "r") as f:
        try:
            history = json.load(f)
        except json.JSONDecodeError:
            history = []

    return jsonify(history)


@app.route("/clear_history", methods=["POST"])
def clear_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
    return jsonify({"message": "History cleared."}), 200

@app.route("/")
def serve_index():
    return app.send_static_file("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
