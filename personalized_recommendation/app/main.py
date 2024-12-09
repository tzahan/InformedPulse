import os
from dotenv import load_dotenv
# import google.generativeai as genai
from fastapi import FastAPI, HTTPException
import uvicorn

from app.fetch_news import NewsFetcher
from app.personalized_recommender import PersonalizedRecommender


load_dotenv()
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
genai_api_key= os.getenv("GOOGLE_API_KEY")

#print(genai_api_key)

uri = f"mongodb+srv://{username}:{password}@cluster0.3rx4l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"        
db_name = "cognitive_project"
collection_name = "news_scraper"

news_fetcher = NewsFetcher(uri, db_name, collection_name)

embedding_model = "models/text-embedding-004"
recommender = PersonalizedRecommender(genai_api_key, embedding_model, news_fetcher)

interaction_list = ["67504c6d04a9bbdb06e0098b","67504c6d04a9bbdb06e00970"]
# user_preferences = "sports technology climate politics"
# recommendations = recommender.recommend(user_preferences, limit=10)
# print(recommendations)
# FastAPI app

app = FastAPI()

@app.get("/recommendations")
def get_recommendations(preferences: str, limit: int = 5):
    """
    API endpoint to fetch personalized news recommendations.
    """
    try:
        recommendations = recommender.recommend(preferences, interaction_list, limit)
        if not recommendations:
            raise HTTPException(status_code=404, detail="No recommendations found.")
        return {"recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
