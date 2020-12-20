from flask import Flask, render_template, abort, request, redirect, url_for
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from models.modelo import db, Botiquin, LiquidoLaboratorio, ReactivoLaboratorio, EquipoInventario, Laboratorio, AlumnoAlimentarias, Maestro, Usuario, RegistroPractica, Material
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = 'MyL4b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://AdminLaboratorio:hola.123@localhost/MyLab'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER']='static/uploads/'
# Configuración para el manejo de la sesion de los usuarios
loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view = "inicio"


@loginManager.user_loader
def load_user(Id):
    return Usuario.query.get(int(Id))

@app.route('/')
def inicio():
    try:
        if current_user.is_authenticated and current_user.Tipo=="M":
            return render_template('indexMaestro.html')
        if current_user.is_authenticated and current_user.Tipo=="A":
            p=RegistroPractica()
            p=p.consultaGeneral()
            return render_template('indexAlumno.html',practicas=p)
        if current_user.is_authenticated and current_user.Tipo=="L":
            p=RegistroPractica()
            p=p.consultaGeneralConteo()
            m=RegistroPractica()
            m=m.consultaGeneralConteo()
            a=RegistroPractica()
            a=a.consultaGeneralConteo()
            return render_template('indexLaboratorista.html',practicas=p,maestros=m,alumnos=a)
        else:
            return render_template('index.html')
    except:
        abort(500)

@app.route('/login',methods=['POST'])
def login():
    try:
        u = Usuario()
        u = u.validar(request.form['inputEmail'], request.form['inputPassword'])
        if u != None:
            login_user(u)
            return redirect(url_for('inicio'))
        else:
            return 'Datos No Válidos'
    except:
        abort(500)
    
@app.route('/cerrarSesion')
@login_required
def cerrarSesion():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for("inicio"))
    else:
        abort(404)

#########################################
#########################################
# Rutas para el CRUD de la tabla Usuarios

@app.route('/usuarios/new')
@login_required
def nuevoUsuario():
    if current_user.Tipo!="A":
        return render_template('Usuarios/altaUsuario.html')
    else:
        return redirect(url_for("inicio"))

