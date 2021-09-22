from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def main():
    try:
        myclient = MongoClient("mongodb://%s:%s@127.0.0.1"%('myUserAdmin', 'abc123'))
        # #create collection
        print("\n\t .Connection Successful : ")
        mydb = myclient['test']
        collection = mydb['Employ']
        # record = {
        #     "Grade ": "G1",
        #     "name": "raj",
        #     "Emp_Id": 100341,
        #     "branch": "cse",
        #     "Salary": 40
        #
        # }
        # record_1 = collection.insert_one(record)
        # print("\n\t.Records", record_1)
        #
        # list_of_db = myclient.list_database_names()
        # print("\n\t.Databases available in mongodb after creation", list_of_db)
        #
        # records = {
        #     "record1":{
        #                     "Grade ": "G1",
        #                     "name": "rohan",
        #                     "Emp_Id ": 103,
        #                     "branch": "cse",
        #                     "Salary": 45
        #                 },
        # "record2":{
        #                 "Grade ": "G1",
        #                     "name": "pretam",
        #                     "Emp_Id ": 103,
        #                     "branch": "cse",
        #                     "Salary": 45
        #             }
        # }
        # # #create collection
        # # collection = mydb['student']
        # for record in records.values():
        #     collection.insert_one(record)
        # mylist = [
        #    {
        #                   "Grade ": "G1",
        #                     "name": "prem",
        #                     "Emp_Id ": 103,
        #                     "branch": "cse",
        #                     "Salry": 45
        #               },
        #    {
        #     "Grade ": "G1",
        #                     "name": "pret",
        #                     "Emp_Id ": 103,
        #                     "branch": "cse",
        #                     "Salry": 50
        # },
        #     {
        #         "Grade ": "G1",
        #                     "name": "retam",
        #                     "Emp_Id ": 103,
        #                     "branch": "cse",
        #                     "Salry": 40
        #     }
        #
        # ]
        #
        # collection.insert_many(mylist)
        #
        # all_document = collection.find()
        # for each_record in all_document:
        #     print("doc", each_record)
        #
        # for x in collection.find({}, {"_id":0, "name":1, "branch":1}):
        #     print("Only fields with 1", x)
        curses = collection.find()
        for record in curses:
            print(record)
        # ## Delete Document ##
        #
        # myquery = {'name':'prem'}
        # collection.delete_one(myquery)
        #
        # curses = collection.find()
        # for record in curses:
        #     print(record)

        # ## Delete Many
        # myquery = {'name': 'prem'}
        # collection.delete_many(myquery)
        #
        # curses = collection.find()
        # for record in curses:
        #     print(record)

        ## Delete Using Two Parameter

        myquery = {'name': 'pret' ,'Grade' : 'G1'}
        collection.delete_many(myquery)

        curses = collection.find()
        for record in curses:
            print(record)

    except ConnectionFailure as e:
        print("error", e)

if __name__ == '__main__':
    main()