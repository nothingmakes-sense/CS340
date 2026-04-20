# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, user, passw): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = user
        PASS = passw
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        
        #Creates a new document in the animals collection.
        #Input argument: a dictionary (key/value pairs) acceptable to MongoDB insert_one.
        #Returns True if the insert was successful, False otherwise.
        
        if data is not None: 
            result = self.database.animals.insert_one(data)  # data should be dictionary     
            return result.acknowledged
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 
            return false

    # Create method to implement the R in CRUD.
    def read(self, query):
        
        #Queries documents from the animals collection.
        #Input argument: key/value lookup pair (dictionary) for MongoDB find API.
        #Uses find() (NOT find_one) and converts the cursor to a Python list.
        #Returns list of documents if successful, empty list otherwise.
        
        try:
            if query is not None:
                # Must work with the MongoDB cursor returned by find()
                cursor = self.collection.find(query)
                return list(cursor)   # Convert cursor → list as required
            else:
                return []
        except Exception as e:
            print(f"Error during read: {e}")
            
    #Update method
    def update(self, query:dict, update_spec):
        #Updates document(s) that match the query.
        
        if not query or not update_spec:
            return 0
        try:
            result = self.collection.update_many(query, update_spec)
            return result.modified_count
        except Exception as e:
            print(e)
            
    #delete method
    def delete(self, query:dict):
        #Deletes documet(s) that match query.
        
        if not query:
            return 0
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Execption as e:
            print(e)
            