from flask import Flask

from routes.auth import auth_bp
from routes.predict import predict_bp
from routes.history import history_bp

app = Flask(__name__)

app.register_blueprint(auth_bp)

app.register_blueprint(predict_bp)

app.register_blueprint(history_bp)


if __name__ == "__main__":
    app.run(debug=True)