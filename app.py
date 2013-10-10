from bottle import Bottle, run

def create_app():
	app = Bottle(__name__)	
	return app

instance = create_app()