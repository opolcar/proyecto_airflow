import sqlite3
import pandas as pd

class sqlite_connector():
    def __init__(self, database_name:str):
        self.conexion = sqlite3.connect(database_name)

    def close(self):
        self.conexion.close()

    def execute_query(self,query:str):
        cursor = self.conexion.cursor()
        cursor.execute(query)
        self.conexion.commit()

    def get_df (self, query:str) -> pd.DataFrame:
        df=pd.read_sql(query,self.conexion)
        return df
    
    # def change_table(self, old_table:str, new_table:str):
    #     rename=f"RENAME TABLE {old_table} TO {new_table} "
    #     cursor = self.conn.cursor()
    #     cursor.execute(rename)
    #     print(f"Table '{old_table}' renombrada a '{new_table}' correctamente.")
    #     self.conn.commit()