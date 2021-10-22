from flask import Flask
from config import Config
from .authentication.routes import auth
from .api.routes import api
from .site.routes import site
from flask_migrate import Migrate
from .models import db, login_manager, ma
from flask_cors import CORS

# instantiating a new flask app
app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(auth)
app.register_blueprint(site)
app.register_blueprint(api)

db.init_app(app)

login_manager.init_app(app)
login_manager.login_view = 'auth.signin'

ma.init_app(app)

migrate = Migrate(app, db)

CORS(app)