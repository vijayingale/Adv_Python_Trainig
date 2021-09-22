import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
def main():
    try:
        myclient = MongoClient("mongodb://%s:%s@127.0.0.1"%('myUserAdmin', 'abc123'))
        print(" \n\t Connection Successfull ",myclient)

        # list_of_db = myclient.list_databases()
        # print("\n\t Database Available in Db :",list_of_db)

        mydb = myclient['test']
        print("\n\t Database Create ... ",mydb)

        collection = mydb['student']
        record = {
            "_id" : 1,
            "name " : "raj",
            "roll_number" : 101,
            "branch": "case",
            "marks": 40
        }
        record_1 = collection.insert_one(record)
        print("\n\t Records :  ",record_1)
        list_of_db = myclient.list_database_names()
        print("\n\t Database Available in Db :",list_of_db)

    except ConnectionFailure as e:
        print("\n\t Error : ",e)


if __name__ == '__main__':
    main()