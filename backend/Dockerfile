FROM python:slim-buster
RUN apt-get update \
  && apt-get -y install gcc \
  && apt-get -y install g++ \
  && apt-get -y install unixodbc unixodbc-dev \
  && apt-get clean
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY db_handler.py .
COPY server.py .
EXPOSE 44777
CMD  uvicorn server:app --port 44777 --host 0.0.0.0 --reload