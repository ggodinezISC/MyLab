/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     1/12/2020 15:56:00                          */
/*==============================================================*/
/*==============================================================*/
/* User: dbo                                                    */
/*==============================================================*/
create  database MyLab;
use MyLab;

/*==============================================================*/
/* Table: Botiquines                                                 */
/*==============================================================*/
create table Botiquines
(
   IdArticuloBotiquin           int auto_increment not null,
   IdLaboratorio          		int not null,
   NombreArtículo    			varchar(150) not null,
   Cantidad           			int,
   Capacidad              		varchar(150) not null,
   constraint pk_articulo_botiquin primary key (IdArticuloBotiquin)
);

/*==============================================================*/
/* Table: LiquidosLaboratorio                                       */
/*==============================================================*/
create table LiquidosLaboratorio
(
   IdLiquido      	int auto_increment not null,
   IdLaboratorio    int not null,
   MedioCultivo     varchar(150) not null,
   FechaCaducidad   date,
   Cantidad   		int not null,
   Capacidad   		varchar(50),
   constraint pk_liquidos_laboratorio primary key (IdLiquido)
);

/*==============================================================*/
/* Table: ReactivosLaboratorio                                               */
/*==============================================================*/
create table ReactivosLaboratorio
(
	IdReactivo     		int auto_increment not null,
    IdLaboratorio       int not null,
    NombreReactivo      varchar(100) not null,
	Formula      		varchar(50) not null,
	PMolecular      	varchar(50) not null,
    Cantidad   			int not null,
    Contenido      		varchar(10) not null,
    ColorAlmacenaje   	varchar(15) not null,
   constraint pk_reactivos_laboratorio primary key (IdReactivo),
   constraint uk_reactivos_NombreReactivo unique(NombreReactivo)
);

/*==============================================================*/
/* Table: EquiposInventario                                              */
/*==============================================================*/
create table EquiposInventario
(
   IdEquipo            	int auto_increment not null,
   IdLaboratorio        int not null,
   NombreEquipo         varchar(150),
   Cantidad             int not null,
   Descripcion          varchar(200),
   Foto         		varchar(500)  not null,
   constraint pk_equipos_inventario primary key (IdEquipo),
   constraint uk_nombreequipo_inventario unique(NombreEquipo)
);

/*==============================================================*/
/* Table: Laboratorios                                           */
/*==============================================================*/
create table Laboratorios
(
   IdLaboratorio        int auto_increment not null,
   NombreLaboratorio    varchar(100) not null,
   Edificio             char(30) not null,
   NumeroAula     		int not null,
   constraint pk_laboratorios primary key (IdLaboratorio),
   constraint uk_nombrelaboratorio_laboratorios unique(NombreLaboratorio)
);

/*==============================================================*/
/* Table: AlumnosAlimentarias                                             */
/*==============================================================*/
create table AlumnosAlimentarias
(
   NoControl         int not null,
   IdUsuario         int not null,
   Semestre          char(1) not null,
   Grupo             char(1) not null,
   constraint pk_nocontrol_alumnos primary key (NoControl),
   constraint uk_idusuario_Alumnos unique(IdUsuario)
);

/*==============================================================*/
/* Table: Maestros                                             */
/*==============================================================*/
create table Maestros
(
   IdMaestro         int auto_increment not null,
   IdUsuario         int not null,
   constraint pk_maestros primary key (IdMaestro),
   constraint uk_idusuario_Maestros unique(IdUsuario)
   
);

/*==============================================================*/
/* Table: Usuarios                                              */
/*==============================================================*/
create table Usuarios
(
   IdUsuario      		int auto_increment not null,
   NombreCompleto       varchar(150)not null,
   Telefono             char(12)not null,
   Email              	varchar(100)not null,
   Contrasenia			varchar(15)not null,
   Sexo                 varchar(9)not null,
   Tipo           		char(1)not null ,
   constraint pk_usuarios primary key (IdUsuario),
   constraint uk_email unique(Email),
   constraint uk_telefono unique(Telefono)
);

