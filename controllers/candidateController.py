from models.candidate import Candidate
from repository.candidateRepository import CandidateRepository
from repository.matchRepository import MatchRepository


class CandidateController():

    def __init__(self):
        self.candidateRepository = CandidateRepository()
        self.matchRepository = MatchRepository()

    def index(self):
        return self.candidateRepository.findAll()

    def create(self, theCandidate):
        try:
            match = self.matchRepository.findById(theCandidate["id_match"])
            newCandidate = Candidate(theCandidate)
            return self.candidateRepository.save(newCandidate)
        except:
            return "El Partido No Existe"

    def show(self, id):
        theCandidate = Candidate(self.candidateRepository.findById(id))
        return theCandidate.__dict__

    def update(self, id, theCandidate):
        model = Candidate(theCandidate)
        return self.candidateRepository.update(id, model)

    def delete(self, id):
        return self.candidateRepository.delete(id)
