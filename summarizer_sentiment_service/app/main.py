from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from summarizer_google import summarize_text, analyze_sentiment
import uvicorn


# Initialize FastAPI app
app = FastAPI()

# Data models for request bodies
class TextInput(BaseModel):
    text: str

# Endpoint for summarization
@app.post("/summarize")
def summarizeText(input_data: TextInput):
    try:
        summary = summarize_text(input_data.text)
        # print(summary)
        return {"summary": summary}
        
    except ValueError as e:
        # Return a 500 error with the specific error message
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        # Return a generic error if something unexpected happens
        raise HTTPException(status_code=500, detail="An unexpected error occurred during summarization.")

# Endpoint for sentiment analysis
@app.post("/analyze_sentiment")
def analyze_sentiment_withScore(input_data: TextInput):
    try:
        sentiment_result = analyze_sentiment(input_data.text)
        # print(sentiment_result)
        return {"sentiment_analysis": sentiment_result}

    except ValueError as e:
        # Return a 500 error with the specific error message
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        # Return a generic error if something unexpected happens
        raise HTTPException(status_code=500, detail="An unexpected error occurred during sentiment analysis.")

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
