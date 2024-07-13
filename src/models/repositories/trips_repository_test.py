import uuid
import pytest

from datetime import datetime, timedelta
from .trips_repository import TripsRepository
from src.models.settings.db_connection_handle import db_coonection_handler


db_coonection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="Interaction with bank")
def test_create_trip() -> None:
  conn = db_coonection_handler.get_connection()
  trips_repository = TripsRepository(conn)

  trips_infos = {
    "id": str(uuid.uuid4()),
    "destination": "Brazil",
    "start_date": datetime.strptime("01-01-2024", "%d-%m-%Y"),
    "end_date": datetime.strptime("01-01-2024", "%d-%m-%Y") + timedelta(days=5),
    "owner_name": "John",
    "owner_email": "john@example.com",
  }

  trips_repository.create_trip(trips_infos)

@pytest.mark.skip(reason="Interaction with bank")
def test_find_trip_by_id() -> None:
  conn = db_coonection_handler.get_connection()
  trips_repository = TripsRepository(conn)

  trip = trips_repository.get_trip_by_id(trip_id)

  print(trip)

@pytest.mark.skip(reason="Interaction with bank")
def test_update_trip_status() -> None:
  conn = db_coonection_handler.get_connection()
  trips_repository = TripsRepository(conn)

  trip = trips_repository.update_trip_status(trip_id)
