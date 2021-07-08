from model.project_model import Project


def test_create_project(app, config):
    username = config['webadmin']["username"]
    password = config['webadmin']["password"]
    old_projects = app.soap.get_user_accessible_projects(username, password)
    project_name = app.project.generate_new_name()
    project = Project(name=project_name, description='some description')
    app.project.create(project)
    new_projects = app.soap.get_user_accessible_projects(username, password)
    old_projects.append(project)
    assert sorted(old_projects, key=lambda p: p.name) == sorted(new_projects, key=lambda p: p.name)
