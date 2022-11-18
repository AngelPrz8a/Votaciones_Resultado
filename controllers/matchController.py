from repository.matchRepository import MatchRepository
from models.match import Match


class MatchController():

    def __init__(self):
        self.matchRepository = MatchRepository()

    def index(self):
        return self.matchRepository.findAll()

    def create(self, theMatch):
        newMatch = Match(theMatch)
        return self.matchRepository.save(newMatch)

    def show(self, id):
        try:
            theMatch = Match(self.matchRepository.findById(id))
            return theMatch.__dict__, 200
        except:
            return {"message": "El Partido no existe"}, 400

    def update(self, id, theMatch):
        try:
            model = Match(theMatch)
            return self.matchRepository.update(id, model), 200
        except:
            return {"message": "El Partido no existe"}, 400

    def delete(self, id):
        try:
            return self.matchRepository.delete(id), 200
        except:
            return {"message": "El Partido no existe"}, 400
