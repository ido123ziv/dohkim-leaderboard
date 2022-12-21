FROM python:slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY db_handler.py .
COPY server.py .
CMD  uvicorn server:app --port 44777 --reload