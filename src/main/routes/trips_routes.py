from flask import jsonify, Blueprint, request

trips_routes_bp = Blueprint("trip_routes", __name__)

# Importação de Controllers
from src.controllers.trip_creator import TripsCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer

from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder

## Importação de Repositories
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository

# Importando gerente de conexões
from src.models.settings.db_connection_handle import db_connection_handler


@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
  conn = db_connection_handler.get_connection()
  trips_repository = TripsRepository(conn)
  emails_repository = EmailsToInviteRepository(conn)
  controller = TripsCreator(trips_repository, emails_repository)
  response = controller.create(request.json)

  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<trip_id>", methods=["GET"])
def find_trip_details(trip_id):
  conn = db_connection_handler.get_connection()
  trips_repository = TripsRepository(conn)
  controller = TripFinder(trips_repository)
  response = controller.find_trip_details(trip_id)

  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<trip_id>/confirm", methods=["GET"])
def confirm_trip(trip_id):
  conn = db_connection_handler.get_connection()
  trips_repository = TripsRepository(conn)
  controller = TripConfirmer(trips_repository)

  response = controller.confirm(trip_id)

  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<trip_id>/links", methods=["POST"])
def create_link(trip_id):
  conn = db_connection_handler.get_connection()
  links_repository = LinksRepository(conn)
  controller = LinkCreator(links_repository)

  response = controller.create(request.json, trip_id)

  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/links", methods=["GET"])
def find_trip_link(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkFinder(links_repository)

    response = controller.find(tripId)

    return jsonify(response["body"]), response["status_code"]