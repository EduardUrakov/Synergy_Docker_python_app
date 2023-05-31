FROM python:3.11-alpine

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install flask
CMD python main.py