from pymongo import MongoClient
try:
    myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ('myUserAdmin', 'abc123'))
    # #create collection
    print("\n\t .Connection Successful : ")
    mydb = myclient['database']
    # collection = mydb['test2']
    #
    # profile = [
    #     {"user":"ram" , "title": "Python"},
    #     {"user": "ramesh", "title": "Java"},
    #     {"user":"ramnath" , "title": "C"},
    #     {"user":"ramesh" , "title": "C++"},
    #     {"user":"ramoji" , "title": "Android"}
    # ]
    #
    # collection.insert_many(profile)
    #
    # agg_result = collection.aggregate(
    #     [
    #         {
    #         "$group":
    #             {
    #                "_id":"$user",
    #                 "num_lang":{"$sum" : 1}
    #             }
    #         }
    #     ]
    # )
    #
    # print("\n\t Result : ")
    # for i in agg_result:
    #     print(i)

    collection = mydb['test3']

    profile = [
        {"Telgu_Films ":{"user": "rajnikat", "title": "Megastar"}},
        {"user": "chiranjivi", "title": "Megastar"},
        {"user": "Allu_Arjun", "title": "Stylish_Star"},
        {"user": "Yash", "title": "Power_Star"},
        {"user": "ramoji", "title": "Film_city"}
    ]

    collection.insert_many(profile)

    agg_result = collection.aggregate(
        [
            {
                "$group":
                    {
                        "_id": "$user",
                        "num_lang": {"$sum": 1}
                    }
            }
        ]
    )

    print("\n\t Result : ")
    for i in agg_result:
        print(i)

except ConnectionError as e:
    print("Errorr" ,e)