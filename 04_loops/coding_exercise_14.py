def mark_completed_tasks(tasks: list[str]) -> list[str]:
    completed_tasks = []

    for task in tasks:
        completed_tasks.append(f"Completed: {task}")

    return completed_tasks
