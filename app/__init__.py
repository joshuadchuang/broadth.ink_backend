from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config
from authlib.integrations.flask_client import OAuth

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    db.init_app(app)

    # Register blueprints
    from .routes import main as main_routes
    app.register_blueprint(main_routes)

    # TODO - Authorize users
    oauth = OAuth(app)
    google = oauth.register(
        name='google',
        client_id='your_google_client_id',
        client_secret='your_google_client_secret',
        access_token_url='https://accounts.google.com/o/oauth2/token',
        access_token_params=None,
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        authorize_params=None,
        api_base_url='https://www.googleapis.com/oauth2/v1/',
        client_kwargs={'scope': 'openid profile email'},
    )

    return app
