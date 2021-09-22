from pymongo import MongoClient
try:
    myclient = MongoClient("mongodb://%s:%s@127.0.0.1"%('myUserAdmin','abc123'))
    ## Create Collection
    print("\n\t .Connectionn Successfull :")
    mydb = myclient['database']
    collections = mydb['test6']
    # profile = [
    #     {"user": "ram", "title": "java"},
    #     {"user": "raju", "title": "Python"},
    #     {"user": "ramesh", "title": "java"},
    #     {"user": "rohan", "title": "Python"},
    #     {"user": "roni", "title": "Python"},
    # ]
    # collections.insert_many(profile)
    # agg_Result = collections.aggregate(
    #     [
    #         {
    #             "$group":
    #                 {
    #                     "_id": "$user",
    #                     "num_lang":{"$sum" : 1}
    #                 }
    #         }
    #     ]
    # )
    # print("\n\t Result :")
    # for i in agg_Result:
    #     print("\n\t Arregation result is :--" ,i)
    profile =[
        {"infosys ":{ "user ": "red_hat", "title": "customer"}},
        {"user" : "Alaska", "title": "North_America"},
        {"user": "Canberra", "title" : "Australia"},
        {"user":"Wellington" , "title" : "new Zeland"},
        {"user":"Paris" , "title" : "France"}
    ]

    collections.insert_many(profile)
    agg_result = collections.aggregate(
        [
            {
                "$group":
                    {
                        "_id":"$user",
                        "num_lang": {"$sum":1}
                    }
            }
        ]
    )

    print("\n\t Result : ")
    for i in agg_result:
        print(i)
except ConnectionError as e:
    print("\n\t .Connection Error :")