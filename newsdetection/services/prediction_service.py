import joblib

# Load model
model = joblib.load("models/fake_news_model.pkl")

# Load vectorizer
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")


def predict_news(news):

    vector = vectorizer.transform([news])

    prediction = model.predict(vector)[0]

    confidence = max(model.predict_proba(vector)[0])

    return prediction, round(confidence * 100, 2)