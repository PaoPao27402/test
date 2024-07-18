from flask import Flask, render_template
from facades.vacations_facades import *
from facades.auth_facades import *
from facades.likes_facades import *
from views.home_view import home_blueprint
from views.about_view import about_blueprint
from views.api_view import api_blueprint
from views.vacations_view import vacation_blueprint
from views.auth_view import auth_blueprint
from logging import getLogger, ERROR
from utils.app_config import AppConfig
from utils.logger import *
from models.status_code_model import *

app = Flask(__name__)

app.secret_key = AppConfig.session_secret_key
app.register_blueprint(home_blueprint)
app.register_blueprint(about_blueprint)
app.register_blueprint(vacation_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(api_blueprint)

@app.errorhandler(404)
def page_not_found(error):
    Logger.log(str(error))
    return render_template("404.html")


@app.errorhandler(Exception)
def catch_all(error):
    Logger.log(str(error))
    return render_template('500.html', error=error)


getLogger("werkzeug").setLevel(ERROR)





