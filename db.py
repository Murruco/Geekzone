from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

conec = 'postgresql://zyxhbqhdkujzoe:1af89d0a3e20e4421c268fc853bc2118939471b25089c676de743cf3914954d0@ec2-3-231-82-226.compute-1.amazonaws.com:5432/ddoisa8eia5l0a'
# config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

engine = create_engine(conec)

db = scoped_session(sessionmaker(bind=engine))

Base.metadata.create_all(engine)

usuario = Usuario(
            correo="gabriel@gmail.com",
            user="form.username.data",
            password="orm.password.data",
            fechaNacimiento=datetime.datetime.now()
        )

db.add(usuario) 
db.commit()

 ##Base.metadata.create_all(engine)
