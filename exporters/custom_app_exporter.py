from prometheus_client import start_http_server, Gauge
import random
import time

# Custom application metrics
cpu_usage = Gauge('app_cpu_usage', 'CPU usage of custom app')
request_count = Gauge('app_request_count', 'Request count of custom app')

def generate_metrics():
    while True:
        cpu_usage.set(random.randint(0, 100))
        request_count.set(random.randint(0, 1000))
        time.sleep(5)

if __name__ == '__main__':
    start_http_server(8000)
    generate_metrics()

