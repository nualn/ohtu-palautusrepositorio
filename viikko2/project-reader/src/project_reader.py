from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # parsi merkkijono dict muotoon
        toml_obj = toml.loads(content)['tool']['poetry']
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(toml_obj['name'], toml_obj['description'], toml_obj['dependencies'], toml_obj['dev-dependencies'])
