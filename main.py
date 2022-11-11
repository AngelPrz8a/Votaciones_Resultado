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


# Candidate
@app.route("/candidate", methods=['GET'])
def getAllCandidate():
    json = candidateC.index()
    return jsonify(json)


@app.route("/candidate", methods=['POST'])
def createCandidate():
    data = request.get_json()
    json = candidateC.create(data)
    return jsonify(json)


@app.route("/candidate/<string:id>", methods=['GET'])
def getCandidate(id):
    json = candidateC.show(id)
    return jsonify(json)

@app.route("/candidate/<string:id>", methods=['PUT'])
def updateCandidate(id):
    data = request.get_json()
    json = candidateC.update(id, data)
    return jsonify(json)


@app.route("/candidate/<string:id>",methods=['DELETE'])
def deleteCandidate(id):
    json = candidateC.delete(id)
    return jsonify(json)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Sever is running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
