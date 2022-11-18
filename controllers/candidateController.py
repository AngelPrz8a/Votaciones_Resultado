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
            return self.candidateRepository.save(newCandidate), 200
        except:
            return {"message": "El Partido no existe"}, 400

    def show(self, id):
        try:
            theCandidate = Candidate(self.candidateRepository.findById(id))
            return theCandidate.__dict__, 200
        except:
            return {"message": "El Candidato no existe"}, 400

    def update(self, id, theCandidate):
        try:
            match = self.matchRepository.findById(theCandidate["id_match"])
            newCandidate = Candidate(theCandidate)
            return self.candidateRepository.update(id, newCandidate), 200
        except:
            return {"message": "El Partido y/o Candidato no existen"}, 400

    def delete(self, id):
        try:
            return self.candidateRepository.delete(id), 200
        except:
            return {"message": "El Candidato no existe"}, 400
