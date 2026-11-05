# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Run `python main.py` to see the demo in action:

```
============================================================
🐾 PawPal+ Scheduler Demo
============================================================

📋 Owner: Jordan
   Available time: 480 minutes

🐕 Dogs:
   - Biscuit (dog, 4 years old)
     Special needs: hip dysplasia

📝 Available tasks: 8
   - Morning walk: 30m [high]
   - Breakfast: 10m [high]
   - Playtime: 60m [medium]
   - Medication (Biscuit): 5m [high]
   - Afternoon walk: 30m [medium]
   - Dinner: 10m [high]
   - Grooming: 45m [low]
   - Training: 30m [medium]

============================================================
Generating optimized schedule...
============================================================

✅ Daily Plan for Biscuit
   Total time: 220 minutes (3h 40m)
   Tasks scheduled: 8

   1. 08:00 — Morning walk
      Duration: 30m | Priority: high
   2. 08:30 — Breakfast
      Duration: 10m | Priority: high
   3. 08:40 — Medication (Biscuit)
      Duration: 5m | Priority: high
   4. 08:45 — Dinner
      Duration: 10m | Priority: high
   5. 08:55 — Playtime
      Duration: 60m | Priority: medium
   6. 09:55 — Afternoon walk
      Duration: 30m | Priority: medium
   7. 10:25 — Training
      Duration: 30m | Priority: medium
   8. 10:55 — Grooming
      Duration: 45m | Priority: low

   Schedule ends at: 11:40
```

**Key Features:**
- Prioritizes high-priority tasks (walks, meals, medication)
- Schedules medium tasks (training, playtime) after high-priority ones
- Fits as many tasks as possible within available time
- Displays tasks in chronological order with times
- Shows unscheduled tasks if time runs out

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
python -m pytest test_models.py -v

# Run specific test:
python -m pytest test_models.py::test_sort_by_priority -v
```

Test suite coverage:
- ✅ Priority value mapping (high=3, medium=2, low=1)
- ✅ Task sorting by priority (highest first)
- ✅ Time-constrained scheduling (greedy fitting)
- ✅ Owner preferences management
- ✅ Daily task recurrence checking
- ✅ Invalid priority handling (error on unknown values)
- ✅ Edge cases: no tasks fit, zero/negative duration, empty task list
- ✅ Multi-pet scheduling support
- ✅ Case-insensitive priority handling

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_tasks_by_priority(tasks)` | Sorts by priority (high → medium → low) |
| Time filtering | `Scheduler.generate_plan()` | Adds tasks until time available runs out |
| Priority mapping | `Task.get_priority_value()` | Maps "high"→3, "medium"→2, "low"→1 |
| Schedule building | `Schedule.add_task(task)` | Tracks tasks and total duration |

## 📸 Demo Walkthrough

### CLI Demo (main.py)

1. **Initialize the system** — Create an Owner (name, available time), Pet(s) (name, species, age, special needs), and list of Tasks (title, priority, duration, frequency)
2. **Add tasks** — Provide high-priority tasks (walks, feeding, meds) and lower-priority enrichment (playtime, training, grooming)
3. **Run the scheduler** — Call `Scheduler.generate_plan(pet)` to create an optimized daily schedule
4. **View the schedule** — Display tasks in time order (starting at 8 AM), sorted by priority and constrained by available time
5. **Handle overflow** — Show unscheduled tasks if time runs out; explain why they didn't fit

### Streamlit UI Demo (app.py)

1. **Enter owner info** — Input owner name and time available (default 480 min = 8 hours)
2. **Select pet** — Choose pet name and species (dog, cat, other)
3. **Add tasks** — Create tasks with title, duration, and priority; add multiple
4. **Generate schedule** — Click the button to call the scheduler and see results
5. **View results** — See scheduled tasks sorted by priority and total time used
