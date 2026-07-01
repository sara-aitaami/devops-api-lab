FROM python:3.12-slim

WORKDIR /app

RUN pip install psycopg2-binary

COPY app/app.py .

CMD ["python3", "app.py"]
