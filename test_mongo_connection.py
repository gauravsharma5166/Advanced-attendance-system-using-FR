import pymongo
from pymongo import MongoClient

# Replace with your connection string
connection_string = "mongodb+srv://gauravsharma5166:<password>@cluster0.ywi7pel.mongodb.net/?retryWrites=true&w=majority"

try:
    client = MongoClient(connection_string)
    # Test connection
    client.server_info()
    print("Successfully connected to MongoDB Atlas!")
except Exception as e:
    print(f"Error connecting to MongoDB Atlas: {str(e)}")
