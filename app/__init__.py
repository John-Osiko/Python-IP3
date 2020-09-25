from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail

from config import config_options

db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap()
mail = Mail()
login_manager.login_view = 'logup.login'
login_manager.session_protection = 'strong'


def create_app(config_name):
    app = Flask(__name__)
    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    from .logup import logup as logup_blueprint
    from .main import main as main_blueprint

    # Will add authentication views
    app.register_blueprint(logup_blueprint)
    # Will add the views and forms
    app.register_blueprint(main_blueprint)
    # Initialized application
    db.init_app(app)
    # Initialized login manager
    login_manager.init_app(app)
    # Initialized flask mail
    mail.init_app(app)
    
    return app
