from flask import jsonify
from services.database_service import get_history


def history(user_id):

    history_data = get_history(user_id)

    if history_data:

        return jsonify({
            "status": True,
            "history": history_data
        }), 200

    return jsonify({
        "status": False,
        "message": "No prediction history found."
    }), 404