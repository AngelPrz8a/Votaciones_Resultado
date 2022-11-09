from models.match import Match


class MatchController():

    def __init__(self):
        print("Creando MatchController")

    def index(self):
        print("Listando todos los Partidos")

    def create(self, theMatch):
        print("Creando un Partido")

    def show(self, id):
        print("Mostrando un Partido")

    def update(self, id, theMatchn):
        print("Actualizando Partido con id ", id)

    def delete(self, id):
        print("Eliminando Partido con id ", id)
