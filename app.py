from fastapi import FastAPI
from env import ResQEnv

app = FastAPI()
env = ResQEnv()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.get("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    return env.step(action)