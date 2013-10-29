from app import db
from datetime import date, datetime
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

ROLE_USER  = 0
ROLE_ADMIN = 1

class User(db.Model):
    id       = db.Column(db.Integer, primary_key = True)
    name     = db.Column(db.String(128), index = True)
    login    = db.Column(db.String(80), index = True, unique = True)
    email    = db.Column(db.String(120), index = True, unique = True)
    role     = db.Column(db.SmallInteger, default = ROLE_USER)
    password = db.Column(db.String(64))

    def is_admin(self):
    	return self.role==ROLE_ADMIN

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    @classmethod
    def get_all(self):
        return db.session.query(self).all()

    @classmethod
    def get_by_id(self, id):
        return db.session.query(self).filter_by(id=id).first()


    # Required for administrative interface
    def __unicode__(self):
        return self.name + "<" + self.email + ">"

    def __repr__(self):
        return '<User %r>' % (self.email)

class Project(db.Model):
    id    = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True)

    @staticmethod
    def all():
        session = Session()
        return session.query(Project);

    @staticmethod
    def exist(_title):
        session = Session()
        return session.query(Project).filter_by(title=_title).first()

    @staticmethod   
    def create(_title):
        session = Session()
        instance = Project(title=_title)
        session.add(instance)
        session.commit()
        return instance

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '[Project title:%r]' % self.title