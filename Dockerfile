FROM python:3.10-slim

WORKDIR /code
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY . .

CMD flask run -h 0.0.0.0 -p 80
