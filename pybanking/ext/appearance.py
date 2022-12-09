from flask_assets import Bundle, Environment


def init_app(app):
    # thinking about using this for the css
    assets = Environment(app)

    css = Bundle('src/main.css', output='dist/main.css',
                 filters='postcss')

    assets.register('main_css', css)
