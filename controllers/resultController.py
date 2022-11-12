from models.result import Result
from repository.resultRepository import ResultRepository
from repository.tableRepository import TableRepository
from repository.candidateRepository import CandidateRepository

class ResultController():

    def __init__(self):
        self.resultRepository = ResultRepository()
        self.tableRepository = TableRepository()
        self.candidateRepository = CandidateRepository()

    def index(self):
        return self.resultRepository.findAll()

    def create(self, theResult):
        try:
            candidate = self.candidateRepository.findById(theResult["id_candidate"])
            table = self.tableRepository.findById(theResult["id_table"])
            newResult = Result(theResult)
            return self.resultRepository.save(newResult)
        except:
            return "El Candidato y/o Mesa No Existen"

    def show(self, id):
        theResult = Result(self.resultRepository.findById(id))
        return theResult.__dict__

    def update(self, id, theResult):
        try:
            candidate = self.candidateRepository.findById(theResult["id_candidate"])
            table = self.tableRepository.findById(theResult["id_table"])
            model = Result(theResult)
            return self.resultRepository.update(id, model)
        except:
            return "El Candidato y/o Mesa No Existen"

    def delete(self, id):
        return self.resultRepository.delete(id)