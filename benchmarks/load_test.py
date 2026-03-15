import requests
import time

URL = "http://localhost:8000/infer"
REQUESTS = 50

latencies = []

for i in range(REQUESTS):
    start = time.time()

    requests.post(URL, params={"prompt": "Explain cloud infrastructure"})

    latency = (time.time() - start) * 1000
    latencies.append(latency)

print("p50 latency:", sorted(latencies)[len(latencies)//2])
print("p95 latency:", sorted(latencies)[int(len(latencies)*0.95)])
