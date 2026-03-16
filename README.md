
## Benchmark Results

| Metric | Value |
|------|------|
| Requests | 50 |
| p50 Latency | 120 ms |
| p95 Latency | 240 ms |
| Throughput | 18 req/sec |


## Running the Benchmark

Start the inference API:

uvicorn api.inference_api:app --host 0.0.0.0 --port 8000

In a second terminal, run the benchmark:

python benchmarks/load_test.py

Benchmark artifacts are stored in:

results/benchmark_run_01.json


## Architecture

Client Request
      |
      v
FastAPI Inference API
      |
      v
Benchmark Script (Load Test)
      |
      v
Latency + Throughput Metrics
      |
      v
Benchmark Results JSON

