from typing import Dict
from src.models.repositories.participants_repository import ParticipantsRepository


class ParticipantConfirmer:
  def __init__(self, participants_repository: ParticipantsRepository) -> None:
    self.__participants_repository = participants_repository

  def confirm(self, trip_id: str) -> Dict:
    try:
      self.__participants_repository.update_participant_status(trip_id)
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