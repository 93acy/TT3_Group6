from flask import Blueprint
from flask_restx import Api

from config import Config

bp = Blueprint('main', __name__)
api = Api(
    bp,
    version=Config.VERSION,
    title=Config.APP_NAME,
    description=''
)

from app.main import routes


@bp.after_request
def corsify(response):
    headers = response.headers
    headers['Access-Control-Allow-Origin'] = '*'
    return response