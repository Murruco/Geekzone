#from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey

#db = SQLAlchemy()

Base = declarative_base()


class Usuario(Base):

    __tablename__ = 'usuarios'

    id_usuario = Column(Integer, primary_key=True)
    correo = Column(String(100))
    user = Column(String(25))
    password = Column(String(66))
    fechaNacimiento = Column(Date)
    fechaIngreso = Column(Date, default=datetime.datetime.now)
    foto = Column(Integer)
