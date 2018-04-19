import os
import psycopg2
from constantes import UPLOAD_FOLDER

# DB NOTA-IMAGEN

def buscar_notas_imagenes_por_nota_id(notas_id):
    sql = '''SELECT * FROM "%s" WHERE notas_id=''' % (TABLA_NOTAS_IMAGENES)
    sql += '''%s;'''
    conn = psycopg2.connect(dbname=DBNAME, user=USER)
    c = conn.cursor()
    c.execute(sql, (str(notas_id)))
    filas = c.fetchall()
    c.close()
    conn.close()
    return list(filas)

def buscar_nota_imagen_por_id(nota_imagen_id):
    sql = '''SELECT * FROM "%s" WHERE id=''' % (TABLA_NOTAS_IMAGENES)
    sql += '''%s;'''
    conn = None
    fila = None
    try:
        conn = psycopg2.connect(dbname=DBNAME, user=USER)
        c = conn.cursor()
        c.execute(sql, (str(nota_imagen_id)))
        fila = c.fetchone()
        c.close()
    except (psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return fila

def agregar_nota_imagen(notas_id,titulo,descripcion):
    conn = None
    sql = '''INSERT INTO "%s" (notas_id,titulo,descripcion) VALUES '''  % (TABLA_NOTAS_IMAGENES)
    sql += '''(%s,%s,%s);'''
    try:
        conn = psycopg2.connect(dbname=DBNAME, user=USER)
        c = conn.cursor()
        c.execute(sql, (notas_id,titulo,descripcion))
        conn.commit()
        c.close()
    except (psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def borrar_una_nota_imagen_por_id(nota_imagen_id):
    sql = '''DELETE FROM "%s" WHERE id=''' % (TABLA_NOTAS_IMAGENES)
    sql += '''%s;'''
    conn = None
    try:
        conn = psycopg2.connect(dbname=DBNAME, user=USER)
        c = conn.cursor()
        c.execute(sql, str(nota_imagen_id))
        conn.commit()
        c.close()
        conn.close()
    except (psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# DB NOTA

def todas_las_notas():
    sql = '''SELECT * FROM notas ORDER BY id DESC;'''
    conn = psycopg2.connect(dbname=DBNAME, user=USER)
    c = conn.cursor()
    c.execute(sql)
    filas = c.fetchall()
    c.close()
    conn.close()
    return list(filas)

def agregar_una_nota(contenido, titulo):
    conn = psycopg2.connect(dbname=DBNAME, user=USER)
    c = conn.cursor()
    c.execute('''INSERT INTO notas (contenido,titulo) VALUES ('%s','%s');''' % (contenido, titulo))
    conn.commit()
    c.close()
    conn.close()

def buscar_una_nota_por_id(id):
    conn = psycopg2.connect(dbname=DBNAME, user=USER)
    c = conn.cursor()
    c.execute('''SELECT * FROM notas WHERE id=%s;''' % (id))
    r = c.fetchone()
    c.close()
    conn.close()
    return r;

def borrar_una_nota_por_id(id):
    conn = psycopg2.connect(dbname=DBNAME, user=USER)
    c = conn.cursor()
    c.execute('''DELETE FROM notas WHERE id=%s;''' % (id))
    conn.commit()
    c.close()
    conn.close()

def actualizar_nota(id,titulo,contenido):
    conn = None
    sql = '''UPDATE notas SET contenido= %s, titulo=%s WHERE id=%s;'''
    try:
        conn = psycopg2.connect(dbname=DBNAME, user=USER)
        c = conn.cursor()
        c.execute(sql, (contenido,titulo,id))
        conn.commit()
        c.close()
    except (psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Manejo de archivo

def comprobar_notas():
    dir_up = UPLOAD_FOLDER
    if not os.path.isdir(dir_up):
        os.mkdir(dir_up)
    for nota in todas_las_notas():
        dir = os.path.join(dir_up, str(nota[0]))
        esta = os.path.isdir(dir)
        if not esta:
            os.mkdir(dir)

# CONSTANTES

DBNAME = 'pagina'
USER = 'lucho'
TABLA_NOTAS = 'notas'
TABLA_NOTAS_IMAGENES = "notas-imagenes"

if __name__=='__main__':
    print("Comprobar si existen las carpetas correspondientes.")
    comprobar_notas()
