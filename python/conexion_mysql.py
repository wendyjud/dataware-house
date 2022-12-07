import mysql.connector

try:
    connection_mysql=mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="jnNS57kXr5EHWT]O",
        db="contaminantes"
    )
    if connection_mysql.is_connected():
        print("Conexión exitosa")
        
except Exception as ex:
    print(ex)