import petl as etl 
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2


table1 = etl.fromcsv('C:/Users/wendy/Documents/7mo semestre/Almacenes de Datos/proyecto/python/recursos/atus_anual_2018.csv')

"""comentario en python requiere de varias lineas."""


def df_2018PM():
    ##-> Especificación de la ubicación de la ruta
    ruta='C:/Users/wendy/Documents/7mo semestre/Almacenes de Datos/proyecto/python/recursos/2018C/2018PM10.csv'
    ##-> Lectura del archivo
    data_2018=pd.read_csv(ruta,  encoding='utf-8')
    ##-> Imprime el volumen de datos original
    print(data_2018.shape)
    ##-> Deuvuelve las primeras n filas(5 por defecto)
    data_2018.head()
    ##-> Devuelve información (número de filas, número de columnas, índices, tipo de las columnas y memoria usado)
    data_2018.info()
    grouped=data_2018.groupby("FECHA").agg({
        "MER": 'mean',
        "PED": 'mean',
        "TLA": 'mean',
        "XAL": 'mean',
        "LOM": 'mean',
        "LPR": 'mean',
        "NEZ": 'mean',
        "SHA": 'mean',
        "UIZ": 'mean',
    })

    grouped.plot(kind="bar")
   
    plt.show()
    #data_2018.to_csv('C:/Users/wendy/Documents/7mo semestre/Almacenes de Datos/proyecto/python/recursos/acc2018.csv', index=False, encoding='latin1')
    return data_2018

    
    
df_2018PM()