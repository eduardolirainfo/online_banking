from flask import Blueprint

from .views import index, login_page

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/login/", view_func=login_page)


def init_app(app):
    app.register_blueprint(bp)
