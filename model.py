import bottle
from bottle import HTTPError
from bottle.ext import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base
import app

Base = declarative_base()
engine = create_engine('sqlite:////tmp/test.db', echo=True)

plugin = sqlalchemy.Plugin(
    engine, # SQLAlchemy engine created with create_engine function.
    Base.metadata, # SQLAlchemy metadata, required only if create=True.
    keyword='db', # Keyword used to inject session database in a route (default 'db').
    create=True, # If it is true, execute `metadata.create_all(engine)` when plugin is applied (default False).
    commit=True, # If it is true, plugin commit changes after route is executed (default True).
    use_kwargs=False # If it is true and keyword is not defined, plugin uses **kwargs argument to inject session database (default False).
)

app.instance.install(plugin)

class Project(Base):
	__tablename__ = 'project'
	id = Column(Integer, primary_key=True)
	title = Column(String(200), unique=True)

	@staticmethod
	def exist(db,_title):
		return db.query(Project).filter_by(title=_title).first()

	@staticmethod	
	def create(db,_title):
		instance = Project(title=_title)
		db.add(instance)
		db.commit()
		return instance

	def __init__(self, title):
		self.title = title

	def __repr__(self):
		return '[Project title:%r]' % self.title