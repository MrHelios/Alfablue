from flask import Flask
from notas.views import notas_page
from notasimagenes.views import notas_imagenes_page

app = Flask(__name__)
app.register_blueprint(notas_page)
app.register_blueprint(notas_imagenes_page)

UPLOAD_FOLDER = "static/upload/"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def hola():
    return "Hola mundo"

if __name__=="__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=5000)
