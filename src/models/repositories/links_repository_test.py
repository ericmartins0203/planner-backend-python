import uuid
import pytest

from src.models.settings.db_connection_handle import db_connection_handler
from .links_repository import LinksRepository


db_connection_handler.connect()
link_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="Interaction with bank")
def test_registry_email() -> None:
  conn = db_connection_handler.get_connection()
  link_repository = LinksRepository(conn)

  link_infos = {
    "id": link_id,
    "trip_id": trip_id,
    "link": "https://www.google.com",
    "title": "Google",
  }

  link_repository.registry_link(link_infos)

@pytest.mark.skip(reason="Interaction with bank")
def test_find_links_from_trip():
  conn = db_connection_handler.get_connection()
  link_repository = LinksRepository(conn)

  links = link_repository.find_links_from_trip(trip_id)

  print(links)

  assert isinstance(links, list)
  assert isinstance(links[0], tuple)

