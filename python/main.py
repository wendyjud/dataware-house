import flask

app=flask.Flask(__name__)

#comentarios

@app.route('/')
def my_index():
    return flask.render_template("index.html", token="hola chicos")

app.run(debug=True)