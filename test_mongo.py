"""
import pymongo


client = pymongo.MongoClient("mongodb+srv://meph:xwXuuY4s7aCjrEe@cluster0.lttmqg6.mongodb.net/resultados-db?retryWrites=true&w=majority")

res_db = client["resultados-db"]
print(res_db.list_collection_names())
"""

"""
from repository.citizenRepository import CitizenRepository

repoCitizen = CitizenRepository()
"""

"""
from repository.matchRepository import MatchRepository
from models.match import Match
repoMatch = MatchRepository()

match1 = Match(
    {
        "nombre": "partido azul",
        "lema": "El liberalismo es el respeto irrestrico del proyecto de vida del prójimo, basado en el principio de no agresión (PNA) y en defensa del derecho a la vida, la libertad y la propiedad privada... "
    }
)

repoMatch.save(match1)
"""

"""
from repository.matchRepository import MatchRepository
from models.match import Match
repoMatch = MatchRepository()

repoMatch.delete("636c0c8ed673ded5a16e80b4")
"""
