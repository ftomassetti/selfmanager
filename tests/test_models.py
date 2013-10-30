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
		
		# users
		normal_user = User() 
		normal_user.role = ROLE_USER
		normal_user.name = "Normal User"
		db.session.add(normal_user)
		boss = User()
		boss.role = ROLE_ADMIN
		boss.name = "The Boss"
		db.session.add(boss)

		# tasks
		task1 = Task('task1')
		task1.owners.append(normal_user)
		db.session.add(task1)
		task2 = Task('task2')
		task2.owners.append(normal_user)
		task2.owners.append(boss)
		db.session.add(task2)
		task3 = Task('task3')
		db.session.add(task3)

		db.session.commit()

	def tearDown(self):
	    db.session.remove()
	    db.drop_all()

	def test_user_get_all(self):
		self.assertEqual(2,len(User.get_all()))

	def test_user_get_id(self):
		nu = User.get_by_id(1)	
		self.assertEqual('Normal User',nu.name)	

	def test_task_owned_by(self):
		nu = User.get_by_id(1)	
		tasks = Task.owned_by(nu)
		self.assertEqual(2,len(tasks))
		self.assertNotEqual([],[t for t in tasks if t.summary=='task1'])
		self.assertNotEqual([],[t for t in tasks if t.summary=='task2'])
		self.assertEqual([],[t for t in tasks if t.summary=='task3'])

if __name__ == '__main__':
	main()