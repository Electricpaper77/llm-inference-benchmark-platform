from fastapi import FastAPI
from fastapi.responses import Response
from prometheus_client import Counter, Histogram, generate_latest
import time

app = FastAPI()

REQUEST_COUNT = Counter(
    "inference_requests_total",
    "Total inference requests"
)

LATENCY = Histogram(
    "inference_latency_seconds",
    "Latency of inference requests"
)

@app.post("/infer")
def infer(prompt: str):

    REQUEST_COUNT.inc()

    start = time.time()

    response = f"Processed: {prompt}"

    latency = time.time() - start
    LATENCY.observe(latency)

    return {
        "response": response,
        "latency_ms": latency * 1000
    }


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
