# Use the official Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /recommender-api

# Copy the project files into the container
COPY ./requirements.txt /recommender-api/requirements.txt
#COPY ./.env /recommender-api/.env

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

COPY ./app   /recommender-api/app

# Expose the application port
EXPOSE 8000

# Start the FastAPI server
#CMD ["python","./main.py"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]