from app import db
from datetime import date, datetime
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

ROLE_USER  = 0
ROLE_ADMIN = 1

class IdMixin(object):
    def get_id(self):
        return self.id

class GetMixin(object):
    @classmethod
    def get_all(self):
        return db.session.query(self).all()

    @classmethod
    def get_by_id(self, id):
        return db.session.query(self).filter_by(id=id).first()

tasks_owners = db.Table('tasks_owners', db.Model.metadata,
    db.Column('task_id', db.Integer,  db.ForeignKey('task.id')),
    db.Column('owner_id', db.Integer, db.ForeignKey('user.id'))
)        

class User(db.Model, IdMixin, GetMixin):
    id       = db.Column(db.Integer, primary_key = True)
    name     = db.Column(db.String(128), index = True)
    login    = db.Column(db.String(80), index = True, unique = True)
    email    = db.Column(db.String(120), index = True, unique = True)
    role     = db.Column(db.SmallInteger, default = ROLE_USER)
    password = db.Column(db.String(64))
    owned_tasks = db.relationship('Task',secondary="tasks_owners",backref='owners')

    def is_admin(self):
        return self.role==ROLE_ADMIN

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    # Required for administrative interface
    def __unicode__(self):
        return self.name + "<" + self.email + ">"

    def __repr__(self):
        return '<User %r>' % (self.email)


class Task(db.Model, IdMixin, GetMixin):
    id      = db.Column(db.Integer, primary_key=True)
    summary = db.Column(db.String(200), unique=True)
#    owners  = db.relationship('User',secondary="tasks_owners",backref='owned_tasks')

    def __init__(self,summary):
        self.summary = summary

    @classmethod
    def owned_by(self,user):
        clause = Task.owners.contains(user)
        return db.session.query(Task).filter(clause).all()