import ollama


def explain_prediction(news, prediction, confidence):

    prompt = f"""
    You are an AI assistant for fake news detection.

    A Machine Learning model has already analyzed this news.

    Prediction: {prediction}
    Confidence: {confidence:.2f}%

    News:
    {news}

    Provide:
    1. Why the model predicted this label.
    2. Mention any trustworthy or suspicious indicators.
    3. Explain in simple language.
    4. Keep the response within 4-5 sentences.
    """

    response = ollama.chat(
        model="llama3.1",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]

