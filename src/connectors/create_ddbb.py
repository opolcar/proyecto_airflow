if __name__ == "__main__":
    import sqlite3

    conexion = sqlite3.connect("tienda_online.db")
    try:
        conexion.execute("""
            CREATE TABLE pedidos (
            numero_pedido INTEGER PRIMARY KEY,
            id_producto INTEGER,
            dni VARCHAR(20),
            fecha_venta DATE
        );""") 
        conexion.execute("""
                        INSERT INTO pedidos (numero_pedido, id_producto, dni, fecha_venta)
                        VALUES 
                            (1,1,'10928251-Z','2024-05-20'),
                            (2,2,'10928251-Z','2024-05-20'),
                            (3,3,'10928251-Z','2024-05-20'),
                            (4,2,'57695931-X','2024-04-20'),
                            (5,3,'45146940-Y','2024-04-24'),
                            (6,4,'17635269-Y','2023-11-05'),
                            (7,5,'18897416-Y','2023-10-20'),
                            (8,1,'18897416-Y','2023-10-20'),
                            (9,3,'10928251-Z','2024-07-05'),
                            (10,3,'10928251-Z','2024-07-05'),
                            (11,5,'10928251-Z','2024-07-05')
                        """)
    except Exception as e:
        print("Error en tabla pedidos:", e)

    try:
        conexion.execute("""
            CREATE TABLE clientes (
            dni VARCHAR(20),
            nombre VARCHAR(100),
            email VARCHAR(50)
            );""")    
        conexion.execute("""
                        INSERT INTO clientes (dni, nombre, email) 
                        VALUES
                            ('10928251-Z','Carlos','carlitos@gmail.com'),
                            ('17635269-Y','Pablo','pablote@gmail.com'),
                            ('18897416-Y','Laura','laula@gmail.com'),
                            ('45146940-Y','Ana','anitadinamita@gmail.com'),
                            ('57695931-X','Marta','martaparra@gmail.com')
                        """)
    except Exception as e:
        print("Error en tabla clientes:", e)

    try:
        conexion.execute("""
            CREATE TABLE productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_producto VARCHAR(255),
                precio REAL,
                url VARCHAR(255),
                create_date TIMESTAMP,
                update_date TIMESTAMP
            );""")
        print("Se creó la tabla productos")
        conexion.execute("""INSERT INTO productos (nombre_producto, precio, url, create_date, update_date) 
                        VALUES 
                            ('JAMÓN BELLOTA IBÉRICO 100%', 338.2, 'https://www.dehesadealburquerque.es/producto/jamon-bellota-iberico-100/', '2024-05-03 11:41:31', '2024-07-19 09:03:58'),
                            ('PALETA CEBO CAMPO IBÉRICA 50%', 71.5, 'https://www.dehesadealburquerque.es/producto/paleta-cebo-campo-iberica-50/', '2024-05-03 11:43:47', '2024-07-19 09:03:58'),
                            ('PALETA BELLOTA IBÉRICA 50%', 98.6, 'https://www.dehesadealburquerque.es/producto/paleta-bellota-iberica-50/', '2024-05-03 11:43:47', '2024-07-19 09:03:58'),
                            ('PALETA BELLOTA IBÉRICA 100%', 104.5, 'https://www.dehesadealburquerque.es/producto/paleta-bellota-iberica-100/', '2024-05-03 11:43:47', '2024-07-19 09:03:58'),
                            ('JAMÓN CURADO «LA JARA DE ALBURQUERQUE»', 115, 'https://www.dehesadealburquerque.es/producto/jamon-curado-la-jara-de-alburquerque/', '2024-05-03 11:43:47', '2024-07-19 09:03:58'),
                            ('Jamón Cebo Campo Ibérico 50%', 139, 'https://www.dehesadealburquerque.es/producto/jamon-cebo-campo-iberico-50/', '2024-05-03 11:43:47', '2024-07-19 09:03:58'),
                            ('LOMO CEBO CAMPO IBÉRICO 50% AL PIMENTÓN', 56.1, 'https://www.dehesadealburquerque.es/producto/lomo-cebo-campo-iberico-50-pimenton/', '2024-06-26 13:27:26', '2024-07-19 09:03:58'),
                            ('LOMO DOBLADO DE BELLOTA IBÉRICO 100%', 66, 'https://www.dehesadealburquerque.es/producto/lomo-doblado-bellota-iberico-100/', '2024-06-27 15:16:19', '2024-07-19 09:03:58'),
                            ('CABEZADA BELLOTA IBÉRICA 100%', 14.85, 'https://www.dehesadealburquerque.es/producto/cabezada-bellota-iberica-100/', '2024-06-27 15:23:54', '2024-07-19 09:03:58')
                        """)
    except Exception as e:
        print("Error en tabla productos:", e)

    conexion.commit()
    conexion.close()
