from flask import Blueprint,render_template, send_file, redirect, url_for, request, session
from flask import jsonify
from facades.vacations_facades import *
from utils.image_handler import *
from models.client_error import *
from facades.auth_facades import *
from models.role_model import *
from utils.logger import *
from logic.likes_logic import *
from logic.vacation_logic import *

vacation_blueprint = Blueprint("vacations_view", __name__)

facade = VacationFacade()
logic = LikesLogic()
auth_facade = AuthFacade()
logic_countries = VacationLogic()

@vacation_blueprint.route("/vacations")
def list():
    auth_facade.block_anonymous()
    all_vacations = facade.get_all_vacations()
    like_count = {vacation.vacations_ID: logic.count_likes_by_vacation(vacation.vacations_ID) for vacation in all_vacations}
    
    user_liked = {}
    if "current_user" in session:
        user_ID = session["current_user"]["user_ID"]
        user_liked = {vacation.vacations_ID: logic.like_exists(user_ID, vacation.vacations_ID) for vacation in all_vacations}
    
    return render_template("vacations.html", vacations=all_vacations, like_count=like_count, user_liked=user_liked, active="vacations")


@vacation_blueprint.route("/vacations/like/<int:vacations_ID>/<action>", methods=["GET"])
def like_unlike_vacation(vacations_ID, action):
    if "current_user" not in session:
        return jsonify(success=False, message="User not logged in"), 401

    user_ID = session["current_user"]["user_ID"]
    if action == 'like':
        if not logic.like_exists(user_ID, vacations_ID):
            logic.add_vacation_like(user_ID, vacations_ID)
            user_liked = True
            message = 'Vacation liked!'
        else:
            user_liked = True
            message = 'You have already liked this vacation.'
            
    elif action == 'unlike':
        if logic.like_exists(user_ID, vacations_ID):
            logic.delete_vacation_like(user_ID, vacations_ID)
            user_liked = False
            message = 'Vacation unliked.'
        else:
            user_liked = False
            message = 'You have not liked this vacation.'
    else:
        return jsonify(success=False, message="Invalid action"), 400

    like_count = logic.count_likes_by_vacation(vacations_ID)
    return jsonify(success=True, message=message, like_count=like_count, user_liked=user_liked)


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


@vacation_blueprint.route("/vacations/new", methods=["GET", "POST"])
def insert():
    try:
        auth_facade.block_anonymous()
        if request.method == "GET":
            all_countries = logic_countries.get_all_countries_order_by_name()
            return render_template("insert.html", vacation={}, countries=all_countries, active="new")
        
        country_ID = request.form.get('country_ID')
        vacation_description = request.form.get('vacation_description')
        start_vacation_date = request.form.get('start_vacation_date')
        end_vacation_date = request.form.get('end_vacation_date')
        price = request.form.get('price')
        vacation_pic_file = request.files.get('image')
        country_name = logic_countries.get_country_name(country_ID)

        facade.add_vacation(
            country_ID=country_ID,
            vacation_description=vacation_description,
            start_vacation_date=start_vacation_date,
            end_vacation_date=end_vacation_date,
            price=price,
            vacation_pic_filename=vacation_pic_file,
            country_name=country_name
        )
        return redirect(url_for("vacations_view.list"))

    except AuthError as err:
        return redirect(url_for("auth_view.login"), error=err.message, credentials={})
    except ValidationError as err:
        all_countries = logic_countries.get_all_countries_order_by_name()
        return render_template("insert.html", error=err.message, countries=all_countries)



@vacation_blueprint.route("/vacations/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    try:
        auth_facade.block_non_admin()
        if request.method == "GET":
            one_vacation = facade.get_one_vacation(id)
            return render_template("edit.html", vacation=one_vacation)

        if request.method == "POST":
            # Call the update method with the ID
            facade.update_vacation(id)
            return redirect(url_for("vacations_view.list"))

    except AuthError as err:
        all_vacations = facade.get_all_vacations()
        return render_template("vacations.html", error=err.message, vacations=all_vacations)

    except ValidationError as err:
        one_vacation = facade.get_one_vacation(id)
        return render_template("edit.html", vacation=one_vacation, error=err.message)


@vacation_blueprint.route("/vacation/delete/<int:id>", methods=['POST'])
def delete(id):
    try:
        auth_facade.block_non_admin()
        facade = VacationFacade()
        facade.delete_vacation(id)
        return redirect(url_for("vacations_view.list"))
    
    except AuthError as err:
        all_vacations = facade.get_all_vacations()
        return render_template("vacations.html", error=err.message, vacations=all_vacations)






# @product_blueprint.route("/products/save", methods =["POST"])
# def save():
#     facade = ProductsFacade()
#     facade.add_product()
#     return redirect(url_for("products_view.List"))

