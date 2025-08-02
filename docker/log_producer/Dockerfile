FROM python:3.11-slim
WORKDIR app/
COPY log_producer/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY log_producer/ .
CMD ["python", "produce.py"]
