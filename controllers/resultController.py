from models.result import Result
from repository.resultRepository import ResultRepository

class ResultController():

    def __init__(self):
        self.resultRepository = ResultRepository()

    def index(self):
        return self.resultRepository.findAll()

    def create(self, theResult):
        newResult = Result(theResult)
        return self.resultRepository.save(newResult)

    def show(self, id):
        theResult = Result(self.resultRepository.findById(id))
        return theResult.__dict__

    def update(self, id, theResult):
        actualResult = Result(self.resultRepository.findById(id))
        actualResult.countVotes = theResult["countVotes"]
        return self.resultRepository.save(actualResult)

    def delete(self, id):
        return self.resultRepository.delete(id)