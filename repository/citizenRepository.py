from models.citizen import Citizen
from repository.interfaceRepository import InterfaceRepository
from repository.tableRepository import TableRepository


class CitizenRepository(InterfaceRepository[Citizen]):

    def __init__(self):
        super().__init__()
        self.tableRepository = TableRepository()

    def findById(self, id):
        citizen = super().findById(id)

        table = self.tableRepository.findById(citizen["id_table"])
        del citizen["id_table"]
        citizen["table"] = table

        return citizen

    def findAll(self):
        citizens = super().findAll()
        for x in citizens:
            id_table = x["id_table"]
            del x["id_table"]
            x["table"] = self.tableRepository.findById(id_table)
        return citizens
