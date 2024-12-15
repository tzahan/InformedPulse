import google.generativeai as genai

from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=openai_api_key)

def analyze_bias(input_text):
    try:
        #model = genai.GenerativeModel("gemini-1.5-flash")
        model=genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                system_instruction='''You are an unbiased news analyst specializing in detecting content bias in news articles. 
                            Analyze the given article for: 
                            1. Framing: Identify how the content is framed, including focus on specific aspects while downplaying others. 
                            2. Tone: Assess whether the language suggests subtle judgments or biases. "
                            3. Selective Details: Highlight significant details included or omitted that may influence the reader's perception. 
                            
                            Provide a bias score (1-100), ranges are:
                                                0-20 (Low bias), 21-60 (Moderate bias), 61-100 (High bias).
                            Provide the response in dictionary format.
                                '''
            )
        #Provide detailed insights for each category.
        prompt = (
                f"Analyze this article for bias:\n\n{input_text},"
            )
        response = model.generate_content(prompt)
        return response.text.strip()
    
    except Exception as e:
        # Handle unexpected errors
        raise ValueError(f"Unexpected error during sentiment analysis: {e}")
