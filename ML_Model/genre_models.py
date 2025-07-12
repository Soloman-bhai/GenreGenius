import joblib

model = joblib.load("genre_classifier.pkl")

print("Genres the model knows:", model.classes_)
