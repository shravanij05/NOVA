from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)  
    role = Column(String(10), nullable=False) 


DATABASE_URL = "mysql+mysqlconnector://root:ShravaniSJ@localhost/GradeBook"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
