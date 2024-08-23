import unittest
from datetime import datetime
import pandas as pd
from src.connectors.sqlite_connector import sqlite_connector
from src.update_ddbb_task import execute  

class TestUpdateJamones(unittest.TestCase):

    def setUp(self):
        self.conector = sqlite_connector(database_name='tienda_online.db')

    def tearDown(self):
        self.conector.close()

    def test_update_jamones(self):
        execute(database_name='tienda_online.db')
        
        query = "SELECT DATE(update_date) as update_date FROM productos"
        df = self.conector.get_df(query)
        
        today_date = datetime.now().strftime('%Y-%m-%d')
        for _, row in df.iterrows():
            update_date = row['update_date']
            self.assertEqual(update_date,today_date)

if __name__ == "__main__":
    unittest.main()
