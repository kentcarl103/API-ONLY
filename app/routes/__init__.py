from .Users import users_bp
from .Detection import detection_bp

def register_blueprints(app):
    app.register_blueprint(users_bp)
    app.register_blueprint(detection_bp)
