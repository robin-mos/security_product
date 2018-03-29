# coding=utf-8


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, DateTime
from sqlalchemy.orm import relationship, sessionmaker
from model.config import database_config

#engine = create_engine(database_config['engine_url'])
DbBase = declarative_base()


class User(DbBase):
	__tablename__ = 'users'

	id = Column(Integer, primary_key = True)
	username = Column(String(64), nullable = False, index = True)
	password = Column(String(64), nullable = False)
	email = Column(String(64), nullable = False, index = True)
	datetime = Column(String(64), nullable = False)

	def __repr__(self):
		return '%s(%r)'%(self.__class__.__name__, self.username)
