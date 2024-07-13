import uuid
from typing import Dict

from src.models.repositories.links_repository import LinksRepository

class LinkCreator:
  def __init__(self, links_repository: LinksRepository) -> None:
    self.__links_repository = links_repository

  def create(self, body: Dict, trip_id: str) -> Dict:
    try:
      link_infos = {
        "id": str(uuid.uuid4()),
        **body,
        "trip_id": trip_id
      }
      self.__links_repository.registry_link(link_infos)
      return {
        "status_code": 201,
        "body": {
          "LinkId": link_infos["id"]
        }
      }
    except Exception as exception:
      return {
        "status_code": 400,
        "body": {
          "message": str(exception)
        }
      }