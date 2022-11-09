from models.tableModel import TableModel


class TableController():

    def __init__(self):
        print("Creando TableController")

    def index(self):
        print("Listando todos las Mesas")

    def create(self, theTable):
        print("Creando una Mesa")

    def show(self, id):
        print("Mostrando una Mesa")

    def update(self, id, theTable):
        print("Actualizando Mesa con id ", id)

    def delete(self, id):
        print("Eliminando Mesa con id ", id)