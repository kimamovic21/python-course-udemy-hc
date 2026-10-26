def generate_numbered_tasks(tasks: list[str]) -> list[str]:
    numbered_tasks = []

    for number, task in enumerate(tasks, start=1):
        numbered_tasks.append(f"{number}. {task}")

    return numbered_tasks
