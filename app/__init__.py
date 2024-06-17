from flask import Flask
from app import api  # Importowanie widoków
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

from .views import views
from .auth import auth

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')

from .models import get_user_by_id

@login_manager.user_loader
def load_user(user_id):
    return get_user_by_id(user_id)
