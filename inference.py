import requests

BASE_URL = "http://127.0.0.1:8000"

def run():
    total_score = 0

    for i in range(3):
        obs = requests.get(f"{BASE_URL}/reset").json()

        action = {
            "allocations": [{"area": "A"}],
            "reasoning": "Choosing area with highest severity and people"
        }

        result = requests.post(f"{BASE_URL}/step", json=action).json()
        total_score += result[1]

    print("Average Score:", total_score / 3)

if __name__ == "__main__":
    run()