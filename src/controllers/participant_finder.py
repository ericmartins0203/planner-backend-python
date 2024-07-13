from typing import Dict

class ParticipantsFinder:
  def __init__(self, participants_repository) -> None:
    self.__participants_repository = participants_repository

  def find(self, tripId: str) -> Dict:
    try:
      participants = self.__participants_repository.find_participants_from_trip(tripId)

      formatted_participants = []
      for participant in participants:
        formatted_participants.append({
          "id": participant[0],
          "name": participant[1],
          "is_confirmed": participant[2],
          "email": participant[3]
        })

      return {
        "body": { "participants": formatted_participants },
        "status_code": 200
      } 
    
    except Exception as exception:
      return {
        "body": { "error": "Bad Request", "message": str(exception) },
        "status_code": 400
      }