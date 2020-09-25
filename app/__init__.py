from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail

from config import Config

app = Flask(__name__)
db = SQLAlchemy()
login_manager = LoginManager(app)
bootstrap = Bootstrap(app)
mail = Mail(app)
login_manager.login_view = 'logup.login'
login_manager.session_protection = 'strong'


def create_app():
    app.config.from_object(Config)
    from .logup import logup as logup_blueprint
    from .main import main as main_blueprint
    app.register_blueprint(logup_blueprint)
    app.register_blueprint(main_blueprint)
    db.init_app(app)
    return app
