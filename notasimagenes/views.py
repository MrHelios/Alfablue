import os
from flask import Flask, Blueprint, render_template, request, redirect, url_for
from notasimagenes.db import agregar_nota_imagen, buscar_notas_imagenes_por_nota_id, buscar_una_nota_por_id
from constantes import UPLOAD_FOLDER

notas_imagenes_page = Blueprint('notas_imagenes_page',__name__)

@notas_imagenes_page.route("/notas/<int:nota_id>", methods=['GET','POST'])
def nota_imagen(nota_id):
    nota = buscar_una_nota_por_id(nota_id)
    dir = os.path.join(UPLOAD_FOLDER, str(nota_id))
    if os.path.isdir(dir):
        if request.method == 'POST':
            id = request.form['id']
            dir = os.path.join(UPLOAD_FOLDER, id)
            if id.isdigit() and os.path.exists(dir):
                file = request.files['file']
                agregar_nota_imagen(nota_id, file.filename, request.form['descripcion'])
                file.save(os.path.join(dir, file.filename))
                return redirect(url_for('notas_imagenes_page.nota_imagen', nota_id=nota_id))
            else:
                return "Hubo un problemas, lo siento."
        else:
            notas_imagen = buscar_notas_imagenes_por_nota_id(nota_id)
            aux = []
            for i in notas_imagen:
                dir = os.path.join('upload/', str(nota_id))
                dir = os.path.join(dir,i[2])
                aux.append([i[0],i[1],dir,i[3]])
            notas_imagen = aux;
            return render_template("nota_imagen.html",nota=nota, nota_id=nota_id, notas_imagen=notas_imagen)
    else:
        return "Esta nota no existe"
