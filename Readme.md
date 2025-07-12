🎵🎧 Welcome to GenreGenius – AI Music Genre Classifier 🎧🎵
==========================================================

🗂️ Project Structure:
---------------------
📁 Music-Genre/
├── ML_Model/
│   └── genre_classifier.pkl      ← Pretrained model file
├── frontend_static/
│   └── index.html, CSS, JS       ← Ready-to-use built React frontend
├── prediction_history.json       ← (auto-generated during use)
├── server/
│   └── app.py                    ← Flask backend
├── run_app.bat                   ← 🔁 Double-click to run everything!
└── requirements.txt              ← Python dependencies list

💡 Prerequisites:
-----------------
1. 🐍 Python 3.10+ installed (Download: https://www.python.org/)
2. Internet connection (for installing packages)

🚀 One-Time Setup (Only First Time After Unzipping):
----------------------------------------------------
📌 Run these in **Command Prompt (CMD)** inside the `Music-Genre` folder.

1️⃣ Create a virtual environment:
    ```bash
    python -m venv venv
    ```

2️⃣ Activate the virtual environment:
    ```bash
    venv\Scripts\activate
    ```

3️⃣ Install required libraries:
    ```bash
    pip install -r requirements.txt
    ```

✔️ Now you're all set!

📦 Daily Usage – Run the App Easily:
------------------------------------
✅ Every time you want to start the project:

📁 Go to the `Music-Genre` folder

🖱️ Double-click `run_app.bat`

This will:
- 🔄 Activate the virtual environment
- 🚀 Start the Flask server
- 🌐 Open your default browser at `http://127.0.0.1:5000/`

🎧 Upload any `.wav` file and it will predict the genre using AI!
Prediction history is stored in `prediction_history.json`.

🧹 Optional Tools:
------------------
- **Export History**: As CSV from the interface
- **Clear History**: Click 'Clear History' button on the page

📌 Notes:
---------
- Do **not delete**: `ML_Model`, `frontend_static`, or `run_app.bat`
- Keep all files in the **same folder structure**
- `.wav` files under 30 seconds work best for prediction

👋 Happy Music Classifying!
===========================

