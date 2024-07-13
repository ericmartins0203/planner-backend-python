from typing import Dict

from src.models.repositories.trips_repository import TripsRepository


class TripFinder:
  def __init__(self, trips_repository: TripsRepository) -> None:
    self.__trips_repository = trips_repository

  def find_trip_details(self, trip_id: str) -> Dict:
    try:
      trip = self.__trips_repository.get_trip_by_id(trip_id)

      if not trip: raise Exception("Trip not found")

      return {
        "status_code": 200,
        "body": {
          "trip": {
            "id": trip[0],
            "destination": trip[1],
            "starts_at": trip[2],
            "ends_at": trip[3],
            "status": trip[6]
          }
        }
      }
    except Exception as exception:
      return {
        "status_code": 404,
        "body": {
          "message": str(exception)
        }
      }