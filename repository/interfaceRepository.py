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

    def save(self, item:T):
        theCollection = self.baseDatos[self.coleccion]
        elId = ""
        item = self.transformRefs(item)
        if hasattr(item, "_id") and item._id != "":
            elId = item._id
            _id = ObjectId(elId)
            theCollection = self.baseDatos[self.coleccion]
            delattr(item, "_id")
            item = item.__dict__
            updateItem = {"$set": item}
            x = theCollection.update_one({"_id": _id}, updateItem)
        else:
            _id = theCollection.insert_one(item.__dict__)
            elId = _id.inserted_id.__str__()
            x = theCollection.find_one({"_id": ObjectId(elId)})
            x["_id"] = x["_id"].__str__()
            return self.findById(elId)

    def delete(self, id):
        theCollection = self.baseDatos[self.coleccion]
        count = theCollection.delete_one({"_id": ObjectId(id)}).deleted_count
        return {"deleted_count": count}

    def update(self, id, item: T):
        _id = ObjectId(id)
        theCollection = self.baseDatos[self.coleccion]
        delattr(item, "_id")
        item = item.__dict__
        updateItem = {"$set": item}
        x = theCollection.update_one({"_id": _id}, updateItem)
        return {"updated_count": x.matched_count}

    def findById(self, id):
        theCollection = self.baseDatos[self.coleccion]
        x = theCollection.find_one({"_id": ObjectId(id)})
        x = self.getValuesDBRef(x)
        if x == None:
            x = {}
        else:
            x["_id"] = x["_id"].__str__()
        return x

    def findAll(self):
        theCollection = self.baseDatos[self.coleccion]
        data = []
        for x in theCollection.find():
            x["_id"] = x["_id"].__str__()
            x = self.transformObjectIds(x)
            x = self.getValuesDBRef(x)
            data.append(x)
        return data

    def query(self, theQuery):
        theCollection = self.baseDatos[self.coleccion]
        data = []
        for x in theCollection.find(theQuery):
            x["_id"] = x["_id"].__str__()
            x = self.transformObjectIds(x)
            x = self.getValuesDBRef(x)
            data.append(x)
        return data

    def queryAggregation(self, theQuery):
        theCollection = self.baseDatos[self.coleccion]
        data = []
        for x in theCollection.aggregate(theQuery):
            x["_id"] = x["_id"].__str__()
            x = self.transformObjectIds(x)
            x = self.getValuesDBRef(x)
            data.append(x)
        return data

    def getValuesDBRef(self, x):
        keys = x.keys()
        for k in keys:
            if isinstance(x[k], DBRef):
                theCollection = self.baseDatos[x[k].collection]
                valor = theCollection.find_one({"_id": ObjectId(x[k].id)})
                valor["_id"] = valor["_id"].__str__()
                x[k] = valor
                x[k] = self.getValuesDBRef(x[k])

            elif isinstance(x[k], list) and len(x[k]) > 0:
                x[k] = self.getValuesDBRefFromList(x[k])

            elif isinstance(x[k], dict):
                x[k] = self.getValuesDBRef(x[k])

            return x

    def getValuesDBRefFromList(self, theList):
        newList = []
        theCollection = self.baseDatos[theList[0]._id.collection]
        for item in theList:
            value = theCollection.find_one({"_id": ObjectId(item.id)})
            value["_id"] = value["_id"].__str__()
            newList.append(value)
        return newList

    def transformObjectIds(self, x):
        for attribute in x.keys():
            if isinstance(x[attribute], ObjectId):
                x[attribute] = x[attribute].__str__()
            elif isinstance(x[attribute], list):
                x[attribute] = self.formatList(x[attribute])
            elif isinstance(x[attribute], dict):
                x[attribute] = self.transformObjectIds(x[attribute])
        return x

    def formatList(self, x):
        newList = []
        for item in x:
            if isinstance(item, ObjectId):
                newList.append(item.__str__())
        if len(newList) == 0:
            newList = x
        return newList

    def transformRefs(self, item):
        theDict = item.__dict__
        keys = list(theDict.keys())
        for k in keys:
            if theDict[k].__str__().count("object") == 1:
                newObject = self.ObjectToDBRef(getattr(item, k))
                setattr(item, k, newObject)
        return item

    def ObjectToDBRef(self, item: T):
        nameCollection = item.__class__.__name__.lower()
        return DBRef(nameCollection, ObjectId(item._id))
