from flask import Flask
from app.routes import main_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    app.register_blueprint(main_routes)

    return app
