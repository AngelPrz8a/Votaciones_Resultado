from models.candidate import Candidate
from repository.candidateRepository import CandidateRepository


class CandidateController():

    def __init__(self):
        self.candidateRepository = CandidateRepository()

    def index(self):
        return self.candidateRepository.findAll()

    def create(self, theCandidate):
        newCandidate = Candidate(theCandidate)
        return self.candidateRepository.save(newCandidate)

    def show(self, id):
        theCandidate = Candidate(self.candidateRepository.findById(id))
        return theCandidate.__dict__

    def update(self, id, theCandidate):
        actualCandidate = Candidate(self.candidateRepository.findById(id))
        actualCandidate.resolution = theCandidate["resolution"]
        actualCandidate.identification = theCandidate["identification"]
        actualCandidate.name = theCandidate["name"]
        actualCandidate.lastname = theCandidate["lastname"]
        return self.candidateRepository.update(id, actualCandidate)

    def delete(self, id):
        return self.candidateRepository.delete(id)
