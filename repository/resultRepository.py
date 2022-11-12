from models.result import Result
from repository.interfaceRepository import InterfaceRepository
from repository.candidateRepository import CandidateRepository
from repository.tableRepository import TableRepository


class ResultRepository(InterfaceRepository[Result]):

    def __init__(self):
        super().__init__()
        self.candidateRepository = CandidateRepository()
        self.tableRepository = TableRepository()

    def findById(self, id):
        result = super().findById(id)

        table = self.tableRepository.findById(result["id_table"])
        del result["id_table"]
        result["table"] = table

        candidate = self.candidateRepository.findById(result["id_candidate"])
        del result["id_candidate"]
        result["candidate"] = candidate

        return result

    def findAll(self):
        result = super().findAll()
        for x in result:
            id_table = x["id_table"]
            del x["id_table"]
            x["table"] = self.tableRepository.findById(id_table)

            id_candidate = x["id_candidate"]
            del x["id_candidate"]
            x["candidate"] = self.candidateRepository.findById(id_candidate)
        return result
