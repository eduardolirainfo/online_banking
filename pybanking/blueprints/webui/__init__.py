from flask import Blueprint

from .views import index, login_page, register_page, deposit_page, withdraw_page, transfer_page, history_page, logout_page

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/login/", methods=["GET", "POST"], view_func=login_page)
bp.add_url_rule("/register/", methods=["GET", "POST"], view_func=register_page)
bp.add_url_rule("/deposit/", methods=["GET", "POST"], view_func=deposit_page)
bp.add_url_rule("/withdraw/", methods=["GET", "POST"], view_func=withdraw_page)
bp.add_url_rule("/transfer/", view_func=transfer_page)
bp.add_url_rule("/history/", view_func=history_page)
bp.add_url_rule("/logout/", view_func=logout_page)


def init_app(app):
    app.register_blueprint(bp)
