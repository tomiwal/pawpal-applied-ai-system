"""
Data persistence module for PawPal+
Save and load schedules to/from JSON files.
"""

import json
from datetime import datetime
from models import Owner, Pet, Task, Schedule, Scheduler


def save_schedule(schedule, pet_name, filename=None):
    """Save a schedule to JSON file."""
    if filename is None:
        filename = f"schedule_{pet_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    data = {
        "pet": pet_name,
        "day": schedule.day,
        "total_time_minutes": schedule.total_time_minutes,
        "tasks": [
            {
                "title": task.title,
                "priority": task.priority,
                "duration_minutes": task.duration_minutes,
                "frequency": task.frequency
            }
            for task in schedule.tasks
        ],
        "saved_at": datetime.now().isoformat()
    }

    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

    return filename


def load_schedule(filename):
    """Load a schedule from JSON file."""
    with open(filename, 'r') as f:
        data = json.load(f)

    tasks = [
        Task(
            title=t["title"],
            priority=t["priority"],
            duration_minutes=t["duration_minutes"],
            frequency=t["frequency"]
        )
        for t in data["tasks"]
    ]

    schedule = Schedule(
        day=data["day"],
        tasks=tasks,
        total_time_minutes=data["total_time_minutes"]
    )

    return schedule, data["pet"]


def save_task_library(tasks, filename="task_library.json"):
    """Save a library of tasks to JSON file."""
    data = {
        "tasks": [
            {
                "title": task.title,
                "priority": task.priority,
                "duration_minutes": task.duration_minutes,
                "frequency": task.frequency
            }
            for task in tasks
        ],
        "saved_at": datetime.now().isoformat()
    }

    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

    return filename


def load_task_library(filename="task_library.json"):
    """Load a library of tasks from JSON file."""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)

        tasks = [
            Task(
                title=t["title"],
                priority=t["priority"],
                duration_minutes=t["duration_minutes"],
                frequency=t["frequency"]
            )
            for t in data["tasks"]
        ]

        return tasks
    except FileNotFoundError:
        return []
