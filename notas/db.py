import psycopg2

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

DBNAME = "pagina"
USER = "lucho"