@app.route('/usuarios/save',methods=['POST'])
@login_required
def guardarUsuario():
    if current_user.Tipo!="A":
        try:
            u= Usuario()
            u.IdUsuario = request.form['idusuario']
            u.NombreCompleto = request.form['nombre']
            u.Telefono = request.form['telefono']
            u.Email = request.form['email']
            u.Contrasenia = request.form['contraseña']
            u.Sexo = request.form['sexo']
            u.Tipo = request.form['tipo']
            u.insertar()
            return redirect(url_for('consultaGeneralUsuario'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/usuarios')
@login_required
def consultaGeneralUsuario():
    if current_user.Tipo!="A":
        try:
            usuario = Usuario()
            usuarios = usuario.consultaGeneral()
            return render_template('Usuarios/consultaUsuario.html', usuarios=usuarios)
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/usuarios/<int:id>')
@login_required
def consultarUsuario(id):
    if current_user.Tipo!="A":
        try:
            usuario = Usuario()
            usuario.IdUsuario = id
            usuario = usuario.consultaIndividual()
            return render_template('Usuarios/modificarUsuario.html', usuario=usuario)
        except:
            abort(400)
    else:
        return redirect(url_for("inicio"))

@app.route('/usuarios/modificar', methods=['POST'])
@login_required
def actualizarUsuario():
    if current_user.Tipo!="A":
        try:
            u = Usuario()
            u.IdUsuario = request.form['idusuario']
            u.Nombre = request.form['nombre']
            u.Telefono = request.form['telefono']
            u.Email = request.form['email']
            u.Contrasenia = request.form['contraseña']
            u.Sexo = request.form['sexo']
            u.Tipo = request.form['tipo']
            u.actualizar()
            return redirect(url_for('consultaGeneralUsuario'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/usuarios/delete/<int:id>')
@login_required
def eliminarUsuario(id):
    if current_user.Tipo=="L":
        try:
            usuario = Usuario()
            usuario.IdUsuario = id
            usuario.eliminar()
            return redirect(url_for('consultaGeneralUsuario'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))
# fin del crud de Usuarios
#########################################
#########################################


#########################################
#########################################
# Rutas para el CRUD de la tabla Alumnos
@app.route('/alumnos/new')
@login_required
def nuevoAlumno():
    if current_user.Tipo!="A":
        return render_template('Alumnos/altaAlumno.html')
    else:
        return redirect(url_for("inicio"))

@app.route('/alumnos/save',methods=['POST'])
@login_required
def guardarAlumno():
    if current_user.Tipo!="A":
        try:
            a = AlumnoAlimentarias()
            a.NoControl = request.form['nocontrol']
            a.IdUsuario = request.form['idusuario']
            a.Semestre = request.form['semestre']
            a.Grupo = request.form['semestre']
            a.insertar()
            return redirect(url_for('consultaGeneralAlumno'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/alumnos')
@login_required
def consultaGeneralAlumno():
    if current_user.Tipo!="A":
        try:
            a = AlumnoAlimentarias()
            a = a.consultaGeneral()
            return render_template('Alumnos/consultaAlumno.html', Alumnos=a)
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/alumnos/<int:id>')
@login_required
def consultarAlumno(id):
    if current_user.Tipo!="A":
        try:
            alumno = AlumnoAlimentarias()
            alumno.NoControl = id
            alumno = alumno.consultaIndividual()
            return render_template('Alumnos/modificarAlumno.html', Alumno=alumno)
        except:
            abort(400)
    else:
        return redirect(url_for("inicio"))

@app.route('/alumnos/modificar', methods=['POST'])
@login_required
def actualizarAlumno():
    if current_user.Tipo!="A":
        try:
            a = AlumnoAlimentarias()
            a.NoControl = request.form['nocontrol']
            a.IdUsuario = request.form['idusuario']
            a.Semestre = request.form['semestre']
            a.Grupo = request.form['semestre']
            a.actualizar()
            return redirect(url_for('consultaGeneralAlumno'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))


@app.route('/alumnos/delete/<int:id>')
@login_required
def eliminarAlumno(id):
    if current_user.Tipo!="A":
        try:
            alumno = AlumnoAlimentarias()
            alumno.NoControl = id
            alumno.eliminar()
            return redirect(url_for('consultaGeneralAlumno'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))
# fin del crud de Alumnos
#########################################
#########################################

#########################################
#########################################
# Rutas para el CRUD de la tabla Laboratorios
@app.route('/laboratorios/new')
@login_required
def nuevoLaboratorio():
    if current_user.Tipo=="L":
        return render_template('Laboratorios/altaLaboratorio.html')
    else:
        return redirect(url_for("inicio"))

@app.route('/laboratorios/save',methods=['POST'])
@login_required
def guardarLaboratorio():
    if current_user.Tipo=="L":
        try:
            l = Laboratorio()
            l.IdLaboratorio = request.form['idlaboratorio']
            l.NombreLaboratorio = request.form['nombre']
            l.Edificio = request.form['edificio']
            l.NumeroAula = request.form['aula']
            l.insertar()
            return redirect(url_for('consultaGeneralLaboratorio'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/laboratorios')
@login_required
def consultaGeneralLaboratorio():
    if current_user.Tipo=="L":
        l = Laboratorio()
        l = l.consultaGeneral()
        return render_template('Laboratorios/consultaLaboratorio.html', Laboratorios=l)
    else:
        return redirect(url_for("inicio"))

@app.route('/laboratorios/<int:id>')
@login_required
def consultarLaboratorio(id):
    if current_user.Tipo=="L":
        try:
            l = Laboratorio()
            l.IdLaboratorio = id
            l = l.consultaIndividual()
            return render_template('Laboratorios/modificarLaboratorio.html', Laboratorio=l)
        except:
            abort(400)
    else:
        return redirect(url_for("inicio"))

@app.route('/laboratorios/modificar', methods=['POST'])
@login_required
def actualizarLaboratorio():
    if current_user.Tipo=="L":
        try:
            l = Laboratorio()
            l.IdLaboratorio = request.form['idlaboratorio']
            l.NombreLaboratorio = request.form['nombre']
            l.Edificio = request.form['edificio']
            l.NumeroAula = request.form['aula']
            l.actualizar()
            return redirect(url_for('consultaGeneralLaboratorio'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/laboratorios/delete/<int:id>')
@login_required
def eliminarLaboratorio(id):
    if current_user.Tipo=="L":
        try:
            l = Laboratorio()
            l.IdLaboratorio = id
            l.eliminar()
            return redirect(url_for('consultaGeneralLaboratorio'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))
# fin del crud de Laboratorios
#########################################
#########################################

#########################################
#########################################
# Rutas para el CRUD de la tabla Botiquines
@app.route('/botiquines/new')
@login_required
def nuevoBotiquin():
    if current_user.Tipo=="L":
        return render_template('Botiquines/altaBotiquin.html')
    else:
        return redirect(url_for("inicio"))   

@app.route('/botiquines/save',methods=['POST'])
@login_required
def guardarBotiquin():
    if current_user.Tipo=="L":
        try:
            b = Botiquin()
            b.IdArticuloBotiquin=request.form['idarticulo']
            b.IdLaboratorio=request.form['idlaboratorio']
            b.NombreArtículo=request.form['nombre']
            b.Cantidad=request.form['cantidad']
            b.Capacidad=request.form['capacidad']
            b.insertar()
            return redirect(url_for('consultaGeneralBotiquin'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/botiquines')
@login_required
def consultaGeneralBotiquin():
    if current_user.Tipo=="L":
        try:
            b = Botiquin()
            b = b.consultaGeneral()
            return render_template('Botiquines/consultaBotiquin.html', Botiquines=b)
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/botiquines/<int:id>')
@login_required
def consultarBotiquin(id):
    if current_user.Tipo=="L":
        try:
            b = Botiquin()
            b.IdArticuloBotiquin = id
            b = b.consultaIndividual()
            return render_template('Botiquines/modificarBotiquin.html', Botiquin=b)
        except:
            abort(400)
    else:
        return redirect(url_for("inicio"))

@app.route('/botiquines/modificar', methods=['POST'])
@login_required
def actualizarBotiquin():
    if current_user.Tipo=="L":
        try:
            b = Botiquin()
            b.IdArticuloBotiquin=request.form['idarticulo']
            b.IdLaboratorio=request.form['idlaboratorio']
            b.NombreArtículo=request.form['nombre']
            b.Cantidad=request.form['cantidad']
            b.Capacidad=request.form['capacidad']
            b.actualizar()
            return redirect(url_for('consultaGeneralBotiquin'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/botiquines/delete/<int:id>')
@login_required
def eliminarBotiquin(id):
    if current_user.Tipo=="L":
        try:
            b = Botiquin()
            b.IdArticuloBotiquin = id
            b.eliminar()
            return redirect(url_for('consultaGeneralBotiquin'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))
# fin del crud de Botiquines
#########################################
#########################################



#########################################
#########################################
# Rutas para el CRUD de la tabla EquiposInventario
@app.route('/inventario/new')
@login_required
def nuevoInventario():
    if current_user.Tipo=="L":
        return render_template('EquiposInventario/altaEquipo.html')
    else:
        return redirect(url_for("inicio"))

@app.route('/inventario/save',methods=['POST'])
@login_required
def guardarInventario():
    if current_user.Tipo=="L":
        try:
            e = EquipoInventario()
            e.IdEquipo=request.form['idequipo']
            e.IdLaboratorio=request.form['idlaboratorio']
            e.NombreEquipo=request.form['nombreequipo']
            e.Cantidad=request.form['cantidad']
            e.Descripcion=request.form['descripcion']
            Foto=request.files['foto']
            filename = secure_filename(Foto.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'],Foto.filename)
            Foto.save(path)
            e.Foto=filename
            e.insertar()
            return redirect(url_for('consultaGeneralInventario'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/inventario')
@login_required
def consultaGeneralInventario():
    if current_user.Tipo=="L":
        try:
            e = EquipoInventario()
            e = e.consultaGeneral()
            return render_template('EquiposInventario/consultaEquipo.html', Equipos=e)
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/inventario/<int:id>')
@login_required
def consultarInventario(id):
    if current_user.Tipo=="L":
        try:
            e = EquipoInventario()
            e.IdEquipo = id
            e = e.consultaIndividual()
            return render_template('EquiposInventario/modificarEquipo.html', Equipo=e)
        except:
            abort(400)
    else:
        return redirect(url_for("inicio"))

@app.route('/inventario/modificar', methods=['POST'])
@login_required
def actualizarInventario():
    if current_user.Tipo=="L":
        try:
            e = EquipoInventario()
            e.IdEquipo=request.form['idequipo']
            e.IdLaboratorio=request.form['idlaboratorio']
            e.NombreEquipo=request.form['nombreequipo']
            e.Cantidad=request.form['cantidad']
            e.Descripcion=request.form['descripcion']
            Foto=request.files['foto']
            filename = secure_filename(Foto.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'],Foto.filename)
            Foto.save(path)
            e.Foto=filename
            e.actualizar()
            return redirect(url_for('consultaGeneralInventario'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/inventario/delete/<int:id>')
@login_required
def eliminarInventario(id):
    if current_user.Tipo=="L":
        try:
            e = EquipoInventario()
            e.IdEquipo = id
            e.eliminar()
            return redirect(url_for('consultaGeneralInventario'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))
# fin del crud de EquiposInventario
#########################################
#########################################

#########################################
#########################################
# Rutas para el CRUD de la tabla LiquidosLaboratorio
@app.route('/liquidos/new')
@login_required
def nuevoLiquido():
    if current_user.Tipo=="L":
        return render_template('LiquidosLaboratorio/altaLiquido.html')
    else:
        return redirect(url_for("inicio"))  

@app.route('/liquidos/save',methods=['POST'])
@login_required
def guardarLiquido():
    if current_user.Tipo=="L":
        try:
            li = LiquidoLaboratorio()
            li.IdLiquido=request.form['idliquido']
            li.IdLaboratorio=request.form['idlaboratorio']
            li.MedioCultivo=request.form['medio']
            li.FechaCaducidad=request.form['caducidad']
            li.Cantidad=request.form['cantidad']
            li.Capacidad=request.form['capacidad']
            li.insertar()
            return redirect(url_for('consultaGeneralLiquidos'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))


@app.route('/liquidos')
@login_required
def consultaGeneralLiquidos():
    if current_user.Tipo=="L":
        try:
            li = LiquidoLaboratorio()
            li = li.consultaGeneral()
            return render_template('LiquidosLaboratorio/consultaLiquido.html', Liquidos=li)
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/liquidos/<int:id>')
@login_required
def consultarLiquido(id):
    if current_user.Tipo=="L":
        try:
            li = LiquidoLaboratorio()
            li.IdLiquido = id
            li = li.consultaIndividual()
            return render_template('LiquidosLaboratorio/modificarLiquido.html', Liquido=li)
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/liquidos/modificar', methods=['POST'])
@login_required
def actualizarLiquido():
    if current_user.Tipo=="L":
        try:
            li = LiquidoLaboratorio()
            li.IdLiquido=request.form['idliquido']
            li.IdLaboratorio=request.form['idlaboratorio']
            li.MedioCultivo=request.form['medio']
            li.FechaCaducidad=request.form['caducidad']
            li.Cantidad=request.form['cantidad']
            li.Capacidad=request.form['capacidad']
            li.actualizar()
            return redirect(url_for('consultaGeneralLiquidos'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/liquidos/delete/<int:id>')
@login_required
def eliminarLiquidos(id):
    if current_user.Tipo=="L":
        try:
            li = LiquidoLaboratorio()
            li.IdLiquido = id
            li.eliminar()
            return redirect(url_for('consultaGeneralLiquidos'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))
# fin del crud de Liquidos
#########################################
#########################################

#########################################
#########################################
# Rutas para el CRUD de la tabla Maestros
@app.route('/maestros/new')
@login_required
def nuevoMaestro():
    if current_user.Tipo=="L":
        return render_template('Maestros/altaMaestro.html')
    else:
        return redirect(url_for("inicio"))

@app.route('/maestros/save',methods=['POST'])
@login_required
def guardarMaestro():
    if current_user.Tipo=="L":
        try:
            m = Maestro()
            m.IdMaestro=request.form['idmaestro']
            m.IdUsuario=request.form['idusuario']
            m.insertar()
            return redirect(url_for('consultaGeneralMaestros'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/maestros')
@login_required
def consultaGeneralMaestros():
    if current_user.Tipo=="L":
        try:
            m = Maestro()
            m = m.consultaGeneral()
            return render_template('Maestros/consultaMaestro.html', Maestros=m)
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/maestros/<int:id>')
@login_required
def consultarMaestros(id):
    if current_user.Tipo=="L": 
        try:
            m = Maestro()
            m.IdMaestro = id
            m = m.consultaIndividual()
            return render_template('Maestros/modificarMaestro.html', Maestro=m)
        except:
            abort(400)
    else:
        return redirect(url_for("inicio"))
        
@app.route('/maestros/modificar', methods=['POST'])
@login_required
def actualizarMaestro():
    if current_user.Tipo=="L":
        try:
            m = Maestro()
            m.IdMaestro=request.form['idmaestro']
            m.IdUsuario=request.form['idusuario']
            m.actualizar()
            return redirect(url_for('consultaGeneralMaestros'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/maestros/delete/<int:id>')
@login_required
def eliminarMaestro(id):
    if current_user.Tipo=="L":
        try:
            m = Maestro()
            m.IdMaestro = id
            m.eliminar()
            return redirect(url_for('consultaGeneralMaestros'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

# fin del crud de Maestros
#########################################
#########################################

#########################################
#########################################
# Rutas para el CRUD de la tabla ReactivosLaboratorio
@app.route('/reactivos/new')
@login_required
def nuevoReactivo():
    if current_user.Tipo=="L":
        return render_template('ReactivosLaboratorio/altaReactivo.html')
    else:
        return redirect(url_for("inicio"))

@app.route('/reactivos/save',methods=['POST'])
@login_required
def guardarReactivo():
    if current_user.Tipo=="L":
        try:
            r = ReactivoLaboratorio()
            r.IdReactivo=request.form['idreactivo']
            r.IdLaboratorio=request.form['idlaboratorio']
            r.NombreReactivo=request.form['nombre']
            r.Formula=request.form['formula']
            r.PMolecular=request.form['pmolecular']
            r.Cantidad=request.form['cantidad']
            r.Contenido=request.form['contenido']
            r.ColorAlmacenaje=request.form['color']
            r.insertar()
            return redirect(url_for('consultaGeneralReactivos'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))
@app.route('/reactivos')
@login_required
def consultaGeneralReactivos():
    if current_user.Tipo=="L":
        try:
            r = ReactivoLaboratorio()
            r = r.consultaGeneral()
            return render_template('ReactivosLaboratorio/consultaReactivo.html', Reactivos=r)
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/reactivos/<int:id>')
@login_required
def consultarReactivos(id):
    if current_user.Tipo=="L":
        try:
            r = ReactivoLaboratorio()
            r.IdReactivo = id
            r = r.consultaIndividual()
            return render_template('ReactivosLaboratorio/modificarReactivo.html', Reactivo=r)
        except:
            abort(400)
    else:
        return redirect(url_for("inicio"))

@app.route('/reactivos/modificar', methods=['POST'])
@login_required
def actualizarReactivo():
    if current_user.Tipo=="L":
        try:
            r = ReactivoLaboratorio()
            r.IdReactivo=request.form['idreactivo']
            r.IdLaboratorio=request.form['idlaboratorio']
            r.NombreReactivo=request.form['nombre']
            r.Formula=request.form['formula']
            r.PMolecular=request.form['pmolecular']
            r.Cantidad=request.form['cantidad']
            r.Contenido=request.form['contenido']
            r.ColorAlmacenaje=request.form['color']
            r.actualizar()
            return redirect(url_for('consultaGeneralReactivos'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/reactivos/delete/<int:id>')
@login_required
def eliminarReactivo(id):
    if current_user.Tipo=="L":
        try:
            r = ReactivoLaboratorio()
            r.IdReactivo = id
            r.eliminar()
            return redirect(url_for('consultaGeneralReactivos'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))
# fin del crud de ReactivosLaboratorio
#########################################
#########################################

#########################################
#########################################
# Rutas para el CRUD de la tabla RegistroPracticas
@app.route('/practicas/new')
@login_required
def nuevaPractica():
    if current_user.Tipo!="A":
        return render_template('RegistroPracticas/altaPractica.html')
    else:
        return redirect(url_for("inicio"))

@app.route('/practicas/save',methods=['POST'])
@login_required
def guardarPractica():
    if current_user.Tipo!="A":
        try:
            p = RegistroPractica()
            p.IdPractica=request.form['idpractica']
            p.IdLaboratorio=request.form['idlaboratorio']
            p.IdMaestro=request.form['idmaestro']
            p.NombrePractica=request.form['nombre']
            p.Descripcion=request.form['descripcion']
            p.Semestre=request.form['semestre']
            p.CicloEscolar=request.form['ciclo']
            p.FechaPractica=request.form['fecha']
            p.HoraInicio=request.form['horai']
            p.HoraFin=request.form['horaf']
            p.Estatus=request.form['estatus']
            p.insertar()
            return redirect(url_for('consultaGeneralPracticas'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))     

@app.route('/practicas')
@login_required
def consultaGeneralPracticas():
    if current_user.Tipo!="A":
        try:
            p = RegistroPractica()
            p = p.consultaGeneral()
            return render_template('RegistroPracticas/consultaPractica.html', Practicas=p)
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/practicas/<int:id>')
@login_required
def consultarPracticas(id):
    if current_user.Tipo!="A":
    
        try:
            p = RegistroPractica()
            p.IdPractica = id
            p = p.consultaIndividual()
            return render_template('RegistroPracticas/modificarPractica.html', Practica=p)
        except:
            abort(400)
    else:
        return redirect(url_for("inicio"))

@app.route('/practicas/modificar', methods=['POST'])
@login_required
def actualizarPractica():
    if current_user.Tipo!="A":
        try:
            p = RegistroPractica()
            p.IdPractica=request.form['idpractica']
            p.IdLaboratorio=request.form['idlaboratorio']
            p.IdMaestro=request.form['idmaestro']
            p.NombrePractica=request.form['nombre']
            p.Descripcion=request.form['descripcion']
            p.Semestre=request.form['semestre']
            p.CicloEscolar=request.form['ciclo']
            p.FechaPractica=request.form['fecha']
            p.HoraInicio=request.form['horai']
            p.HoraFin=request.form['horaf']
            p.Estatus=request.form['estatus']
            p.actualizar()
            return redirect(url_for('consultaGeneralPracticas'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/practicas/delete/<int:id>')
@login_required
def eliminarPractica(id):
    if current_user.Tipo!="A":
        try:
            p = RegistroPractica()
            p.IdPractica = id
            p.eliminar()
            return redirect(url_for('consultaGeneralPracticas'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))
# fin del crud de RegistroPracticas
#########################################
#########################################


#########################################
#########################################
# Rutas para el CRUD de la tabla Materiales
@app.route('/materiales/new')
@login_required
def nuevoMaterial():
    if current_user.Tipo!="A":
        try:
            p = RegistroPractica()
            p = p.consultaGeneral()
            l = LiquidoLaboratorio()
            l = l.consultaGeneral()
            r = ReactivoLaboratorio()
            r = r.consultaGeneral()
            e = EquipoInventario()
            e = e.consultaGeneral()
            return render_template('MaterialNecesario/altaMaterial.html',Practicas=p,Equipos=e,Liquidos=l,Reactivos=r)
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/materiales/save',methods=['POST'])
@login_required
def guardarMaterial():
    if current_user.Tipo!="A":
        try:
            ma = Material()
            ma.IdPractica=request.form['idpractica']
            ma.Materiales=request.form['material']
            ma.insertar()
            return redirect(url_for('consultaGeneralMateriales'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/materiales')
@login_required
def consultaGeneralMateriales():
    if current_user.Tipo!="A":
        try:
            ma = Material()
            ma = ma.consultaGeneral()
            return render_template('MaterialNecesario/consultaMaterial.html', Materiales=ma)
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))   

@app.route('/materiales/<int:id>')
@login_required
def consultarMaterial(id):
    if current_user.Tipo!="A":
        try:
            ma = Material()
            ma.IdMaterial = id
            ma = ma.consultaIndividual()
            p = RegistroPractica()
            p = p.consultaGeneral()
            l = LiquidoLaboratorio()
            l = l.consultaGeneral()
            r = ReactivoLaboratorio()
            r = r.consultaGeneral()
            e = EquipoInventario()
            e = e.consultaGeneral()
            return render_template('MaterialNecesario/modificarMaterial.html', Material=ma,Practicas=p,Equipos=e,Liquidos=l,Reactivos=r)
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/materiales/modificar', methods=['POST'])
@login_required
def actualizarMaterial():
    if current_user.Tipo!="A":
        try:
            ma = Material()
            ma.IdMaterial=request.form['idmaterial']
            ma.IdPractica=request.form['idpractica']
            ma.Materiales=request.form['material']
            ma.actualizar()
            return redirect(url_for('consultaGeneralMateriales'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

@app.route('/materiales/delete/<int:id>')
@login_required
def eliminarMaterial(id):
    if current_user.Tipo!="A":
        try:
            ma = Material()
            ma.IdMaterial = id
            ma.eliminar()
            return redirect(url_for('consultaGeneralMateriales'))
        except:
            abort(500)
    else:
        return redirect(url_for("inicio"))

# fin del crud de MaterialNecesario
#########################################
#########################################
@app.errorhandler(400)
def error_400(e):
    return render_template('Comunes/error404.html',mensaje='La pagina que buscas No Existe en esta plataforma'),400

@app.errorhandler(404)
def error_404(e):
    return render_template('Comunes/error404.html',mensaje='La pagina que buscas No Existe en esta plataforma'),404

@app.errorhandler(500)
def error_500(e):
    return render_template('Comunes/error500.html',mensaje='Introdujiste información errónea en algunos campos'),500

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)