from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)

# Controllers
from controllers.matchController import MatchController
from controllers.candidateController import CandidateController
from controllers.citizenController import CitizenController
from controllers.resultController import ResultController
from controllers.tableController import TableController

matchC = MatchController()
candidateC = CandidateController()
citizenC = CitizenController()
resultC = ResultController()
tableC = TableController()


@app.route("/", methods=['GET'])
def test():
    json = {"message": "Server is running......."}
    return jsonify(json)


# -------------------------------- > Candidate
@app.route("/candidate", methods=['GET'])
def getAllCandidate():
    json = candidateC.index()
    return jsonify(json)


@app.route("/candidate", methods=['POST'])
def createCandidate():
    data = request.get_json()
    json = candidateC.create(data)
    return jsonify(json[0]), json[1]


@app.route("/candidate/<string:id>", methods=['GET'])
def getCandidate(id):
    json = candidateC.show(id)
    return jsonify(json[0]), json[1]


@app.route("/candidate/<string:id>", methods=['PUT'])
def updateCandidate(id):
    data = request.get_json()
    json = candidateC.update(id, data)
    return jsonify(json[0]), json[1]


@app.route("/candidate/<string:id>", methods=['DELETE'])
def deleteCandidate(id):
    json = candidateC.delete(id)
    return jsonify(json[0]), json[1]


# -------------------------------- > Citizen
@app.route("/citizen", methods=['GET'])
def getAllCitizen():
    json = citizenC.index()
    return jsonify(json)


@app.route("/citizen", methods=['POST'])
def createCitizen():
    data = request.get_json()
    json = citizenC.create(data)
    return jsonify(json[0]), json[1]


@app.route("/citizen/<string:id>", methods=['GET'])
def getCitizen(id):
    json = citizenC.show(id)
    return jsonify(json[0]), json[1]


@app.route("/citizen/<string:id>", methods=['PUT'])
def updateCitizen(id):
    data = request.get_json()
    json = citizenC.update(id, data)
    return jsonify(json[0]), json[1]


@app.route("/citizen/<string:id>", methods=['DELETE'])
def deleteCitizen(id):
    json = citizenC.delete(id)
    return jsonify(json[0]), json[1]


# -------------------------------- > Match
@app.route("/match", methods=['GET'])
def getAllMatch():
    json = matchC.index()
    return jsonify(json)


@app.route("/match", methods=['POST'])
def createMatch():
    data = request.get_json()
    json = matchC.create(data)
    return jsonify(json)


@app.route("/match/<string:id>", methods=['GET'])
def getMatch(id):
    json = matchC.show(id)
    return jsonify(json[0]), json[1]


@app.route("/match/<string:id>", methods=['PUT'])
def updateMatch(id):
    data = request.get_json()
    json = matchC.update(id, data)
    return jsonify(json[0]), json[1]


@app.route("/match/<string:id>", methods=['DELETE'])
def deleteMatch(id):
    json = matchC.delete(id)
    return jsonify(json[0]), json[1]

# -------------------------------- > Result
@app.route("/result", methods=['GET'])
def getAllResult():
    json = resultC.index()
    return jsonify(json)


@app.route("/result", methods=['POST'])
def createResult():
    data = request.get_json()
    json = resultC.create(data)
    return jsonify(json[0]), json[1]


@app.route("/result/<string:id>", methods=['GET'])
def getResult(id):
    json = resultC.show(id)
    return jsonify(json[0]), json[1]


@app.route("/result/<string:id>", methods=['PUT'])
def updateResult(id):
    data = request.get_json()
    json = resultC.update(id, data)
    return jsonify(json[0]), json[1]


@app.route("/result/<string:id>", methods=['DELETE'])
def deleteResult(id):
    json = resultC.delete(id)
    return jsonify(json[0]), json[1]

# -------------------------------- > Table
@app.route("/table", methods=['GET'])
def getAllTable():
    json = tableC.index()
    return jsonify(json)


@app.route("/table", methods=['POST'])
def createTable():
    data = request.get_json()
    json = tableC.create(data)
    return jsonify(json)


@app.route("/table/<string:id>", methods=['GET'])
def getTable(id):
    json = tableC.show(id)
    return jsonify(json[0]), json[1]


@app.route("/table/<string:id>", methods=['PUT'])
def updateTable(id):
    data = request.get_json()
    json = tableC.update(id, data)
    return jsonify(json[0]), json[1]


@app.route("/table/<string:id>", methods=['DELETE'])
def deleteTable(id):
    json = tableC.delete(id)
    return jsonify(json[0]), json[1]



def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Sever is running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
