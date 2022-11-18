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
            return self.citizenRepository.save(newCitizen), 200
        except:
            return {"message": "La Mesa no existe"}, 400

    def show(self, id):
        try:
            theCitizen = Citizen(self.citizenRepository.findById(id))
            return theCitizen.__dict__, 200
        except:
            return {"message": "El Ciudadano no existe"}, 400

    def update(self, id, theCitizen):
        try:
            table = self.tableRepository.findById(theCitizen["id_table"])
            model = Citizen(theCitizen)
            return self.citizenRepository.update(id, model), 200
        except:
            return {"message": "La Mesa y/o Ciudadano no existen"}, 400

    def delete(self, id):
        try:
            return self.citizenRepository.delete(id), 200
        except:
            return {"message": "El Ciudadano no existe"}, 400
