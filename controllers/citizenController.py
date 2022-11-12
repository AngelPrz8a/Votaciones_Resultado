from models.citizen import Citizen
from repository.citizenRepository import CitizenRepository
from repository.tableRepository import TableRepository

class CitizenController():

    def __init__(self):
        self.citizenRepository = CitizenRepository()
        self.tableRepository = TableRepository()

    def index(self):
        return self.citizenRepository.findAll()

    def create(self, theCitizen):
        try:
            table = self.tableRepository.findById(theCitizen["id_table"])
            newCitizen = Citizen(theCitizen)
            return self.citizenRepository.save(newCitizen)
        except:
            return "LA MESA NO EXISTE"

    def show(self, id):
        theCitizen = Citizen(self.citizenRepository.findById(id))
        return theCitizen.__dict__

    def update(self, id, theCitizen):
        try:
            table = self.tableRepository.findById(theCitizen["id_table"])
            model = Citizen(theCitizen)
            return self.citizenRepository.update(id, model)
        except:
            return "LA MESA NO EXISTE"

    def delete(self, id):
        return self.citizenRepository.delete(id)
