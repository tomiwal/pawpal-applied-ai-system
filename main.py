#!/usr/bin/env python
"""
PawPal+ Scheduler Demo
Foundation layer demonstration of the pet care scheduling system.
"""

from models import Owner, Pet, Task, Scheduler


def main():
    print("\n" + "=" * 70)
    print("PawPal+ - Pet Care Scheduler (Foundation Layer)")
    print("=" * 70)

    # Setup owner and pets
    print("\n[INPUT]")

    owner = Owner(
        name="Jordan",
        preferences=["morning", "consistent"],
        time_available_minutes=480
    )

    dog = Pet(name="Biscuit", species="dog", age=4, special_needs=["hip_dysplasia"])
    cat = Pet(name="Mittens", species="cat", age=2, special_needs=[])

    print(f"Owner: {owner.name}")
    print(f"Available time: {owner.time_available_minutes} minutes (8 hours)")

    print(f"\nPets:")
    print(f"  • {dog.name} ({dog.species}, age {dog.age}) - Special needs: hip dysplasia")
    print(f"  • {cat.name} ({cat.species}, age {cat.age}) - Special needs: None")

    # Define tasks
    tasks = [
        Task(title="Morning walk", priority="high", duration_minutes=30, frequency="daily"),
        Task(title="Breakfast", priority="high", duration_minutes=10, frequency="daily"),
        Task(title="Playtime", priority="medium", duration_minutes=60, frequency="daily"),
        Task(title="Medication (Biscuit)", priority="high", duration_minutes=5, frequency="daily"),
        Task(title="Afternoon walk", priority="medium", duration_minutes=30, frequency="daily"),
        Task(title="Dinner", priority="high", duration_minutes=10, frequency="daily"),
        Task(title="Grooming", priority="low", duration_minutes=45, frequency="weekly"),
        Task(title="Training", priority="medium", duration_minutes=30, frequency="daily"),
    ]

    print(f"\nAvailable tasks ({len(tasks)}):")
    for task in tasks:
        print(f"  • {task.title}: {task.duration_minutes}m ({task.priority} priority)")

    # Generate schedule
    print("\n" + "-" * 70)
    print("[PROCESSING]")
    print("-" * 70)

    scheduler = Scheduler(owner=owner, pets=[dog, cat], available_tasks=tasks)

    try:
        schedule = scheduler.generate_plan(pet=dog)

        # Display results
        print("\n" + "-" * 70)
        print("[RESULTS]")
        print("-" * 70)

        print(f"\nSchedule for {dog.name}")
        total_hours = schedule.total_time_minutes // 60
        total_mins = schedule.total_time_minutes % 60
        print(f"Total duration: {schedule.total_time_minutes} minutes ({total_hours}h {total_mins}m)")
        print(f"Tasks included: {len(schedule.tasks)}")

        print("\nScheduled activities:")
        current_time_minutes = 8 * 60
        for i, task in enumerate(schedule.tasks, 1):
            hour = current_time_minutes // 60
            minute = current_time_minutes % 60
            print(f"  {i}. {hour:02d}:{minute:02d} - {task.title} ({task.duration_minutes}m)")
            current_time_minutes += task.duration_minutes

        end_hour = current_time_minutes // 60
        end_minute = current_time_minutes % 60
        print(f"\nSchedule ends at: {end_hour:02d}:{end_minute:02d}")

        # Show unscheduled tasks
        unscheduled = set(tasks) - set(schedule.tasks)
        if unscheduled:
            print(f"\nUnscheduled tasks (insufficient time):")
            for task in unscheduled:
                print(f"  • {task.title} ({task.duration_minutes}m, {task.priority} priority)")

    except ValueError as e:
        print(f"Error generating schedule: {e}")

    print("\n" + "=" * 70)
    print("Process complete")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
