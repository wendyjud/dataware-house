
import psycopg2
import pandas as pd

  
conn = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='wendy123',
    database='accidentes')
  
#Importar datos de postgresql a pandas
# Creamos el cursor con el objeto conexion
cur = conn.cursor()

# Ejecutamos una consulta
cur.execute( "SELECT * FROM acc2018" )

acc2018=cur.fetchall()
for acc in acc2018:
    print(acc)


# Cerramos la conexión
conn.close()