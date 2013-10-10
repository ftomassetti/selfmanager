from bottle import route, run, template
from model import Project
import app

app = app.instance

@app.route("/")
def projects_list():
    return template('templates/projects_list',projects=Project.all())

@app.route("/create/<project_name>")
def create_project(project_name):
	p=Project.exist(project_name)
	if p:
		return "Project %s already exist, ID:%d" % (project_name,p.id)
	else:
		p = Project.create(project_name)
		return "Create %s, ID: %d" % (project_name, p.id)

if __name__ == "__main__":	
    run(app,host='localhost',port=8080)