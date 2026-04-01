def grade(action, solution, observation):
    score = 0.0

    chosen_area = None
    if action.get("allocations"):
        chosen_area = action["allocations"][0].get("area")

    # Correct decision
    if chosen_area == solution["best_area"]:
        score += 0.6
    else:
        score -= 0.3  # penalty for wrong choice

    reasoning = action.get("reasoning", "").lower()

    if "severity" in reasoning:
        score += 0.2
    if "people" in reasoning:
        score += 0.2

    return max(0.0, min(score, 1.0))