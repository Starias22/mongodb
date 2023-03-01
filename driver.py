from pymongo import MongoClient
uri = "mongodb://localhost:27017/"
client = MongoClient(uri)
print('client:',client)
print(type(client))
db = client['test']
print('db:',db)
# or
# db = client.test_db
# collection = db['test_collection']
# or
collection = db.book
print('collection:',collection)
#collection.save({"hello":"world"})
print (collection.find_one())
db=client['newdb']
collection = db.new_collection
collection.insert_one({'name':'zzz'})
print (collection.find_one())
#collection.update_one()
"""collection.update_many()"""
x=collection.delete_one({'name':'zzz'})
print('deleted',x)
print (collection.find_one())



