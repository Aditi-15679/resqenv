import random
from tasks import TASKS
from grader import grade

class ResQEnv:
    def __init__(self):
        self.current_task = None
        self.step_count = 0

    def reset(self):
        self.current_task = random.choice(TASKS)
        self.step_count = 0
        return self.current_task["data"]

    def step(self, action):
        self.step_count += 1

        reward = grade(
            action,
            self.current_task["solution"],
            self.current_task["data"]
        )

        chosen_area = None
        if action.get("allocations"):
            chosen_area = action["allocations"][0].get("area")

        done = True

        info = {
            "chosen_area": chosen_area,
            "correct_area": self.current_task["solution"]["best_area"]
        }

        return self.current_task["data"], reward, done, info

    def state(self):
        return self.current_task