from src.main.server.server import app
from src.models.settings.db_connection_handle import db_connection_handler

db_connection_handler.connect()

if __name__ == "__main__":
  db_connection_handler.connect()
  app.run(host="0.0.0.0", port=3333, debug=True)