# import os
# from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import PyMongoError
from typing import List, Dict
from datetime import datetime, timedelta
import logging
from typing import List, Dict
from bson import ObjectId



class NewsFetcher:
    def __init__(self, db_uri: str, db_name: str, collection_name: str):
        """
        Constructor to initialize MongoDB connection parameters.
        """
        # load_dotenv()
        # username = os.getenv("MONGO_USERNAME")
        # password = os.getenv("MONGO_PASSWORD")
        
        # self.uri = f"mongodb+srv://{username}:{password}@cluster0.3rx4l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        self.uri = db_uri
        self.db_name = db_name
        self.collection_name = collection_name

    def serialize_doc(self, doc: Dict) -> Dict:
        """
        Converts MongoDB ObjectId to string and processes nested fields if needed.
        """
        for key, value in doc.items():
            if isinstance(value, ObjectId):
                doc[key] = str(value)
            elif isinstance(value, list):
                doc[key] = [self.serialize_doc(item) if isinstance(item, dict) else item for item in value]
        return doc

    def fetch_news(self, limit: int) -> List[Dict]:
        """
        Fetch news articles from MongoDB.
        """
        try:
            with MongoClient(self.uri, server_api=ServerApi("1")) as client:
                # print(self.uri)
                collection = client[self.db_name][self.collection_name]
                all_documents = list(
                collection.find(
                    {
                        # Filters to exclude None values for required fields
                        "title": {"$exists": True, "$ne": None},
                        "summary": {"$exists": True, "$ne": None},
                        "sentiment": {"$exists": True, "$ne": None},
                        "embedding": {"$exists": True, "$ne": None},
                        # Check nested array field for non-empty lists
                        "$or": [
                            {"top_5_similar": {"$exists": False}},  # If not present, accept it
                            {"top_5_similar": {"$ne": []}}         # If present, must not be empty
                        ]
                    },
                    {
                        "_id": 1,
                        "title": 1,
                        "summary": 1,
                        "sentiment": 1,
                        "main_image": 1,
                        "embedding": 1,
                        "domain": 1,
                        "category": 1,
                        "url": 1,
                        "publication_date": 1,
                        "top_5_similar": 1
                    }
                ).limit(limit)
            )

            # Serialize ObjectIds and nested fields for valid documents
            return [self.serialize_doc(doc) for doc in all_documents]

        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        

    def fetch_news_by_ids(self, news_ids: List[str]) -> List[Dict]:
        """
        Fetch news articles based on a list of news IDs.
        """
        try:
            with MongoClient(self.uri, server_api=ServerApi("1")) as client:
                print(self.uri)
                collection = client[self.db_name][self.collection_name]
                
                object_ids = [ObjectId(news_id) for news_id in news_ids]
                # Fetch articles that match any of the given IDs
                news_articles = list(
                    collection.find(
                        {
                            "_id": {"$in": object_ids}  # Match any ID in the list
                        
                            # Filters to exclude None values for required fields
                            #"title": {"$exists": True, "$ne": None},
                            #"summary": {"$exists": True, "$ne": None},
                            #"sentiment": {"$exists": True, "$ne": None},
                            #"embedding": {"$exists": True, "$ne": None},
                        },
                        {
                            "_id": 1,
                            "title": 1,
                            "summary": 1,
                            "sentiment": 1,
                            "main_image": 1,
                            "embedding": 1,
                            "domain": 1,
                            "category": 1,
                            "url": 1,
                            "publication_date": 1,
                            "top_5_similar": 1
                        }
                    )
                )
                print(news_articles)
                #return news_articles
                # Serialize ObjectIds and nested fields for valid documents
                return [self.serialize_doc(doc) for doc in news_articles]
        except Exception as e:
            print(f"Error fetching news by IDs: {e}")
            return []



    def fetch_latest_news(self) -> List[Dict]:
        """
        Fetch all news articles from the latest day saved in MongoDB.
        """
        try:
            with MongoClient(self.uri, server_api=ServerApi("1")) as client:
                # print(self.uri)
                collection = client[self.db_name][self.collection_name]

                # Fetch the most recent news article's publication_date
                latest_news = collection.find({}, {"publication_date": 1}).sort("publication_date", -1).limit(1)
                print(latest_news)
                latest_date = next(latest_news, {}).get("publication_date")

                if not latest_date:
                    print("No news articles found.")
                    return []

                # Ensure the latest_date is a datetime object
                if isinstance(latest_date, str):
                    latest_date = datetime.fromisoformat(latest_date)  # Convert string to datetime

                # Calculate the start and end of the latest date
                start_of_day = latest_date.replace(hour=0, minute=0, second=0, microsecond=0)
                end_of_day = start_of_day + timedelta(days=1)

                # Query to fetch all articles from the latest day
                all_documents = list(
                    collection.find(
                        {"publication_date": {"$gte": start_of_day, "$lt": end_of_day}}, 
                        {
                            "_id": 0,
                            "title": 1,
                            "summary": 1,
                            "sentiment": 1,
                            "main_image": 1,
                            "embedding": 1,
                            "domain": 1,
                            "category": 1,
                            "url": 1,
                            "publication_date": 1,
                        }
                    )
                )

                return all_documents
        except Exception as e:
            print(f"An error occurred: {e}")
            return []