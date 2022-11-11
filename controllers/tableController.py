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
        theTable = Table(self.tableRepository.findById(id))
        return theTable.__dict__

    def update(self, id, theTable):
        actualTable = Table(self.tableRepository.findById(id))
        actualTable.tableNumber = theTable["tableNumber"]
        actualTable.documentsCount = theTable["documentsCount"]
        return self.tableRepository.save(actualTable)

    def delete(self, id):
        return self.tableRepository.delete(id)