import uuid

from typing import Dict

from src.models.repositories.activities_repository import ActivitiesRepository

class ActivityCreator:
  def __init__(self, activities_repository: ActivitiesRepository) -> None:
    self.__activities_repository = activities_repository

  def create(self, body, trip_id) -> Dict:
    try:
      activity_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "title": body.get("title"),
        "occurs_at": body.get("occurs_at")
      }

      self.__activities_repository.registry_activity(activity_infos)

      return {
        "body": { "activity_id": activity_infos["id"] },
        "status_code": 201
      }

    except Exception as exception:
      return {
        "status_code": 400,
        "body": {
          "message": str(exception)
        }
      }