from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Mr. Whites secret key: key'

    from .views import views
    from .auth import auth

    # The slash means no prefix, prefix /luuk/ would give for example www.website.com/luuk/partofsite/
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
