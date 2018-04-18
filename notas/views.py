from flask import Blueprint, render_template, redirect, url_for, request
from notas.db import todas_las_notas, agregar_una_nota, buscar_una_nota_por_id, borrar_una_nota_por_id, actualizar_nota

notas_page = Blueprint('notas_page',__name__)

@notas_page.route('/notas')
def hola():
    notas = todas_las_notas()    
    return render_template('hola.html', notas=notas)

@notas_page.route('/notas/crear', methods=['GET','POST'])
def notaNueva():
    if request.method == 'POST':
        agregar_una_nota(request.form['contenido'], request.form['titulo'])
        return redirect(url_for('notas_page.hola'))
    else:
        return render_template('notanueva.html')

@notas_page.route('/notas/editar/<int:notas_id>', methods=['GET','POST'])
def notaEditar(notas_id):
    nota = buscar_una_nota_por_id(notas_id)
    if request.method == 'POST':
        actualizar_nota(notas_id, request.form['titulo'], request.form['contenido'])
        return redirect(url_for('notas_page.hola'))
    else:
        return render_template('notaeditar.html', nota=nota, notas_id=notas_id)

@notas_page.route('/notas/borrar/<int:notas_id>', methods=['GET','POST'])
def notaBorrar(notas_id):
    nota = buscar_una_nota_por_id(notas_id)
    if request.method == 'POST':
        borrar_una_nota_por_id(notas_id)
        return redirect(url_for('notas_page.hola'))
    else:
        return render_template('notaborrar.html', nota=nota)
