FROM python:3.11-slim

WORKDIR /app
COPY app/web /app

RUN pip install --no-cache-dir flask requests

CMD ["python", "web_app.py"]
