import petl as etl 
import pandas as pd
import matplotlib.pyplot as plt

table1 = etl.fromcsv('C:/Users/wendy/Documents/7mo semestre/Almacenes de Datos/proyecto/python/recursos/atus_anual_2018.csv')

"""comentario en python que requiere de varias lineas."""

def df_2018():
    ##-> Especificación de la ubicación de la ruta
    ruta='C:/Users/wendy/Documents/7mo semestre/Almacenes de Datos/proyecto/python/recursos/atus_anual_2018.csv'
    ##-> Lectura del archivo
    data_2018=pd.read_csv(ruta,  encoding='utf-8')
    ##-> Imprime el volumen de datos original
    print(data_2018.shape)
    ##-> Deuvuelve las primeras n filas(5 por defecto)
    data_2018.head()
    ##-> Devuelve información (número de filas, número de columnas, índices, tipo de las columnas y memoria usado)
    data_2018.info()
    ##-> conteo de los niveles en las diferenres columnas categoricas
    cols_cat=['COBERTURA','DIASEMANA','URBANA','SUBURBANA','TIPACCID','CAUSAACCI','CAPAROD','SEXO','ALIENTO','CINTURON','CLASACC','ESTATUS']
    for col in cols_cat:
        print(f'Columna {col}:{data_2018[col].nunique()} subniveles')

    ##-> Eliminación de columnas irrelevantes para el propósito
    data_2018.drop(columns=['COBERTURA','AUTOMOVIL','CAMPASAJ','MICROBUS', 'PASCAMION', 'OMNIBUS', 'TRANVIA','CAMIONETA','CAMION',
    'TRACTOR','FERROCARRI', 'MOTOCICLET', 'BICICLETA','OTROVEHIC', 'CAPAROD','SEXO', 'ALIENTO','CINTURON','ID_EDAD', 'CONDMUERTO',
    'CONDHERIDO','PASAMUERTO', 'PASAHERIDO', 'PEATMUERTO','PEATHERIDO','CICLMUERTO', 'CICLHERIDO', 'OTROMUERTO', 'OTROHERIDO', 'NEMUERTO', 'NEHERIDO','ESTATUS' ],inplace=True)
    ##-> Devuelve una tupla con el número de filas y columnas, esto mostrará solo las columnas reelevantes, se han quitado las del apso anterior
    #print(data_2018.shape)
    data_2018.head()
    ##-> Filtro para mostrar solo registros pertenecientes al estado de México,es decir, de ID_ENTIDAD==15
    filtro = data_2018['ID_ENTIDAD'] == 15
    print("Volumen final")
    data_2018 = data_2018[filtro]
    print(data_2018.shape)
    #data_2018.head()
    #Municipios con mas frecuencia de accidentes
    print(data_2018['ID_MUNICIPIO'].value_counts(ascending=False))
    plt.title("El municipio con mayor número de accidentes en el estado de México es Ecatepec de Morelos= mun 33")   # Establece el título del gráfica
    data_2018['ID_MUNICIPIO'].value_counts().plot(kind='bar')
    plt.show()
    #El municipio con mayor número de accidentes en el Edo de México en el 2018 fue Ecatepec de Morelos
    print(data_2018['CLASACC'].value_counts())
    data_2018.to_csv('C:/Users/wendy/Documents/7mo semestre/Almacenes de Datos/proyecto/python/recursos/acc2018.csv', index=False, encoding='latin1')
    return data_2018

def df_2019():
    ruta='C:/Users/wendy/Documents/7mo semestre/Almacenes de Datos/proyecto/python/recursos/atus_anual_2019.csv'
    data_2019=pd.read_csv(ruta)
    print(data_2019.shape)
    data_2019.head()
    data_2019.info()
    cols_cat=['COBERTURA','DIASEMANA','URBANA','SUBURBANA','TIPACCID','CAUSAACCI','CAPAROD','SEXO','ALIENTO','CINTURON','CLASACC','ESTATUS']
    for col in cols_cat:
        print(f'Columna {col}:{data_2019[col].nunique()} subniveles')

    data_2019.drop(columns=['COBERTURA','AUTOMOVIL','CAMPASAJ','MICROBUS', 'PASCAMION', 'OMNIBUS', 'TRANVIA','CAMIONETA','CAMION',
    'TRACTOR','FERROCARRI', 'MOTOCICLET', 'BICICLETA','OTROVEHIC', 'CAPAROD','SEXO', 'ALIENTO','CINTURON','ID_EDAD', 'CONDMUERTO',
    'CONDHERIDO','PASAMUERTO', 'PASAHERIDO', 'PEATMUERTO','PEATHERIDO','CICLMUERTO', 'CICLHERIDO', 'OTROMUERTO', 'OTROHERIDO', 'NEMUERTO', 'NEHERIDO','ESTATUS' ],inplace=True)
    #print(data_2019.shape)
    data_2019.head()
    filtro = data_2019['ID_ENTIDAD'] == 15
    print("Volumen final")
    data_2019 = data_2019[filtro]
    print(data_2019.shape)
    data_2019.head()
    
    return data_2019

