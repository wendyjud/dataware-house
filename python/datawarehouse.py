import pandas as pd 
import psycopg2
import mysql.connector


file=pd.read_csv('C:/Users/wendy/Documents/7mo semestre/Almacenes de Datos/proyecto/python/recursos/acc2018.csv', encoding='latin-1')
valores=file.values.tolist()

connection_postgresql=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='wendy123',
        database='datawarehouse'
    )

print("Conexión exitosa base de datos:datawarehouse")

#cursor para almacenar la información en memoria
cursor=connection_postgresql.cursor()

#crear la tabla info
cursor.execute("""CREATE TABLE acc2018 (ID_ENTIDAD CHAR(2), ID_MUNICIPIO CHAR(3),ANIO INT,MES CHAR(2),	ID_HORA  INT,	ID_MINUTO  INT,	ID_DIA CHAR(2),	DIASEMANA VARCHAR(20),	URBANA VARCHAR(50),SUBURBANA VARCHAR(50),
	TIPACCID VARCHAR(100),	CAUSAACCI VARCHAR(50),	CLASACC VARCHAR(50)
);""")
#insersión de datos
cursor.executemany("INSERT INTO acc2018 (ID_ENTIDAD,ID_MUNICIPIO,ANIO,MES,ID_HORA,ID_MINUTO,ID_DIA,DIASEMANA,URBANA,SUBURBANA,TIPACCID,CAUSAACCI,CLASACC) VALUES (%s,%s,%s,%s,%s, %s, %s,%s ,%s,%s,%s,%s,%s)", valores)

#agregar otra tabla de otro gestor de bases de datos
file2=pd.read_csv('C:/Users/wendy/Documents/7mo semestre/Almacenes de Datos/proyecto/python/recursos/2018pm10.csv', encoding='latin-1')
valores2=file2.values.tolist()
#cursor para almacenar la información en memoria
#cursor=connection_postgresql.cursor()

#crear la tabla info
cursor.execute("""CREATE TABLE con_2018PM10 (FECHA DATE, MER FLOAT, PED FLOAT,TLA FLOAT,XAL FLOAT, LOM FLOAT, LPR FLOAT, NEZ FLOAT, SHA FLOAT,UIZ FLOAT);""")
#insersión de datos
cursor.executemany("INSERT INTO con_2018PM10 (FECHA , MER, PED ,TLA ,XAL , LOM , LPR , NEZ	, SHA ,UIZ ) VALUES (%s,%s,%s,%s,%s, %s, %s,%s ,%s,%s)", valores2)



#Guardar los cambios a la base de datos
connection_postgresql.commit()

connection_postgresql.close()