# 💡 Informed Pulse – AI-Powered News Analysis Platform

**Informed Pulse** is an **AI-powered news analysis platform** that leverages **LLM-based natural language processing** and **microservice architecture** to deliver personalized and insightful news content.  

It integrates features like summarization, sentiment analysis, bias detection, and personalized recommendations — all served through a scalable **FastAPI-based RESTful backend**.

---

## 🚀 Key Features

- **Personalized News Recommendations** – Tailored content suggestions based on user preferences and interaction data.
- **AI-Powered NLP Services** – Automated text summarization, sentiment analysis, and bias detection using Gemini and Google Cloud APIs.
- **Secure Authentication** – User registration and login supported by JWT-based authentication.
- **Modular Microservices Architecture** – Independent AI services ensure scalability and maintainability.
- **Containerized & Cloud-Ready** – Dockerized services deployable to Azure App Service or other cloud platforms.

---
## 🧩 Architecture Overview
### 1️⃣ High-level Architecture
![image alt](https://github.com/tzahan/InformedPulse/blob/75ee57561950f0cd8d101af784abe9c0bb98827f/high_level_architecture.png)

### 2️⃣ System Architecture 
![image alt](https://github.com/tzahan/InformedPulse/blob/393d5b0e3c5f4ebeb632f659f6980e906650b603/system_architecture.jpg)

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend Framework** | FastAPI (Python 3.9+) |
| **Database** | MongoDB |
| **AI APIs** | Gemini API, Google Cloud Embedding API |
| **Authentication** | JWT (JSON Web Token) |
| **Deployment** | Docker, Azure App Service |
| **Architecture** | Microservices (REST APIs) |

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/tzahan/InformedPulse.git
cd InformedPulse
```  
### 2️⃣ Backend Setup 
```bash  
cd informed-pulse-backend
python -m venv venv
source venv/bin/activate     # For Windows: venv\Scripts\activate
pip install -r requirements.txt  
```  
### 3️⃣ Configure Environment Variables  
Create a .env file in each service directory or copy from the example file:
```bash  
cp .env.example .env 
```
Then edit the .env file as shown below:
```env  
# Database
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/informed-pulse?retryWrites=true&w=majority

# Authentication
JWT_SECRET_KEY=replace-with-strong-secret

# External APIs
GEMINI_API_KEY=your-gemini-api-key
GOOGLE_EMBEDDING_API_KEY=your-google-embedding-api-key

# Service Ports
BACKEND_PORT=8000
RECOMMENDER_PORT=8001
SUMMARIZER_PORT=8002
BIAS_PORT=8003
```

---

## ▶️ Run Locally (Manual)
```bash
# Backend
cd informed-pulse-backend
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Recommender
cd ../personalized_recommendation
uvicorn recommender.main:app --host 0.0.0.0 --port 8001 --reload

# Summarizer & Sentiment
cd ../summarizer_sentiment_service
uvicorn summarizer.main:app --host 0.0.0.0 --port 8002 --reload

# Bias Analyzer
cd ../bias_analyzer_service
uvicorn bias.main:app --host 0.0.0.0 --port 8003 --reload
```

---

## 🐳 Run with Docker Compose
This project includes a preconfigured **`docker-compose.yml`** file for running all microservices together.  
It automatically builds and starts the following services:
- Backend API (FastAPI)
- Personalized Recommender
- Summarizer & Sentiment Analyzer
- Bias Analyzer

### ▶️ Start All Services

Run the following command from the project root:

```bash
docker-compose up --build
```
This will:
- Build Docker images for all services
- Start containers on ports 8000–8003
- Automatically link services within the same Docker network

Once started, you can access the backend at:
👉 http://localhost:8000

---

## 📚 API Endpoints

| Service | Method | Endpoint | Description |
|----------|---------|-----------|--------------|
| **User** | `POST` | `/user/register` | Register a new user |
| **User** | `POST` | `/auth/login` | Authenticate user and return JWT |
| **Recommender** | `GET` | `/user/recommendations` | Retrieve personalized article recommendations |
| **Summarizer** | `POST` | `/summarize` | Generate AI-based article summary |
| **Sentiment** | `POST` | `/sentiment` | Analyze sentiment of article text |
| **Bias Analyzer** | `POST` | `/analyze_bias` | Detect bias or political leaning in text |

Access the auto-generated API documentation here:  
👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

