import psycopg2

try: 
    connection_postgresql=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='wendy123',
        database='accidentes'
    )

    print("Conexión exitosa base de datos:accidentes")
        
except Exception as ex:
    print(ex)