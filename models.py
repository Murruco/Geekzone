import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from werkzeug.security import generate_password_hash, check_password_hash


engine = create_engine('postgresql://nugmoxvbqiawgb:9f210c0ffbb8492d9628604a1bd68bf69ddfaadb57378fd5473dc3eb2227111d@ec2-34-233-115-14.compute-1.amazonaws.com:5432/db5llcgio2ts59')
db = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db.query_property()


class Usuario(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(Integer, primary_key=True)
    correo = Column(String(100), unique=True, nullable=False)
    user = Column(String(25), nullable=False)
    password = Column(String(172), nullable=False)
    fechaNacimiento = Column(Date, nullable=False)
    fechaIngreso = Column(DateTime, default=datetime.datetime.now, nullable=False)
    foto = Column(String(), nullable=True)
    publicacion = relationship('Publicacion')
    comentario = relationship('Comentario')

    def __init__(self, correo, user, password, fechaNacimiento):
        self.correo = correo
        self.user = user
        self.password = self.__create_password(password)
        self.fechaNacimiento = fechaNacimiento

    def __create_password(self, password):
        return generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)


class Publicacion(Base):
    __tablename__ = 'publicaciones'

    id_publicacion = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
    id_categoria = Column(Integer, ForeignKey('categorias.id_categoria'))
    titulo = Column(String(100), nullable=False)
    topic = Column(String(100), nullable=False)
    content = Column(Text(), nullable=False)
    pictures = Column(String(), nullable=True)
    fechaPublicacion = Column(DateTime, default=datetime.datetime.now)
    comentario = relationship('Comentario')


class Comentario(Base):
    __tablename__ = 'comentarios'

    id_comentario = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
    id_publicacion = Column(Integer, ForeignKey('publicaciones.id_publicacion'))
    comentario = Column(Text(), nullable=False)
    fechaComentario = Column(DateTime, default=datetime.datetime.now)


class Categoria(Base):

    __tablename__ = 'categorias'

    id_categoria = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(500), nullable=True)
    publicacion = relationship('Publicacion')


class Noticias(Base):
    __tablename__ = 'noticias'

    id_noticia = Column(Integer, primary_key=True)
    id_categoria = Column(Integer, ForeignKey('categorias.id_categoria'))
    titulo = Column(String(100), nullable=False)
    descripcion = Column(String(500), nullable=True)
    fechaPublicacion = Column(DateTime, default=datetime.datetime.now)
