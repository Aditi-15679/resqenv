# 🌍 ResQEnv – Intelligent Disaster Response RL Environment

## 🚀 Overview

**ResQEnv** is a real-world Reinforcement Learning environment built using the OpenEnv framework. It simulates disaster response scenarios where an AI agent must allocate limited resources to maximize rescue impact.

The environment evaluates not just the final decision, but also the **quality of reasoning**, making it suitable for training and benchmarking modern LLM-based agents.

---

## 🎯 Motivation

In real-world disaster situations, responders must make quick decisions under uncertainty, balancing:

* Severity of impact
* Number of affected people
* Limited resources

ResQEnv models this decision-making process, allowing AI agents to learn **prioritization, reasoning, and trade-offs**.

---

## 🧠 Key Features

* ✅ Real-world task simulation (disaster response)
* ✅ 3 difficulty levels (easy → medium → hard)
* ✅ Dynamic task generation (randomized scenarios)
* ✅ Intelligent reward function (partial scoring)
* ✅ Reasoning-based evaluation (LLM-style grading)
* ✅ Penalty for incorrect decisions
* ✅ Transparent scoring via `info` output
* ✅ Fully OpenEnv-compatible API
* ✅ Lightweight and fast (<20 min runtime)

---

## 🏗️ Environment Design

### 🔹 Observation Space

The agent receives:

```json
{
  "disaster_type": "fire",
  "areas": [
    {"name": "A", "people": 30, "severity": 0.7},
    {"name": "B", "people": 100, "severity": 0.6},
    {"name": "C", "people": 40, "severity": 0.95}
  ],
  "resources": {"fire_trucks": 1}
}
```

---

### 🔹 Action Space

The agent must respond with:

```json
{
  "allocations": [{"area": "A"}],
  "reasoning": "Area A has highest severity and most people"
}
```

---

### 🔹 Reward Function

The reward is computed as:

| Component              | Score |
| ---------------------- | ----- |
| Correct area selection | +0.6  |
| Mentions "severity"    | +0.2  |
| Mentions "people"      | +0.2  |
| Wrong decision penalty | -0.3  |

Final reward is clipped between **0.0 and 1.0**

---

### 🔹 Episode

* Each episode consists of **1 step**
* The environment resets with a new random task

---

## 🧪 Tasks

### 🟢 Easy

* Single area
* Obvious decision

### 🟡 Medium

* Multiple areas
* Trade-off between severity and population

### 🔴 Hard

* Conflicting priorities
* Requires deeper reasoning

---

## ⚙️ API Endpoints

### 🔹 Reset Environment

```
GET /reset
```

Returns initial observation.

---

### 🔹 Take Action

```
POST /step
```

#### Request:

```json
{
  "allocations": [{"area": "A"}],
  "reasoning": "Area A has highest severity"
}
```

#### Response:

```json
[
  {...observation},
  0.8,
  true,
  {
    "chosen_area": "A",
    "correct_area": "C"
  }
]
```

---

## 🧾 Project Structure

```
resqenv/
│
├── app.py
├── env.py
├── tasks.py
├── grader.py
├── models.py
├── inference.py
├── openenv.yaml
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🛠️ Setup & Installation

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd resqenv
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run the server

```bash
uvicorn app:app --reload
```

---

### 4. Open in browser

```
http://127.0.0.1:8000/docs
```

---

## 🤖 Baseline Inference

Run the baseline script:

```bash
python inference.py
```

### ✅ Output:

```
Average Score: 1.0
```

This demonstrates reproducible evaluation across tasks.

---

## 🐳 Docker Support

### Build image:

```bash
docker build -t resqenv .
```

### Run container:

```bash
docker run -p 7860:7860 resqenv
```

---

## 📄 OpenEnv Compliance

* ✔ Implements `reset()`, `step()`, `state()`
* ✔ Typed structure using Pydantic (models.py)
* ✔ Includes `openenv.yaml`
* ✔ Supports automated validation
* ✔ Compatible with HF Spaces deployment

---

## 🏆 Evaluation Criteria Alignment

| Criteria           | How ResQEnv Meets It               |
| ------------------ | ---------------------------------- |
| Real-world utility | Disaster response simulation       |
| Task quality       | Multi-level tasks with clear goals |
| Environment design | Clean API, structured state        |
| Reward system      | Dense + reasoning-based            |
| Code quality       | Modular, typed, documented         |
| Creativity         | Combines RL + reasoning evaluation |

---

## 🚀 Future Improvements

* Multi-step decision-making
* Integration with real-world map APIs
* Multi-resource allocation strategies
* Multi-agent coordination

---

## 👤 Author

**Aditi**
Solo Participant –Hackathon

---

## 🏁 Final Note

ResQEnv is designed to go beyond toy environments by introducing **real-world complexity, reasoning evaluation, and meaningful reward shaping**, making it a strong candidate for benchmarking next-generation AI agents.
