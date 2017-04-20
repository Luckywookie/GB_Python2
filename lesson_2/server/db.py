from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('sqlite:///data.db', echo=True)
Base.metadata.create_all(engine)
Sess = sessionmaker(bind=engine)
session = Sess()



