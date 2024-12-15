from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.bias_analyzer import analyze_bias
import uvicorn


# Initialize FastAPI app
app = FastAPI()

# Data models for request bodies
class TextInput(BaseModel):
    text: str

# Endpoint for summarization
@app.post("/analyze_bias")
def analyze_bias_withscore(input_data: TextInput):
    try:
        bias_result = analyze_bias(input_data.text)
        print(bias_result)
        return {"bias_analysis": bias_result}
        
    except ValueError as e:
        # Return a 500 error with the specific error message
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        # Return a generic error if something unexpected happens
        raise HTTPException(status_code=500, detail="An unexpected error occurred during summarization.")


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
