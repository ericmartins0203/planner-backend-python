import uuid

from typing import Dict
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository

class TripsCreator:
  def __init__(self, trips_repository: TripsRepository, emails_repository: EmailsToInviteRepository) -> None:
    self.__trips_repository = trips_repository
    self.__emails_repository = emails_repository

  def create(self, body) -> Dict:
    try:
      emails = body.get("emails_to_invite")
      trip_id = str(uuid.uuid4())

      trip_infos = {
        "id": trip_id,
        **body
      }

      self.__trips_repository.create_trip(trip_infos)

      if emails:
        for email in emails:
          emails_trips_infos = {
            "id": str(uuid.uuid4()),
            "trip_id": trip_id,
            "email": email
          }
          self.__emails_repository.registry_email(emails_trips_infos)

      return { 
        "body": {'id': trip_id }, 
        'status_code': 201 
      }
    
    except Exception as exception:
      return {
        "body": {
          "message": str(exception)
        },
        "status_code": 400
      } 