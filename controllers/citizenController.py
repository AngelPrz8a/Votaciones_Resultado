from models.citizen import Citizen
from repository.citizenRepository import CitizenRepository

class CitizenController():

    def __init__(self):
        self.citizenRepository = CitizenRepository()

    def index(self):
        return self.citizenRepository.findAll()

    def create(self, theCitizen):
        newCitizen = Citizen(theCitizen)
        return self.citizenRepository.save(newCitizen)

    def show(self, id):
        theCitizen = Citizen(self.citizenRepository.findById(id))
        return theCitizen.__dict__

    def update(self, id, theCitizen):
        actualCitizen = Citizen(self.citizenRepository.findById(id))
        actualCitizen.name = theCitizen["name"]
        actualCitizen.lastname = theCitizen["lastname"]
        actualCitizen.identification = theCitizen["identification"]
        return self.citizenRepository.save(actualCitizen)

    def delete(self, id):
        return self.citizenRepository.delete(id)
