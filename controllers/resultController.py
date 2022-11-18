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
            return self.resultRepository.save(newResult), 200
        except:
            return {"message": "El Candidato y/o Mesa no existen"}, 400

    def show(self, id):
        try:
            theResult = Result(self.resultRepository.findById(id))
            return theResult.__dict__, 200
        except:
            return {"message": "El Resultado no existe"}, 400

    def update(self, id, theResult):
        try:
            candidate = self.candidateRepository.findById(theResult["id_candidate"])
            table = self.tableRepository.findById(theResult["id_table"])
            model = Result(theResult)
            return self.resultRepository.update(id, model), 200
        except:
            return "El Candidato, Mesa y/o Resultado No Existen", 400

    def delete(self, id):
        try:
            return self.resultRepository.delete(id), 200
        except:
            return {"message": "El Resultado no existe"}, 400
