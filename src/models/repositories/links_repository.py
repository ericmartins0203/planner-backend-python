from typing import Tuple, Dict, List
from sqlite3 import Connection

class LinksRepository:
  def __init__(self, conn: Connection) -> None:
    self.__conn  = conn

  def registry_link(self, Link_infos: Dict) -> None:
    cursor = self.__conn .cursor()
    cursor.execute(
      '''
        INSERT INTO links
            (id, trip_id, link, title)
        VALUES
            (?, ?, ?, ?)
      ''', (
        Link_infos["id"],
        Link_infos["trip_id"],
        Link_infos["link"],
        Link_infos["title"],
      )
    )
    self.__conn.commit()

  def find_links_from_trip(self, trip_id: str) -> List[Tuple]:
    cursor = self.__conn .cursor()
    cursor.execute(
      '''
        SELECT * FROM links
        WHERE trip_id = ?
      ''', (trip_id,)
    )
    return cursor.fetchall()
  
