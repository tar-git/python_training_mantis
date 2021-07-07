from model.project_model import Project
import random


def test_delete_some_project(app):
    old_projects = app.project.get_project_list()
    if len(old_projects) == 0:
        app.project.create(Project(name=app.project.generate_new_name(), description='some description'))
        old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_by_name(project.name)
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert sorted(old_projects, key=lambda p: p.name) == sorted(new_projects, key=lambda p: p.name)
