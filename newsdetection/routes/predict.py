from flask import Blueprint
from controllers.predict_controller import predict_news1

predict_bp = Blueprint("predict", __name__, url_prefix="/predict")

predict_bp.route("/predict_news1", methods=["POST"])(predict_news1)