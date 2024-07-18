from flask import Blueprint, render_template, send_file, url_for, redirect, request
from facades.auth_facades import AuthFacade
from models.client_error import * 
auth_blueprint=Blueprint("auth_view", __name__)
from models.credential_model import *
from utils.logger import *



facade = AuthFacade() 

@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    try:
        if request.method == "GET": return render_template("register.html",active="register", user={})
        facade.register() 
        return redirect(url_for("home_view.home"))
    
    except ValidationError as err:
        return render_template("register.html", error = err.message, user=err.model)


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    try:
        if request.method == "GET": return render_template("login.html",credentials={}, active="login")
        facade.login() 
        return redirect(url_for("home_view.home"))
    
    except (ValidationError, AuthError) as err:
        Logger.log(err.message)
        return render_template("login.html", error = err.message, credentials = err.model)
    
@auth_blueprint.route("/logout")
def logout():
    facade.logout()
    return redirect(url_for("home_view.home"))