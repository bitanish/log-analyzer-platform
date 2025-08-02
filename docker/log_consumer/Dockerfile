
FROM python:3.11-slim
WORKDIR /consumer
COPY log_consumer/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY log_consumer/ .
CMD ["python", "consumer.py"]
