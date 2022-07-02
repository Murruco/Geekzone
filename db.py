import os
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

conec = 'postgresql://nugmoxvbqiawgb:9f210c0ffbb8492d9628604a1bd68bf69ddfaadb57378fd5473dc3eb2227111d@ec2-34-233-115-14.compute-1.amazonaws.com:5432/db5llcgio2ts59'
# config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Base.metadata.create_all(engine)


def usuarios(form):
    usuario = Usuario(
        form.email.data,
        form.username.data,
        form.password.data,
        form.fecha_nacimiento.data
    )
    db.add(usuario)
    db.commit()


def publicaciones(form, id_usuario):
    publicacion = Publicacion(
        id_usuario=id_usuario,
        id_categoria=form.category.data,
        titulo=form.title.data,
        topic=form.topic.data,
        content=form.content.data,
        pictures=form.pictures.data
    )
    db.add(publicacion)
    db.commit()

'''
categorias1 = engine.execute("INSERT INTO categorias (nombre, descripcion) VALUES ('Juegos', 'VideoJuegos')")
categorias2 = engine.execute("INSERT INTO categorias (nombre, descripcion) VALUES ('Anime', 'Anime y manga')")
categorias3 = engine.execute("INSERT INTO categorias (nombre, descripcion) VALUES ('Comics', 'Marvel y DC')")
categorias4 = engine.execute("INSERT INTO categorias (nombre, descripcion) VALUES ('Series', 'Series y Peliculas')")
categorias5 = engine.execute("INSERT INTO categorias (nombre, descripcion) VALUES ('Tecnología', 'Tecnología')")
'''