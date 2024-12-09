import google.generativeai as genai

from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key=os.getenv('GOOGLE_API_KEY')
print(openai_api_key)
genai.configure(api_key=openai_api_key)

def summarize_text(input_text, max_tokens=300):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt=f"Write a concise summary of the following text: {input_text} around 100 words"
        response = model.generate_content(prompt, 
                    generation_config = genai.GenerationConfig(
                        max_output_tokens=max_tokens,
                        temperature=1.0
                    )
                )

        # return response.text
        return response.text.strip()
    
    except Exception as e:
        # Handle unexpected errors
        raise ValueError(f"Unexpected error during sentiment analysis: {e}")

def analyze_sentiment(input_text):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        # prompt = f"Analyze the sentiment of the following text and respond with 'Positive', 'Negative', or 'Neutral' along with a score from -1 to 1, where -1 is very negative, 0 is neutral, and 1 is very positive:\n\n{input_text}"
        prompt = (
                f"Analyze the sentiment of the following text and respond with only the sentiment score, "
                f"where -1 represents negative, 0 represents neutral, and 1 represents positive:\n\n{input_text},"
                f"Do not include any text or explanations, only output the numerical score."
            )
        response = model.generate_content(prompt)
        return response.text.strip()
    
    except Exception as e:
        # Handle unexpected errors
        raise ValueError(f"Unexpected error during sentiment analysis: {e}")
