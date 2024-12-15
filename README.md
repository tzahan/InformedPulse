
# Informed Pulse Backend and Microservices  

Informed Pulse is a comprehensive news analysis platform. It includes a main backend API along with dedicated microservices for summarization, bias analysis and recommendation, creating a scalable and modular architecture.  

## Features  
- **Backend API**:  
  - User management (registration, login, JWT-based authentication).  
  - Personalized news recommendations based on user preferences and interaction data.  
  - User interaction tracking.  
- **Summarizer Microservice**:  
  - Generates concise summaries for news articles along with sentiment score.  
  - Utilizes the Gemini API.  
- **Recommender Microservice**:  
  - Calculates news similarity using embedding models.  
  - Delivers personalized recommendations.  
- **Bias Analysis Microservice**:  
  - Analyzes news articles for content bias, including framing, tone, and selective details.
  - Provides a bias score and detailed explanations using LLM-based models.

## Tech Stack  
- **Backend and Microservices**: Python FastAPI   
- **Database**: MongoDB  
- **Authentication**: JWT-based authentication  
- **External APIs**: Google Cloud Embedding API, Gemini API  
- **Containerization**: Docker  

## Installation  

### Prerequisites  
- Python 3.9+  
- MongoDB instance (local or cloud).  
- Docker (optional for containerized deployment).  

### Steps  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/tzahan/InformedPulse.git  
   cd InformedPulse/informed-pulse-backend   # For backend service
   cd InformedPulse/personalized_recommendation   # For recommender system
   cd InformedPulse/semmarizer_sentiment_service   # For summarization and sentiment analysis
   cd InformedPulse/bias_analysis_service    # For bias analizer
   ```  

2. Set up a virtual environment:  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   ```  

3. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. Set up environment variables for the backend and microservices in a `.env` file:  
   ```env  
   # Backend API  
   JWT_SECRET_KEY=your-secret-key
   MONGO_USERNAME=your_mongoDB_username>
   MONGO_PASSWORD=your_mongoDB_password>
   GENAI_API_KEY=your-google-cloud-api-key  

   # Recommender Microservice  
   MONGO_USERNAME=your_mongoDB_username>
   MONGO_PASSWORD=your_mongoDB_password>
   GENAI_API_KEY=your-google-cloud-api-key  

   # Summarizer and Bias Analysis Microservices
   GENAI_API_KEY=your-google-cloud-api-key   
   ```  

5. Start the services:   
   ```bash  
   uvicorn app.main:app --host 0.0.0.0 --port 8000   
   ```  

### Run with Docker  
1. Build the Docker image (navigate to the required service folder):  
   ```bash  
   docker build -t <docker_image_name> .  

2. Run the container:  
   ```bash  
   docker run -d -p 8000:8000 --env-file .env <docker_image_name>
   ```  

## Example of API Endpoints  

### Backend API  
| Method | Endpoint                | Description                           |  
|--------|-------------------------|---------------------------------------|  
| POST   | `/user/register`        | Register a new user                   |  
| POST   | `/auth/login`           | Login and get a JWT token             |  
| POST   | `/user/add-interaction` | Add user interaction data (news ID)   |  
| GET    | `user/recommendations`  | Get personalized news recommendations |  

### Recommender Microservice  
| Method | Endpoint             | Description                                                    |  
|--------|----------------------|----------------------------------------------------------------|  
| POST   | `/recommendations`   | Fetch recommendations based on user preference and interactions|  

### Summarizer Microservice  
| Method | Endpoint             | Description                        |  
|--------|----------------------|------------------------------------|  
| POST   | `/summarize`         | Generate news summaries.           |  

### Bias Analysis Microservice  
| Method | Endpoint             | Description                        |  
|--------|----------------------|------------------------------------|  
| POST   | `/analyze_bias`         | Provide bias analysis result.   |  