/*==============================================================*/
/* Table: MaterialNecesario                                             */
/*==============================================================*/
create table MaterialNecesario
(
   IdMaterial           int auto_increment not null,
   IdPractica           int not null,
   Materiales           varchar(500) not null,
   constraint pk_material primary key (IdMaterial)
);

/*==============================================================*/
/* Table: RegistroPracticas                                            */
/*==============================================================*/
create table RegistroPracticas
(
   IdPractica         int auto_increment not null,
   IdLaboratorio      int not null,
   IdMaestro          int not null,
   NombrePractica     varchar(200) not null,
   Descripcion        varchar(500) not null,
   Semestre           char(1) not null,
   CicloEscolar       varchar(12) not null,
   FechaPractica      date,
   HoraInicio         time,
   HoraFin            time,
   Estatus            varchar(15) not null,
   constraint pk_practicas primary key (IdPractica),
   constraint uk_nombre_practica unique (NombrePractica)
);



/*==============================================================*/
/* Restricciones FK	alter													                                             */
/*==============================================================*/
alter table LiquidosLaboratorio add constraint LiquidosLaboratorio_Laboratorio_FK foreign key (IdLaboratorio)
      references Laboratorios (IdLaboratorio);

alter table Botiquines add constraint Botiquines_Laboratorio_FK foreign key (IdLaboratorio)
      references Laboratorios (IdLaboratorio);

alter table ReactivosLaboratorio add constraint ReactivosLaboratorio_Laboratorio_FK foreign key (IdLaboratorio)
      references Laboratorios (IdLaboratorio);

alter table EquiposInventario add constraint EquiposInventario_Laboratorio_FK foreign key (IdLaboratorio)
      references Laboratorios (IdLaboratorio);

alter table AlumnosAlimentarias add constraint AlumnosAlimentarias_IdUsuario_FK foreign key (IdUsuario)
      references Usuarios (IdUsuario);

alter table Maestros add constraint Maestros_IdUsuario_FK foreign key (IdUsuario)
      references Usuarios (IdUsuario);

alter table RegistroPracticas add constraint RegistroPracticas_Laboratorio_FK foreign key (IdLaboratorio)
      references Laboratorios (IdLaboratorio);
      
alter table RegistroPracticas add constraint RegistroPracticas_IdMaestro_FK foreign key (IdMaestro)
      references Maestros (IdMaestro);
alter table MaterialNecesario add constraint MaterialPracticas_IdPractica_FK foreign key (IdPractica)
      references RegistroPracticas (IdPractica);
      
	show tables;
/*==============================================================*/
/* Creacion del Usuario para la conexion   y permisos                                         		 */
/*==============================================================*/
CREATE USER 'adminlaboratorio'@'localhost' IDENTIFIED BY 'hola.123';
GRANT ALL PRIVILEGES ON MyLab.Laboratorios TO 'AdminLaboratorio'@'localhost';
GRANT ALL PRIVILEGES ON MyLab.RegistroPracticas TO 'AdminLaboratorio'@'localhost';
GRANT ALL PRIVILEGES ON MyLab.MaterialNecesario TO 'AdminLaboratorio'@'localhost';
GRANT ALL PRIVILEGES ON MyLab.Maestros TO 'AdminLaboratorio'@'localhost';
GRANT ALL PRIVILEGES ON MyLab.Usuarios TO 'AdminLaboratorio'@'localhost';
GRANT ALL PRIVILEGES ON MyLab.AlumnosAlimentarias TO 'AdminLaboratorio'@'localhost';
GRANT ALL PRIVILEGES ON MyLab.LiquidosLaboratorio TO 'AdminLaboratorio'@'localhost';
GRANT ALL PRIVILEGES ON MyLab.Botiquines TO 'AdminLaboratorio'@'localhost';
GRANT ALL PRIVILEGES ON MyLab.ReactivosLaboratorio TO 'AdminLaboratorio'@'localhost';
GRANT ALL PRIVILEGES ON MyLab.EquiposInventario TO 'AdminLaboratorio'@'localhost';

insert into Usuarios(IdUsuario,NombreCompleto,Telefono,Email,Contrasenia,Sexo,Tipo) 
values(1,"Francisco Rodríguez Díaz","3931041660","administrador@gmail.com","Hola.123","H","L");