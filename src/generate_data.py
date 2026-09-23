import json
import random
from pathlib import Path

KIGALI_LOCATIONS = [
    "Gikondo", "Nyamirambo", "Kicukiro", "Kanombe",
    "Nyabugogo", "Kimisagara", "Kinyinya",
    "Masaka", "Kimironko", "Kacyiru", "Remera"
]

def generate_drivers(count=10000):
    drivers = []
    for i in range(1, count + 1):
        drivers.append({
            "driver_id": f"DRV-{i:05d}",
            "name": f"Driver_{i}",
            "status": random.choice(["available", "busy", "offline"]),
            "zone": random.choice(KIGALI_LOCATIONS),
            "rating": round(random.uniform(4.0, 5.0), 2)
        })
    return drivers

if __name__ == "__main__":
    out_dir = Path(__file__).resolve().parent
    file_path = out_dir / "drivers.json"
    
    data = generate_drivers(10000)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    
    print(f"Generated {len(data)} drivers at {file_path}")