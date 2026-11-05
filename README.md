# 🐾 PawPal+

A smart pet care scheduling assistant that helps busy pet owners create optimized daily plans for their pets.

## Overview

**PawPal+** uses intelligent task scheduling to organize pet care activities based on priority, duration, and available time. Perfect for owners juggling multiple pets and competing tasks.

**Features:**
- 📅 Priority-based task scheduling (high → medium → low)
- ⏱️ Time-constrained planning (fits tasks within available hours)
- 🐕 Multi-pet support (manage schedules for different pets)
- 🎯 Smart filtering (automatically handles tasks that don't fit)
- 💾 Persistent storage (save and load schedules)
- ✅ Comprehensive testing (11 test cases covering edge cases)

## Quick Start

### Installation

```bash
git clone https://github.com/tomiwal/pawpal-project.git
cd pawpal-project

python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
```

### Run the Demo

```bash
python main.py
```

Output:
```
🐾 PawPal+ Scheduler Demo

✅ Daily Plan for Biscuit
   Total time: 220 minutes (3h 40m)
   Tasks scheduled: 8

   1. 08:00 — Morning walk (30m | high)
   2. 08:30 — Breakfast (10m | high)
   3. 08:40 — Medication (5m | high)
   4. 08:45 — Dinner (10m | high)
   5. 08:55 — Playtime (60m | medium)
   6. 09:55 — Afternoon walk (30m | medium)
   7. 10:25 — Training (30m | medium)
   8. 10:55 — Grooming (45m | low)

   Schedule ends at: 11:40
```

### Run the Web UI

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

## How It Works

### Core Algorithm

1. **Priority Mapping** — Convert text priorities to numeric values (high=3, medium=2, low=1)
2. **Sort Tasks** — Order all tasks by priority (highest first)
3. **Greedy Fitting** — Add tasks to schedule until time runs out
4. **Validate Input** — Reject invalid data (negative duration, unknown priority, etc.)
5. **Display Results** — Show scheduled tasks in chronological order with times

### System Architecture

```
Owner → Pet → Task → Scheduler → Schedule
```

- **Owner**: Stores availability (minutes/day) and preferences
- **Pet**: Holds pet info and special needs
- **Task**: Represents a care activity (walks, feeding, training, etc.)
- **Scheduler**: Orchestrates planning (sorts, filters, builds schedule)
- **Schedule**: Final plan with ordered tasks and total duration

## Testing

Run the full test suite:

```bash
python -m pytest test_models.py -v
```

**Test Coverage:**
- ✅ Priority value mapping
- ✅ Task sorting by priority
- ✅ Time-constrained scheduling
- ✅ Invalid priority handling (error on unknown values)
- ✅ Edge cases: no tasks fit, zero/negative duration, empty lists
- ✅ Multi-pet scheduling
- ✅ Case-insensitive input handling

## File Structure

```
pawpal-project/
├── models.py           # Core classes (Owner, Pet, Task, Scheduler, Schedule)
├── app.py              # Streamlit web UI
├── main.py             # CLI demo script
├── persistence.py      # Save/load schedules to JSON
├── test_models.py      # Comprehensive test suite (11 tests)
├── diagrams/
│   └── uml.mmd         # UML class diagram
├── requirements.txt    # Dependencies
└── README.md           # This file
```

## Data Persistence

Save a schedule:
```python
from persistence import save_schedule
filename = save_schedule(schedule, pet_name="Biscuit")
```

Load a schedule:
```python
from persistence import load_schedule
schedule, pet_name = load_schedule(filename)
```

Load task library:
```python
from persistence import load_task_library
tasks = load_task_library("task_library.json")
```

## Key Classes

### Scheduler
```python
scheduler = Scheduler(owner=owner, pets=[pet1, pet2], available_tasks=tasks)
schedule = scheduler.generate_plan(pet=pet1)
```

Raises `ValueError` if:
- No pets available
- Task has invalid/negative duration
- No tasks fit in available time

### Task
```python
task = Task(
    title="Morning walk",
    priority="high",  # high, medium, low
    duration_minutes=30,
    frequency="daily"  # daily, weekly, etc.
)
priority_value = task.get_priority_value()  # Returns 3, 2, or 1
```

## Design Decisions

**Priority-based greedy scheduling** — Tasks are sorted by priority and added in order until time runs out. This prioritizes critical tasks (feeding, medication) over enrichment. Trade-off: may not be optimal packing, but ensures important tasks get scheduled.

**Fail-fast validation** — Invalid inputs raise errors immediately rather than silently defaulting. Makes bugs obvious during testing.

**Separation of concerns** — Scheduling logic (`models.py`) is independent of UI (`app.py`), making it testable and reusable.

## Future Enhancements

- Time slot constraints (e.g., walks only in morning/evening)
- Weighted prioritization (combine priority + urgency)
- Recurring task patterns (weekly, monthly)
- Conflict detection (overlapping tasks)
- Cost optimization (minimize owner fatigue)

## License

Project completed for AI110 Module 2 coursework.

## Author

James Tomiwa  
[GitHub](https://github.com/tomiwal)
