from src.connectors import sqlite_connector

class update_ddbb():
    def __init__(self) -> None:
        self.conn=sqlite_connector()
