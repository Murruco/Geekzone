from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

conec = 'mysql://root:1234@localhost:3306/geekzone'
# config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

engine = create_engine(conec)

db = scoped_session(sessionmaker(bind=engine))

Base.metadata.create_all(engine)
