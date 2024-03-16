from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import logging

DATABASE_URL = 'mysql://root:Toast13?@localhost:3306/epicevents'

engine = create_engine(DATABASE_URL, echo=False)
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
