from models.table import Table
from repository.tableRepository import TableRepository


class TableController():

    def __init__(self):
        self.tableRepository = TableRepository()

    def index(self):
        return self.tableRepository.findAll()

    def create(self, theTable):
        newTable = Table(theTable)
        return self.tableRepository.save(newTable)

    def show(self, id):
        try:
            theTable = Table(self.tableRepository.findById(id))
            return theTable.__dict__, 200
        except:
            return {"message": "La Mesa no existe"}, 400

    def update(self, id, theTable):
        try:
            model = Table(theTable)
            return self.tableRepository.update(id, model), 200
        except:
            return {"message": "La Mesa no existe"}, 400

    def delete(self, id):
        try:
            return self.tableRepository.delete(id), 200
        except:
            return {"message": "La Mesa no existe"}, 400
