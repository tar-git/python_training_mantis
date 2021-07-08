from model.project_model import Project
import random


def test_delete_some_project(app, config):
    username = config['webadmin']["username"]
    password = config['webadmin']["password"]
    old_projects = app.soap.get_user_accessible_projects(username, password)
    if len(old_projects) == 0:
        app.project.create(Project(name=app.project.generate_new_name(), description='some description'))
        old_projects = app.soap.get_user_accessible_projects(username, password)
    project = random.choice(old_projects)
    app.project.delete_by_name(project.name)
    new_projects = app.soap.get_user_accessible_projects(username, password)
    old_projects.remove(project)
    assert sorted(old_projects, key=lambda p: p.name) == sorted(new_projects, key=lambda p: p.name)
