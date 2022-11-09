import pymongo


client = pymongo.MongoClient("mongodb+srv://meph:xwXuuY4s7aCjrEe@cluster0.lttmqg6.mongodb.net/resultados-db?retryWrites=true&w=majority")

res_db = client["resultados-db"]
print(res_db.list_collection_names())
