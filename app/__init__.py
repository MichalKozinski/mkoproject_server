# from flask import Flask
# from flask_login import LoginManager
# from .models import get_user_by_id, create_initial_admin
# from app import api  # Importowanie widoków

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'

# login_manager = LoginManager()
# login_manager.init_app(app)

# from .views import views
# from .auth import auth

# app.register_blueprint(views, url_prefix='/')
# app.register_blueprint(auth, url_prefix='/')

# @login_manager.user_loader
# def load_user(user_id):
#     return get_user_by_id(user_id)

# # Tworzenie początkowego administratora przy uruchomieniu aplikacji
# with app.app_context():
#     create_initial_admin()


from flask import Flask
from flask_login import LoginManager
from .models import get_user_by_id, create_initial_admin

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = b'\x8b\x9b\xa8_l\x08\xb0\x84\x0e\x8e\x01\xc0z/\x89\xce\x1dC\xcd\x06\xdd\xdd{\xf3'

    login_manager.init_app(app)

    from app.views import views
    from app.auth import auth
    from app.api import api

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(api, url_prefix='/api')

    @login_manager.user_loader
    def load_user(user_id):
        return get_user_by_id(user_id)

    with app.app_context():
        create_initial_admin()
    return app