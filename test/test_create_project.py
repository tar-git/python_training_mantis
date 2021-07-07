from model.project_model import Project


def test_create_project(app):
    old_projects = app.project.get_project_list()
    project_name = app.project.generate_new_name()
    project = Project(name=project_name, description='some description')
    app.project.create(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=lambda p: p.name) == sorted(new_projects, key=lambda p: p.name)
