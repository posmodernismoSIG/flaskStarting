#header con la importacion del framework y la incializacion
from flask import Flask
app = Flask(__name__)

#get en el navegador
@app.route("/")
def hello_world():
    return "<p> Hello World"

if __name__=='__main__':
    app.run(debug=true,port=5000)   #ejecucion automatica lugo de los cambios el run corre el codigo

