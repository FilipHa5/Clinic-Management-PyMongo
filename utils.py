import pymongo


class MongoManager:
     __instance = None
     @staticmethod 
     def getInstance():
         if MongoManager.__instance == None:
             MongoManager()
         return MongoManager.__instance
     def __init__(self):
        if MongoManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            client = pymongo.MongoClient('localhost', 27017)
            MongoManager.__instance = client['Clinic']
            