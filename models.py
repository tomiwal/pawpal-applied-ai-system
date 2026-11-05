class Owner:
    def __init__(self, name, preferences, time_available_minutes):
        self.name = name
        self.preferences = preferences
        self.time_available_minutes = time_available_minutes

    def add_preference(self, preference: str):
        self.preferences.append(preference)

    def get_preferences(self):
        return self.preferences


class Pet:
    def __init__(self, name, species, age, special_needs):
        self.name = name
        self.species = species
        self.age = age
        self.special_needs = special_needs

    def get_special_needs(self):
        return self.special_needs


class Task:
    def __init__(self, title, priority, duration_minutes, frequency):
        self.title = title
        self.priority = priority
        self.duration_minutes = duration_minutes
        self.frequency = frequency

    def get_priority_value(self):
        priority_map = {"high": 3, "medium": 2, "low": 1}
        priority_key = self.priority.lower()
        if priority_key not in priority_map:
            raise ValueError(f"Invalid priority: {self.priority}. Must be 'high', 'medium', or 'low'.")
        return priority_map[priority_key]   



    def is_due_today(self):
        return self.frequency.lower() == "daily"


class Schedule:
    def __init__(self, day, tasks, total_time_minutes):
        self.day = day
        self.tasks = tasks
        self.total_time_minutes = total_time_minutes

    def add_task(self, task: Task):
        self.tasks.append(task)
        self.total_time_minutes += task.duration_minutes

    def get_total_duration(self):
        return self.total_time_minutes


class Scheduler:
    def __init__(self, owner, pets, available_tasks):
        self.owner = owner
        self.pets = pets if isinstance(pets, list) else [pets]
        self.available_tasks = available_tasks

    def generate_plan(self, pet=None):
        """Generate a daily schedule. If pet is None, uses first pet."""
        if pet is None:
            if not self.pets:
                raise ValueError("No pets available. Add a pet to schedule.")
            pet = self.pets[0]

        # Validate duration values
        for task in self.available_tasks:
            if task.duration_minutes <= 0:
                raise ValueError(f"Task '{task.title}' has invalid duration: {task.duration_minutes}")

        sorted_tasks = self.sort_tasks_by_priority(self.available_tasks)
        scheduled_tasks = []
        total_time = 0

        for task in sorted_tasks:
            if total_time + task.duration_minutes <= self.owner.time_available_minutes:
                scheduled_tasks.append(task)
                total_time += task.duration_minutes

        if not scheduled_tasks:
            raise ValueError(f"No tasks fit in available time ({self.owner.time_available_minutes} minutes)")

        schedule = Schedule(day="today", tasks=scheduled_tasks, total_time_minutes=total_time)
        return schedule

    def sort_tasks_by_priority(self, tasks: list):
        """Sort tasks by priority (high to low)."""
        if not tasks:
            return []
        sorted_tasks = sorted(tasks, key=lambda task: task.get_priority_value(), reverse=True)
        return sorted_tasks

