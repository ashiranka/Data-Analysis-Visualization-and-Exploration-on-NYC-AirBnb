import json
import pymongo
from bson import json_util

# Connect to mongoDB database
myclient = pymongo.MongoClient("mongodb+srv://ashiranka:ashiranka@cluster.ivy0q.mongodb.net/new_york_airbnb?ssl=true&ssl_cert_reqs=CERT_NONE")
db = myclient["new_york_airbnb"]
col = db["Detail"]


# Upload the cleaned csv data to the database with each row as a document
def json_loader(filepath):
    with open(filepath, "r") as file_descriptor:
        data = json.load(file_descriptor)
        for rows in data:
            tempDict = {}
            tempDict["InnerDetails"] = rows
            col.insert_one(tempDict)


json_loader("/Users/ashiranka/Desktop/DSCIProject/venv/nyAirBnbData.json")
