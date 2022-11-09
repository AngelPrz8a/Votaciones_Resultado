from models.candidate import Candidate


class CandidateController():

    def __init__(self):
        print("Creando CandidateController")

    def index(self):
        print("Listar todos los Candidatos")

    def create(self, theCandidate):
        print("Crear un Candidato")

    def show(self, id):
        print("Mostrando un Candidato")

    def update(self, id, theCandidate):
        print("Actualizando Candidato con id ", id)

    def delete(self, id):
        print("Elimiando Candidato con id ", id)
