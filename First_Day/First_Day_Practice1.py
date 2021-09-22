from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ('myUserAdmin', 'abc123'))
print("\n\t.connection successful :-", myclient)

# list down the databases
list_of_db = myclient.list_database_names()
print("\n\t.Databases available in mongodb :-", list_of_db)

mydb = myclient['test']
print("\n\t.Database created...", mydb)
collection = mydb['Employ']

curson = collection.find({"salry": {"$lt": 45}})
print("The records greater than 45")

for record in curson:
  print("records:%s" % record)

mydoc = collection.find().sort("name", -1)
for x in mydoc:
    print("sorting..", x)
