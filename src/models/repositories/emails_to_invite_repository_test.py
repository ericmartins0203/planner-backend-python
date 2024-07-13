import uuid
import pytest

from src.models.settings.db_connection_handle import db_connection_handler
from .emails_to_invite_repository import EmailsToInviteRepository


db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="Interaction with bank")
def test_registry_email() -> None:
  conn = db_connection_handler.get_connection()
  emails_to_invite_repository = EmailsToInviteRepository(conn)

  emails_trips_infos = {
    "id": str(uuid.uuid4()),
    "trip_id": trip_id,
    "email": "johnDoe@example.com",
  }

  emails_to_invite_repository.registry_email(emails_trips_infos)

@pytest.mark.skip(reason="Interaction with bank")
def test_find_emails_from_trip():
  conn = db_connection_handler.get_connection()
  emails_to_invite_repository = EmailsToInviteRepository(conn)

  emails = emails_to_invite_repository.find_emails_from_trip(trip_id)

  print(emails)

