import flask
from conexion_mysql import connection_mysql
from conexion_postgres import connection_postgresql

app=flask.Flask(__name__)

#comentarios

@app.route('/')
def my_index():
    return flask.render_template("index.html", token="hola chicos")

app.run(debug=True)