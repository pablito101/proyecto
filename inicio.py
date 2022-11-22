from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# Crud del Pantalones
@app.route('/pantalones_dama')
def pantalones_dama(): 
    return render_template("panatlones_dama.html")

@app.route('/pantalones')
def pantalones(): 
    return render_template("pantalones.html")

# Crud de Sudaderas
@app.route('/sudaderas')
def sudaderas():
    return render_template("sudaderas.html")

@app.route('/suda_dama')
def suda_dama():
    return render_template("suda_dama.html")


# Crud del Blusas
@app.route('/blusas')
def blusas():
    return render_template("blusas.html")

@app.route('/playeras')
def playeras():
    return render_template("playeras.html")


 # Crud del Camisas
@app.route('/camisas')
def camisas():
    return render_template("camisas.html")

@app.route('/camisas_dama')
def camisas_dama():
    return render_template("camisas_dama.html")


 # Crud del Shorts
@app.route('/shorts')
def shorts():
    return render_template("shorts.html")
 
@app.route('/shorts_dama')
def shorts_dama():
    return render_template("short_dama.html")


 # Crud de Ropa Interior
@app.route('/ropa_interior')
def ropa_interior():
    return render_template("ropa_interior.html")

@app.route('/ropa_dama')
def ropa_dama():
    return render_template("ropa_dama.html")


 # Crud de Zapatos
@app.route('/zapatos')
def zapatos():
    return render_template("zapatos.html")

@app.route('/zapa_dama')
def zapa_dama():
    return render_template("zapa_dama.html")


 # Crud del Accesorios
@app.route('/accesorios')
def accesorios():
    return render_template("accesorios.html")

@app.route('/acc_dama')
def acc_dama():
    return render_template("acc_dama.html")


# Crud del Buen fin
@app.route('/buen_fin')
def buen_fin():
    return render_template("buen_fin.html")


# Crud del Rebajas
@app.route('/rebajas')
def rebajas():
    return render_template("rebajas.html")



@app.route('/contacto')
def contacto():
    return render_template("contacto.html")


@app.route('/crud')
def crud():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='dasp')
    cursor = conn.cursor()
    cursor.execute('select id, correo, comentarios from comenta order by id')
    datos = cursor.fetchall()
    return render_template("crud.html", comen = datos)

@app.route('/editar/<string:id>')
def editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='dasp')
    cursor = conn.cursor()
    cursor.execute('select id, correo, comentarios from comenta where id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editar.html", comentar=dato[0])

@app.route('/editar_comenta/<string:id>',methods=['POST'])
def editar_comenta(id):
    if request.method == 'POST':
        corr=request.form['correo']
        come=request.form['comentarios']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='dasp')
        cursor = conn.cursor()
        cursor.execute('update comenta set correo=%s, comentarios=%s where id=%s', (corr,come,id))
        conn.commit()
    return redirect(url_for('crud'))

@app.route('/borrar/<string:id>')
def borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='dasp')
    cursor = conn.cursor()
    cursor.execute('delete from comenta where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('crud'))

@app.route('/insertar')
def insertar():
    return render_template("insertar.html")

@app.route('/agrega_comenta', methods=['POST'])
def agrega_comenta():
    if request.method == 'POST':
        aux_Correo = request.form['correo']
        aux_Comentarios = request.form['comentarios']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='dasp')
        cursor = conn.cursor()
        cursor.execute('insert into comenta (correo,comentarios) values (%s, %s)',(aux_Correo, aux_Comentarios))
        conn.commit()
    return redirect(url_for('crud'))


@app.route('/Registro')
def Registro():
    return render_template("registro.html")

@app.route('/usuarios', methods=['POST'])
def usuarios():
    if request.method == 'POST':
        aux_Correo = request.form['correo']
        aux_Contrasena = request.form['contrasena']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='dasp')
        cursor = conn.cursor()
        cursor.execute('insert into registros (correo,contrasena) values (%s, %s)',(aux_Correo, aux_Contrasena))
        conn.commit()
    return redirect(url_for('Registro'))





# Crud de Mensaje
@app.route('/mensaje')
def mensaje():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='dasp' )
    cursor = conn.cursor()
    cursor.execute('select idmsj, tu_msj from mensaje order by idmsj')
    datos = cursor.fetchall()
    return render_template("nuevo_msj.html", mensaje = datos)

@app.route('/editar_msj/<string:id>')
def editar_msj(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='dasp')
    cursor = conn.cursor()
    cursor.execute('select idmsj, tu_msj from mensaje where idmsj = %s', (id))
    dato = cursor.fetchall()
    return render_template("edi_mensaje.html", mensaje=dato[0])

@app.route('/mensaje_fedita/<string:id>',methods=['POST'])
def mensaje_fedita(id):
    if request.method == 'POST':
        desc=request.form['tu_msj']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='dasp')
        cursor = conn.cursor()
        cursor.execute('update mensaje set tu_msj=%s where idmsj=%s', (desc,id))
        conn.commit()
    return redirect(url_for('mensaje'))
    
@app.route('/borrar_msj/<string:id>')
def borrar_msj(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='dasp')
    cursor = conn.cursor()
    cursor.execute('delete from mensaje where idmsj = {0}'.format(id))
    conn.commit()
    return redirect(url_for('mensaje'))

@app.route('/mensaje_agr')
def mensaje_agr():
    return render_template("agr_mensaje.html")

@app.route('/mensaje_fagrega', methods=['POST'])
def mensaje_fagrega():
    if request.method == 'POST':
        desc = request.form['tu_msj']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='dasp' )
        cursor = conn.cursor()
        cursor.execute('insert into mensaje (tu_msj) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('mensaje'))

if __name__ == "__main__":
    app.run(debug=True)