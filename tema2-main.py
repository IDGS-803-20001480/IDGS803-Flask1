from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "!!!Hola mundo!!!--cambio"

@app.route("/hola")
def hola():
    return "<h1>Saludo desde hola</h1>"

@app.route("/nueva")
def nueva():
    return "<h1>Saludo desde Nueva</h1>"


if __name__=="__main__":
    app.run(debug=True)