def df_2020():
    ruta='C:/Users/wendy/Documents/7mo semestre/Almacenes de Datos/proyecto/python/recursos/atus_anual_2020.csv'
    data_2020=pd.read_csv(ruta)
    print(data_2020.shape)
    data_2020.head()
    data_2020.info()
    cols_cat=['COBERTURA','DIASEMANA','URBANA','SUBURBANA','TIPACCID','CAUSAACCI','CAPAROD','SEXO','ALIENTO','CINTURON','CLASACC','ESTATUS']
    for col in cols_cat:
        print(f'Columna {col}:{data_2020[col].nunique()} subniveles')

    data_2020.drop(columns=['COBERTURA','AUTOMOVIL','CAMPASAJ','MICROBUS', 'PASCAMION', 'OMNIBUS', 'TRANVIA','CAMIONETA','CAMION',
    'TRACTOR','FERROCARRI', 'MOTOCICLET', 'BICICLETA','OTROVEHIC', 'CAPAROD','SEXO', 'ALIENTO','CINTURON','ID_EDAD', 'CONDMUERTO',
    'CONDHERIDO','PASAMUERTO', 'PASAHERIDO', 'PEATMUERTO','PEATHERIDO','CICLMUERTO', 'CICLHERIDO', 'OTROMUERTO', 'OTROHERIDO', 'NEMUERTO', 'NEHERIDO','ESTATUS' ],inplace=True)
    #print(data_2020.shape)
    data_2020.head()
    filtro = data_2020['ID_ENTIDAD'] == 15
    print("Volumen final")
    data_2020 = data_2020[filtro]
    print(data_2020.shape)
    data_2020.head()
    return data_2020

def df_2021():
    ##-> Especificación de la ubicación de la ruta
    ruta='C:/Users/wendy/Documents/7mo semestre/Almacenes de Datos/proyecto/python/recursos/atus_anual_2021.csv'
    ##-> Lectura del archivo
    data_2021=pd.read_csv(ruta)
    ##-> Imprime el volumen de datos original
    print(data_2021.shape)
    ##-> Deuvuelve las primeras n filas(5 por defecto)
    data_2021.head()
    ##-> Devuelve información (número de filas, número de columnas, índices, tipo de las columnas y memoria usado)
    data_2021.info()
    ##-> conteo de los niveles en las diferenres columnas categoricas
    cols_cat=['COBERTURA','DIASEMANA','URBANA','SUBURBANA','TIPACCID','CAUSAACCI','CAPAROD','SEXO','ALIENTO','CINTURON','CLASACC','ESTATUS']
    for col in cols_cat:
        print(f'Columna {col}:{data_2021[col].nunique()} subniveles')

    ##-> Eliminación de columnas irreevantes para el propósito
    data_2021.drop(columns=['COBERTURA','AUTOMOVIL','CAMPASAJ','MICROBUS', 'PASCAMION', 'OMNIBUS', 'TRANVIA','CAMIONETA','CAMION',
    'TRACTOR','FERROCARRI', 'MOTOCICLET', 'BICICLETA','OTROVEHIC', 'CAPAROD','SEXO', 'ALIENTO','CINTURON','ID_EDAD', 'CONDMUERTO',
    'CONDHERIDO','PASAMUERTO', 'PASAHERIDO', 'PEATMUERTO','PEATHERIDO','CICLMUERTO', 'CICLHERIDO', 'OTROMUERTO', 'OTROHERIDO', 'NEMUERTO', 'NEHERIDO','ESTATUS' ],inplace=True)
    ##-> Devuelve una tupla con el número de filas y columnas, esto mostrará solo las columnas reelevantes, se han quitado las del apso anterior
    #print(data_2021.shape)
    data_2021.head()
    ##-> Filtro para mostrar solo registros pertenecientes al estado de México,es decir, de ID_ENTIDAD==15
    filtro = data_2021['ID_ENTIDAD'] == 15
    print("Volumen final")
    data_2021 = data_2021[filtro]
    print(data_2021.shape)
    data_2021.head()
    ##-> Retorna el resultado final de limpieza de accidentes ocurridos en el 2018, estado de México.   
    return data_2021

df_2018()
#df_2019()
#df_2020()
#df_2021()