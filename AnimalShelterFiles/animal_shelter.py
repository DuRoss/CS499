#Dustin Ross
#Assignment 4-1
#March 25, 2022

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        self.client = MongoClient('mongodb://localhost:46729')
        # access the MongoDB databases and collections. 
        # self.client = MongoClient('mongodb://%s:%s@localhost:46729' % (username, password))
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Create method to implement the R in CRUD.
    def read(self, query):
        if query is not None:
            return self.database.animals.find(query)
        else:
            return self.database.animals.find({})
    
# Create method to implement the U in CRUD.
    def update(self, query, update):
        if query is not None:
            self.database.animals.update_many(query, update)
            return True
        else:
            raise Exception("Cannot read document, as query is parameter is empty")
            return False
            
# Create method to implement the D in CRUD.
    def delete(self, query):
        if query is not None:
            self.database.animals.delete_many(query)
            return True
        else:
            raise Exception("Cannot read document, as query is parameter is empty")
            return False
        
