
from src.connectors.sqlite_connector import sqlite_connector

def update_ddbb_execute():
    conn=sqlite_connector("tienda_online.db")
    print(1)

if __name__ == "__main__":
    update_ddbb_execute()
    