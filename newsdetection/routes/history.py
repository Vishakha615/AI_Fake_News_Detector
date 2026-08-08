from flask import Blueprint
from controllers.history_controller import history

history_bp = Blueprint("history", __name__, url_prefix="/history")

history_bp.route("/<int:user_id>", methods=["GET"])(history)