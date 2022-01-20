import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

logger = logging.getLogger('gunicorn.error')

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    if not app.debug and not app.testing:
        logger.info('Service starting up')

    with app.app_context():
        return app