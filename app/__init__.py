from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.Config')
    
    db.init_app(app)
    
    from .routes import main_routes
    app.register_blueprint(main_routes)

    return app
