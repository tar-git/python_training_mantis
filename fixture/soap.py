from suds.client import Client
from suds import WebFault
from model.project_model import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.3.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_user_accessible_projects(self, username, password):
        client = Client("http://localhost/mantisbt-1.3.20/api/soap/mantisconnect.php?wsdl")
        projects = client.service.mc_projects_get_user_accessible(username, password)
        return [Project(name=p.name, description=p.description) for p in projects]
