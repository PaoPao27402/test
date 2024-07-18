from flask import Blueprint, jsonify, render_template, send_file, redirect, url_for, request, session, make_response
from facades.vacations_facades import *
from utils.image_handler import *
from models.client_error import *
from facades.auth_facades import *
from models.role_model import *
from utils.logger import *
from models.status_code_model import *

api_blueprint = Blueprint("api_view", __name__)

vacation_facade = VacationFacade()

@api_blueprint.route("/api/vacations")
def vacations():
    vacations = vacation_facade.get_all_vacations()
    return jsonify(vacations)


@api_blueprint.route("/api/vacation/<int:vacations_ID>")
def vacation(vacations_ID):
    try:
        vacation = vacation_facade.get_one_vacation(vacations_ID)
        return jsonify(vacation)
    
    except ResourceNotFoundError as err:
        Logger.log(err.message)
        json = jsonify({"error":err.message})
        return make_response(json, StatusCode.NotFound.value) 
    
