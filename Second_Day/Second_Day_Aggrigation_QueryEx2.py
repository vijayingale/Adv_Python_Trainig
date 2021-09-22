## use Pipe line For Two Different Type
## Exploer unwind

from pymongo import MongoClient
from bson.son import SON
import pprint

try:
    myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ('myUserAdmin', 'abc123'))
    # #create collection
    print("\n\t .Connection Successful : ")
    mydb = myclient['database']
    mycon = mydb['test3']


    cricketer_playing_Format =[
        {"p": 45 ,"format":["T20","OneDay"]},
        {"p": 12, "format": ["T20"]},
        {"p": 100, "format": ["T20", "Test"]},
        {"p": 18, "format": ["T20", "OneDay" ,"Test"]},
        {"p": 42, "format": ["OneDay"]},
                               ]

    result = mycon.insert_many(cricketer_playing_Format)

    pipeline =[
        {"$unwind":"$format"},
        {"$group":{"_id":"$format","count":{"$sum":1}}},
        {"$sort":SON([("count",+1),("_id" ,-1)])}
    ]
    pprint.pprint((list(mycon.aggregate(pipeline))))
except ConnectionError as e:
    print("\n\t .Error :-- ",e)