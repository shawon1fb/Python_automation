import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

print(myclient.list_database_names())

mydb = myclient.shawon

print(mydb.list_collection_names())

mycol = mydb["mongo_collection"]
#
# mylist = [
#     {"name": "Amy", "address": "Apple st 652"},
#     {"name": "Hannah", "address": "Mountain 21"},
#     {"name": "Michael", "address": "Valley 345"},
#     {"name": "Sandy", "address": "Ocean blvd 2"},
#     {"name": "Betty", "address": "Green Grass 1"},
#     {"name": "Richard", "address": "Sky st 331"},
#     {"name": "Susan", "address": "One way 98"},
#     {"name": "Vicky", "address": "Yellow Garden 2"},
#     {"name": "Ben", "address": "Park Lane 38"},
#     {"name": "William", "address": "Central st 954"},
#     {"name": "Chuck", "address": "Main Road 989"},
#     {"name": "Viola", "address": "Sideway 1633"}
# ]
#
# x = mycol.insert_many(mylist)

# print(x.inserted_ids)

x = mycol.find_one()

print(x)

for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
    print(x)

print("----------------")
for x in mycol.find({}, {"address": 0}):
    print(x)
# mycol.delete_many({})
