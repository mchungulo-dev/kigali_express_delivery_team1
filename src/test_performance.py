import json
import random
import time
from pathlib import Path
from algorithms import linear_search, binary_search, build_driver_map, hash_lookup

def load_data():
    data_path = Path(__file__).resolve().parent.parent / "data" / "drivers.json"
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)

def run_benchmarks(iterations=5000):
    drivers = load_data()
    sorted_drivers = sorted(drivers, key=lambda d: d["driver_id"])
    
    # Pre-building the O(1) hash map
    driver_map = build_driver_map(drivers)

    # Pick random target IDs to search for
    all_ids = [d["driver_id"] for d in drivers]
    sample_targets = [random.choice(all_ids) for _ in range(iterations)]

    # 1. Benchmark Linear Search O(N)
    start = time.perf_counter()
    for tid in sample_targets:
        linear_search(drivers, tid)
    linear_total = time.perf_counter() - start

    # 2. Benchmark Binary Search O(log N)
    start = time.perf_counter()
    for tid in sample_targets:
        binary_search(sorted_drivers, tid)
    binary_total = time.perf_counter() - start

    # 3. Benchmark Dictionary Lookup O(1)
    start = time.perf_counter()
    for tid in sample_targets:
        hash_lookup(driver_map, tid)
    hash_total = time.perf_counter() - start

    print(f"Ran {iterations:,} lookups over {len(drivers):,} records:\n")
    print(f"| Algorithm           | Complexity | Total Time (s) | Average Latency (Microseconds) |")
    print(f"|---------------------|------------|----------------|------------------------|")
    print(f"| Linear Search       | O(N)       | {linear_total:14.4f} | {(linear_total / iterations) * 1e6:22.2f} |")
    print(f"| Binary Search       | O(log N)   | {binary_total:14.4f} | {(binary_total / iterations) * 1e6:22.2f} |")
    print(f"| Hash Map (Dict)     | O(1)       | {hash_total:14.4f} | {(hash_total / iterations) * 1e6:22.2f} |")

if __name__ == "__main__":
    run_benchmarks()