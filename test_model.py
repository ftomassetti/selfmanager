import unittest

import model
from model import Project
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine

class ModelTest(unittest.TestCase):

    def setUp(self):
        engine = create_engine('sqlite:///:memory:')
        Session = sessionmaker(bind=engine)
        self.session = Session()

        # You probably need to create some tables and 
        # load some test data, do so here.

        # To create tables, you typically do:
        model.Base.metadata.create_all(engine)
        #self.session.metadata.create_all(engine)

    def teardown(self):
        self.session.remove()

    def test_something(self):
        self.assertEqual(0, len(self.session.query(model.Project).all()))
        self.session.add(Project(title="Pippo"))
        self.assertEqual(1, len(self.session.query(model.Project).all()))        
        self.session.commit()
        self.assertEqual(1, len(self.session.query(model.Project).all()))        

def main():
    unittest.main()

if __name__ == '__main__':
    main()        