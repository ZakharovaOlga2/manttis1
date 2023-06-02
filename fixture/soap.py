from suds.client import Client
from suds import WebFault

class SoapHelper:

    def __init__(self, app, username, password, wsdl):
        self.app = app
        self.username = username
        self.password = password
        self.wsdl = wsdl

    def can_login(self):
        client = Client(self.wsdl)
        try:
            client.service.mc_login(self.username, self.password)
        except WebFault:
            return False
        return True

    def is_project_exists(self, project_name):
        client = Client(self.wsdl)
        id = 0
        try:
           id = client.service.mc_project_get_id_from_name(self.username, self.password, project_name)
        except WebFault:
            return False
        return (id>0)

    def get_project_list(self):
        client = Client(self.wsdl)
        pr_list = []
        try:
           for proj in client.service.mc_projects_get_user_accessible(self.username, self.password):
               pr_list.append(proj.name)
        except WebFault:
            return False
        return list(pr_list)