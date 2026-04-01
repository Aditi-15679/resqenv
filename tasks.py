TASKS = [
    {
        "id": "easy",
        "data": {
            "disaster_type": "flood",
            "areas": [
                {"name": "A", "people": 50, "severity": 0.9}
            ],
            "resources": {"boats": 1}
        },
        "solution": {
            "best_area": "A"
        }
    },
    {
        "id": "medium",
        "data": {
            "disaster_type": "earthquake",
            "areas": [
                {"name": "A", "people": 50, "severity": 0.9},
                {"name": "B", "people": 80, "severity": 0.6}
            ],
            "resources": {"ambulances": 1}
        },
        "solution": {
            "best_area": "A"
        }
    },
    {
        "id": "hard",
        "data": {
            "disaster_type": "fire",
            "areas": [
                {"name": "A", "people": 30, "severity": 0.7},
                {"name": "B", "people": 100, "severity": 0.6},
                {"name": "C", "people": 40, "severity": 0.95}
            ],
            "resources": {"fire_trucks": 1}
        },
        "solution": {
            "best_area": "C"
        }
    }
]