from models.candidate import Candidate
from repository.interfaceRepository import InterfaceRepository
from repository.matchRepository import MatchRepository

class CandidateRepository(InterfaceRepository[Candidate]):

    def __init__(self):
        super().__init__()
        self.matchRepository = MatchRepository()

    def findById(self, id):
        candidate = super().findById(id)
        match = self.matchRepository.findById(candidate["id_match"])
        del candidate["id_match"]
        candidate["match"] = match
        return candidate

    def findAll(self):
        candidatos = super().findAll()
        for x in candidatos:
            id_match = x["id_match"]
            del x["id_match"]
            x["match"] = self.matchRepository.findById(id_match)
        return candidatos
