import pymongo
from bson import DBRef
from bson.objectid import ObjectId
from typing import TypeVar, Generic, List, get_origin, get_args
import json

T = TypeVar('T')


class InterfaceRepository(Generic[T]):
    def __init__(self):
        dataConfig = self.loadFileConfig()
        client = pymongo.MongoClient(dataConfig["database-url"])
        self.baseDatos = client[dataConfig["database-name"]]
        theClass = get_args(self.__orig_bases__[0])
        self.coleccion = theClass[0].__name__.lower()

    def loadFileConfig(self):
        with open('config.json') as f:
            data = json.load(f)
        return data

    def save(self, item: T):
        laColeccion = self.baseDatos[self.coleccion]
        elId = ""
        item = self.transformRefs(item)
        if hasattr(item, "_id") and item._id != "":
            elId = item._id
            _id = ObjectId(elId)
            laColeccion = self.baseDatos[self.coleccion]
            delattr(item, "_id")
            item = item.__dict__
            updateItem = {"$set": item}
            x = laColeccion.update_one({"_id": _id}, updateItem)
        else:
            _id = laColeccion.insert_one(item.__dict__)
            elId = _id.inserted_id.__str__()
            x = laColeccion.find_one({"_id": ObjectId(elId)})
            x["_id"] = x["_id"].__str__()
            return self.findById(elId)
