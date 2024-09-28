
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)  
    role = Column(String(10), nullable=False)
    assignments = relationship("Assignment", back_populates="student")

class Assignment(Base):
    __tablename__ = 'assignments'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    class_name = Column(String(100), nullable=False)
    file_path = Column(String(255), nullable=False)
    status = Column(String(20), nullable=False)
    grade = Column(String(5))
    feedback = Column(String(500))
    submitted_at = Column(DateTime, default=datetime.utcnow)
    student = relationship("User", back_populates="assignments")


DATABASE_URL = "mysql+mysqlconnector://root:ShravaniSJ@localhost/GradeBook"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
