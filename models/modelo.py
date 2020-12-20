from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time
from flask_login import UserMixin
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Usuario(UserMixin, db.Model):
    __tablename__ = 'Usuarios'
    IdUsuario = Column(Integer, primary_key=True)
    NombreCompleto = Column(String, nullable=False)
    Telefono = Column(String, nullable=False)
    Email = Column(String, nullable=False)
    Contrasenia = Column(String, nullable=False)
    Sexo = Column(String, nullable=False)
    Tipo = Column(String, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        usua = self.query.all()
        return usua
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        usu = self.consultaIndividual()
        db.session.delete(usu)
        db.session.commit()
    def consultaIndividual(self):
        usu = self.query.get(self.IdUsuario)
        return usu
    @property
    def password(self):
        raise AttributeError('El atributo password no es de lectura')
    def validarPassword(self, Contrasenia):
        pwd = self.query.filter_by(Contrasenia=Contrasenia).first()
        print(Contrasenia)
        return pwd
    def is_authenticated(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.IdUsuario
    def validar(self, Email, Contrasenia):
        user = Usuario.query.filter_by(Email=Email).first()
        if user != None:
            if user.validarPassword(Contrasenia):
                return user
        else:
            return None

class Botiquin(db.Model):
    __tablename__ = 'Botiquines'
    IdArticuloBotiquin = Column(Integer, primary_key=True)
    IdLaboratorio = Column(Integer, ForeignKey('Laboratorios.IdLaboratorio'))
    NombreArtículo = Column(String, nullable=False)
    Cantidad = Column(Integer, nullable=False)
    Capacidad = Column(String, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        botoquines = self.query.all()
        return botoquines

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        botiquin = self.consultaIndividual()
        db.session.delete(botiquin)
        db.session.commit()

    def consultaIndividual(self):
        botiquin = self.query.get(self.IdArticuloBotiquin)
        return botiquin

class LiquidoLaboratorio(db.Model):
    __tablename__ = 'LiquidosLaboratorio'
    IdLiquido = Column(Integer, primary_key=True)
    IdLaboratorio = Column(Integer, ForeignKey('Laboratorios.IdLaboratorio'))
    MedioCultivo = Column(String, nullable=False)
    FechaCaducidad = Column(Date, nullable=False)
    Cantidad = Column(Integer, nullable=False)
    Capacidad = Column(String, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        liquidos = self.query.all()
        return liquidos

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        liquido = self.consultaIndividual()
        db.session.delete(liquido)
        db.session.commit()

    def consultaIndividual(self):
        liquido = self.query.get(self.IdLiquido)
        return liquido

class ReactivoLaboratorio(db.Model):
    __tablename__ = 'ReactivosLaboratorio'
    IdReactivo = Column(Integer, primary_key=True)
    IdLaboratorio = Column(Integer, ForeignKey('Laboratorios.IdLaboratorio'))
    NombreReactivo = Column(String, nullable=False)
    Formula = Column(String, nullable=False)
    PMolecular = Column(String, nullable=False)
    Cantidad = Column(Integer, nullable=False)
    Contenido = Column(String, nullable=False)
    ColorAlmacenaje = Column(String, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        reactivos = self.query.all()
        return reactivos

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        reactivo = self.consultaIndividual()
        db.session.delete(reactivo)
        db.session.commit()

    def consultaIndividual(self):
        reactiv = self.query.get(self.IdReactivo)
        return reactiv

class EquipoInventario(db.Model):
    __tablename__ = 'EquiposInventario'
    IdEquipo = Column(Integer, primary_key=True)
    IdLaboratorio = Column(Integer, ForeignKey('Laboratorios.IdLaboratorio'))
    NombreEquipo = Column(String, nullable=False)
    Cantidad = Column(Integer, nullable=False)
    Descripcion = Column(String, nullable=False)
    Foto = Column(String, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        equipos = self.query.all()
        return equipos
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        equipo = self.consultaIndividual()
        db.session.delete(equipo)
        db.session.commit()
    def consultaIndividual(self):
        equipo = self.query.get(self.IdEquipo)
        return equipo

class Laboratorio(db.Model):
    __tablename__ = 'Laboratorios'
    IdLaboratorio = Column(Integer, primary_key=True)
    NombreLaboratorio = Column(String, unique=True, nullable=False)
    Edificio = Column(String, nullable=False)
    NumeroAula = Column(Integer, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def consultaGeneral(self):
        labos = self.query.all()
        return labos

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self):
        labo = self.consultaIndividual()
        db.session.delete(labo)
        db.session.commit()

    def consultaIndividual(self):
        labos = self.query.get(self.IdLaboratorio)
        return labos

class AlumnoAlimentarias(db.Model):
    __tablename__ = 'AlumnosAlimentarias'
    NoControl = Column(Integer, primary_key=True)
    IdUsuario = Column(Integer,ForeignKey('Usuarios.IdUsuario'), nullable=False)
    Semestre = Column(String, nullable=False)
    Grupo = Column(String, nullable=False)

    def consultaGeneralConteo(self):
        alumnos = self.query.count()
        return alumnos
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        alumnos = self.query.all()
        return alumnos
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        alumno = self.consultaIndividual()
        db.session.delete(alumno)
        db.session.commit()
    def consultaIndividual(self):
        alumno = self.query.get(self.NoControl)
        return alumno

class Maestro(db.Model):
    __tablename__ = 'Maestros'
    IdMaestro = Column(Integer, primary_key=True)
    IdUsuario = Column(Integer,ForeignKey('Usuarios.IdUsuario'), unique=True, nullable=False)

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        maestros = self.query.all()
        return maestros
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        maestro = self.consultaIndividual()
        db.session.delete(maestro)
        db.session.commit()
    def consultaIndividual(self):
        maestro = self.query.get(self.IdMaestro)
        return maestro
    def consultaGeneralConteo(self):
        maestros = self.query.count()
        return maestros

class RegistroPractica(db.Model):
    __tablename__ = 'RegistroPracticas'
    IdPractica = Column(Integer, primary_key=True)
    IdLaboratorio = Column(Integer,ForeignKey('Laboratorios.IdLaboratorio'), nullable=False)
    IdMaestro = Column(Integer,ForeignKey('Maestros.IdMaestro'), nullable=False)
    NombrePractica = Column(String, nullable=False)
    Descripcion = Column(String, nullable=False)
    Semestre = Column(String, nullable=False)
    CicloEscolar = Column(String, nullable=False)
    FechaPractica = Column(Date, nullable=False)
    HoraInicio = Column(Time, nullable=False)
    HoraFin = Column(Time, nullable=False)
    Estatus = Column(String, nullable=False)
    Laboratorio=relationship('Laboratorio', foreign_keys=[IdLaboratorio])
    
    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        practicas = self.query.all()
        return practicas
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        practica = self.consultaIndividual()
        db.session.delete(practica)
        db.session.commit()
    def consultaIndividual(self):
        practica = self.query.get(self.IdPractica)
        return practica
    def consultaGeneralConteo(self):
        practicas = self.query.count()
        return practicas

class Material(db.Model):
    __tablename__ = 'MaterialNecesario'
    IdMaterial = Column(Integer, primary_key=True)
    IdPractica = Column(Integer, ForeignKey('RegistroPracticas.IdPractica'))
    Materiales = Column(String, nullable=False)
    Practica=relationship('RegistroPractica', foreign_keys=[IdPractica])

    def insertar(self):
        db.session.add(self)
        db.session.commit()
    def consultaGeneral(self):
        practicas = self.query.all()
        return practicas
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        practica = self.consultaIndividual()
        db.session.delete(practica)
        db.session.commit()
    def consultaIndividual(self):
        practica = self.query.get(self.IdMaterial)
        return practica