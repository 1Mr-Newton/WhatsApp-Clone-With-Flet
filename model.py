import os
from sqlalchemy import (
    create_engine,
    Integer,
    Text,
    Column,
    String,
    ForeignKey,
    Boolean
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
conn = 'sqlite:///'+os.path.join(BASE_DIR, 'database.db')
engine = create_engine(conn)
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True)
    username = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    img_src = Column(String)
    has_media = Column(Boolean, nullable=False, default=False)
    messages = relationship("Message", back_populates="user", cascade="all, delete-orphan")


class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer(), primary_key=True)
    text = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="messages")

def createdb():
    Base.metadata.create_all(engine)  # creates the database
    return True


# createdb()
session = sessionmaker()(bind=engine)
