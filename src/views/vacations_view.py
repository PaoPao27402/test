from flask import Blueprint,render_template, send_file, redirect, url_for, request, session
from facades.vacations_facades import *
from utils.image_handler import *
from models.client_error import *
from facades.auth_facades import *
from models.role_model import *
from utils.logger import *

vacation_blueprint = Blueprint("vacations_view", __name__)

facade = VacationFacade()

auth_facade = AuthFacade()

@vacation_blueprint.route("/vacations")
def list():
    all_vacations = facade.get_all_vacations()
    # print(all_vacations)
    return render_template("vacations.html", vacations = all_vacations, active="vacations")

@vacation_blueprint.route("/vacations/details/<int:id>")
def details(id):
    try:
        one_vacation = facade.get_one_vacation(id)
        return render_template("details.html", vacation = one_vacation, current_user = session.get('current_user'), admin = RoleModel.Admin.value)
    
    except ResourceNotFoundError as err:
        Logger.log(err.message)
        return render_template("404.html", error = err.message)


@vacation_blueprint.route("/vacations/images/<string:image_name>")
def get_image(image_name):
    image_path = ImageHandler.get_image_path(image_name)
    return send_file(image_path)


@vacation_blueprint.route("/vacations/new", methods=["GET","POST"])
def insert():
    try:
        auth_facade.block_anonymous()
        if(request.method=="GET"): return render_template("insert.html",  active="new")
        facade.add_vacation()
        return redirect(url_for("vacations_view.list"))
    
    except AuthError as err:
        return redirect("auth_view.login", error = err.message, credentials = {})
    except ValidationError as err:
        return render_template("insert.html", error = err.message)


@vacation_blueprint.route("/vacations/edit/<int:id>", methods=["GET", "POST"])
def edit(id): 
    try:
      auth_facade.block_non_admin()
      if(request.method=="GET"):
        one_vacation = facade.get_one_vacation(id)
        return render_template("edit.html", vacation = one_vacation)
      facade.update_vacation()
      return redirect(url_for("vacations_view.list"))
     
    except AuthError as err:
        all_vacations = facade.get_all_vacations()
        return render_template("vacations.html", error = err.message, vacations = all_vacations)
    
    except ValidationError as err:
        return render_template("edit.html", err=err.message)


@vacation_blueprint.route("/vacation/delete/<int:id>")
def delete(id):
    try:
        auth_facade.block_non_admin()
        facade = VacationFacade()
        facade.delete_vacation(id)
        return redirect(url_for("vacations_view.list"))
    
    except AuthError as err:
        all_vacations = facade.get_all_vacations()
        return render_template("vacations.html", error = err.message,  vacations = all_vacations )





# @product_blueprint.route("/products/save", methods =["POST"])
# def save():
#     facade = ProductsFacade()
#     facade.add_product()
#     return redirect(url_for("products_view.List"))

