from fastapi import FastAPI
import time

app = FastAPI()

@app.post("/infer")
def infer(prompt: str):
    start = time.time()

    # mock inference
    response = f"Processed: {prompt}"

    latency = time.time() - start

    return {
        "response": response,
        "latency_ms": latency * 1000
    }
