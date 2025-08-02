# metrics.py

from prometheus_client import Counter, start_http_server

# Counter for number of logs successfully ingested
log_ingested_counter = Counter(
    'logs_ingested_total', 'Total number of logs successfully ingested'
)

# Counter for number of DB insert failures
insert_failure_counter = Counter(
    'insert_failures_total', 'Total number of failed log insert attempts'
)

# Start Prometheus metrics HTTP server on port 8001
def start_metrics_server(port=8001):
    start_http_server(port)
