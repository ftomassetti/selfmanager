from bottle import route, run, template
from model import Project
import app

app = app.instance

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/create/<project_name>")
def create_project(project_name,db):
	p=Project.exist(db,project_name)
	if p:
		return "Project %s already exist, ID:%d" % (project_name,p.id)
	else:
		p = Project.create(db,project_name)
		return "Create %s, ID: %d" % (project_name, p.id)

if __name__ == "__main__":	
    run(app,host='localhost',port=8080)