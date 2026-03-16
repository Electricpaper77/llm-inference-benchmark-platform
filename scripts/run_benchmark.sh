#!/bin/bash

echo "Starting inference API..."

uvicorn api.inference_api:app --host 0.0.0.0 --port 8000 &

API_PID=$!

sleep 3

echo "Running load test..."

python benchmarks/load_test.py

echo "Benchmark finished"

kill $API_PID
