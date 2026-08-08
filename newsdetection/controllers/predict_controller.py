from flask import request, jsonify
from services.prediction_service import predict_news
from services.database_service import save_prediction , save_chat
from services.translation_service import translate_text
from services.preprocess import clean_text
from services.llm_service import explain_prediction

def predict_news1():

    data = request.get_json()

    user_id = data.get("user_id")
    title = data.get("title")
    news_text = data.get("news_text")
    language = data.get("language")

    if not user_id or not news_text:
        return jsonify({
            "status": False,
            "message": "User ID and News are required."
        }), 400

    if language.lower() == "marathi":
        translated_text = translate_text(news_text, "en")

    elif language.lower() == "hindi":
        translated_text = translate_text(news_text, "en")

    else:
        translated_text = news_text
        
    clean_text1 = clean_text(translated_text)   
        
    # Predict using ML Model
    prediction, confidence = predict_news(clean_text1)
    
    
    explanation = explain_prediction(
    news_text,
    prediction,
    confidence
    )

    
    
    # Save prediction into database
    save_prediction(
        user_id,
        title,
        news_text,
        language,
        prediction,
        confidence
    )
    
    save_chat(user_id,news_text,explanation)

    return jsonify({
        "status": True,
        "prediction": prediction,
        "confidence": confidence,
        "explanation": explanation
    }), 200