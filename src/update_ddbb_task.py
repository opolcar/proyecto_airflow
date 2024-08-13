
from src.connectors.sqlite_connector import sqlite_connector
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def gef_df(conector:sqlite_connector, query:str) -> pd.DataFrame:
    df=conector.get_df(query)
    return df

def update_df(df=pd.DataFrame)-> pd.DataFrame:
    headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'} 
    update_date= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for index,row in df.iterrows():
        url=row['url']
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            nombre_producto = soup.find('h2', class_= 'edgtf-single-product-title')
            nombre_producto = nombre_producto.text.strip()
            precio = float(soup.find('span', class_='woocommerce-Price-amount amount').text.replace('€','').replace(',','.'))
            df.loc[index,'precio']=precio
            df.loc[index,'nombre_producto']=nombre_producto
            df.loc[index,'update_date']=update_date
    return df

def update_bbdd(conector:sqlite_connector, df:pd.DataFrame):
    try:
        for index, row in df.iterrows():
            query=f"UPDATE productos SET nombre_producto = '{row['nombre_producto']}', precio = {row['precio']}, update_date= '{row['update_date']}' WHERE url = '{row['url']}';"
            print(query)
            conector.execute_query(query=query)
        print(f"Se han actualizado {str(index)} productos en la tabla productos de SQLITE exitosamente.")
    except Exception as e:
        print(f"Error al actualizar la tabla SQLITE: {e}")

def execute(database_name:str):
    conector=sqlite_connector (database_name=database_name)
    df_completo=gef_df(conector, query='SELECT * FROM productos')
    df_actualizado=update_df(df_completo)
    update_bbdd(conector=conector,df=df_actualizado)
    conector.close()
    

if __name__ == "__main__":
    execute(database_name='tienda_online.db')

  