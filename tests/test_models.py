import os
from app import app,db
from app.models import *
from unittest import TestCase, main

basedir = os.path.abspath(os.path.dirname(__file__))

class TestModels(TestCase):

	def setUp(self):
		pass
		app.config['TESTING'] = True
		app.config['CSRF_ENABLED'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
		db.create_all()
		normal_user = User() 
		normal_user.role = ROLE_USER
		normal_user.name = "Normal User"
		db.session.add(normal_user)
		boss = User()
		boss.role = ROLE_ADMIN
		boss.name = "The Boss"
		db.session.add(boss)
		db.session.commit()

	def tearDown(self):
	    db.session.remove()
	    db.drop_all()

	def test_user_get_all(self):
		self.assertEqual(2,len(User.get_all()))

	def test_user_get_id(self):
		nu = User.get_by_id(1)	
		self.assertEqual('Normal User',nu.name)	

if __name__ == '__main__':
	main()