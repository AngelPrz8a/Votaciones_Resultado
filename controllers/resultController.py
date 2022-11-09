from models.result import Result


class ResultController():

    def __init__(self):
        print("Creando ResultController")

    def index(self):
        print("Listando todos los Resultados")

    def create(self, theResult):
        print("Creando un Resultado")

    def show(self, id):
        print("Mostrando un Resultado")

    def update(self, id, theResult):
        print("Actualizando Resultado con id ", id)

    def delete(self, id):
        print("Eliminando Resultado con id ", id)