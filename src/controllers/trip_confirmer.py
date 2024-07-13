from typing import Dict
from src.models.repositories.trips_repository import TripsRepository


class TripConfirmer:
  def __init__(self, trips_repository: TripsRepository) -> None:
    self.__trips_repository = trips_repository

  def confirm(self, trip_id: str) -> Dict:
    try:
      self.__trips_repository.update_trip_status(trip_id)
      return {
        "status_code": 204,
        "body": None
      }
    except Exception as exception:
      return {
        "status_code": 404,
        "body": {
          "message": str(exception)
        }
      }