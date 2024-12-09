FROM python:latest

WORKDIR /summarizer-api

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY .env .
COPY ./app ./app

# EXPOSE 3000
CMD ["python","./app/main.py"]
