
from models.Project import Project, project_schema, projects_schema
from models.Technical_Skillset import Technical_Skillset, technical_skillet_schema, technical_skillets_schema
from flask import jsonify, make_response
from config import app


@app.route('/project')
def projects():
    projects = Project.query.filter_by(Title="Project 1").all()
    return projects_schema.dump(projects)

@app.route('/skills/<keyword>')
def search_project(keyword):
    projects = Technical_Skillset.query.filter(Technical_Skillset.Frontend.contains(keyword)).all()
    return technical_skillets_schema.dump(projects)