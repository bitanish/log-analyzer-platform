FROM python:3.11-slim
WORKDIR app/
RUN apt-get update && apt-get install -y gcc
COPY api_service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY api_service/ .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]