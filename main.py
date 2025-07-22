from flask import Flask
from app.routes.Users import users_bp
from app.routes.Detection import detection_bp

def create_app():
    app = Flask(__name__)


    @app.route('/')
    def index():
        return {"message":"SmartServe API is running!"}

    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(detection_bp, url_prefix='/detection')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0',port=5050)
