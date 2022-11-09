from models.citizenModel import CitizenModel


class CitizenController():

    def __init__(self):
        print("Creando CitizenController")

    def index(self):
        print("Listando todos los Ciudadanos")

    def create(self, theCitizen):
        print("Creando un Ciudadano")

    def show(self, id):
        print("Mostrando un Ciudadano")

    def update(self, id, theCitizen):
        print("Actualizando Ciudadano con id ", id)

    def delete(self, id):
        print("Eliminando Ciudadano con id ", id)
