
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


## What This Project Demonstrates

- API-based inference service
- Load testing and benchmarking
- Latency and throughput measurement
- Persisted benchmark artifacts


## Related Project

RAG Evaluation Platform  
https://github.com/Electricpaper77/ai-rag-eval-platform


## Benchmark + Observability Proof

Example benchmark run:

| Metric | Value |
|------|------|
| Requests | 50 |
| p50 Latency | ~120 ms |
| p95 Latency | ~240 ms |
| Throughput | ~18 req/sec |

Benchmark artifact stored in:

results/benchmark_run_01.json

Prometheus metrics exposed at:

/metrics

Example metrics captured:

inference_requests_total  
inference_latency_seconds_count  

Metrics artifact stored in:

results/metrics_output.txt

These artifacts demonstrate performance testing and observability for an inference service.
