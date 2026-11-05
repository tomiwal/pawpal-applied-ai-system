#!/usr/bin/env python
"""
PawPal+ Demo Script
End-to-end example showing the scheduling system in action.
"""

from models import Owner, Pet, Task, Scheduler


def main():
    print("=" * 60)
    print("🐾 PawPal+ Scheduler Demo")
    print("=" * 60)

    # Create owner
    owner = Owner(
        name="Jordan",
        preferences=["morning", "consistent"],
        time_available_minutes=480  # 8 hours
    )
    print(f"\n📋 Owner: {owner.name}")
    print(f"   Available time: {owner.time_available_minutes} minutes")

    # Create pets
    dog = Pet(name="Biscuit", species="dog", age=4, special_needs=["hip dysplasia"])
    cat = Pet(name="Mittens", species="cat", age=2, special_needs=[])

    print(f"\n🐕 Dogs:")
    print(f"   - {dog.name} ({dog.species}, {dog.age} years old)")
    print(f"     Special needs: {', '.join(dog.special_needs) if dog.special_needs else 'None'}")

    print(f"\n🐈 Cats:")
    print(f"   - {cat.name} ({cat.species}, {cat.age} years old)")
    print(f"     Special needs: {', '.join(cat.special_needs) if cat.special_needs else 'None'}")

    # Create tasks
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

    print(f"\n📝 Available tasks: {len(tasks)}")
    for task in tasks:
        print(f"   - {task.title}: {task.duration_minutes}m [{task.priority}]")

    # Generate schedule
    print("\n" + "=" * 60)
    print("Generating optimized schedule...")
    print("=" * 60)

    scheduler = Scheduler(owner=owner, pets=[dog, cat], available_tasks=tasks)

    try:
        schedule = scheduler.generate_plan(pet=dog)

        print(f"\n✅ Daily Plan for {dog.name}")
        print(f"   Total time: {schedule.total_time_minutes} minutes ({schedule.total_time_minutes // 60}h {schedule.total_time_minutes % 60}m)")
        print(f"   Tasks scheduled: {len(schedule.tasks)}\n")

        current_time_minutes = 8 * 60  # Start at 8 AM
        for i, task in enumerate(schedule.tasks, 1):
            hour = current_time_minutes // 60
            minute = current_time_minutes % 60
            print(f"   {i}. {hour:02d}:{minute:02d} — {task.title}")
            print(f"      Duration: {task.duration_minutes}m | Priority: {task.priority}")
            current_time_minutes += task.duration_minutes

        end_hour = current_time_minutes // 60
        end_minute = current_time_minutes % 60
        print(f"\n   Schedule ends at: {end_hour:02d}:{end_minute:02d}")

        # Show unscheduled tasks
        unscheduled = set(tasks) - set(schedule.tasks)
        if unscheduled:
            print(f"\n⚠️  Unscheduled tasks (not enough time):")
            for task in unscheduled:
                print(f"   - {task.title} ({task.duration_minutes}m, {task.priority})")

    except ValueError as e:
        print(f"❌ Error generating schedule: {e}")

    print("\n" + "=" * 60)
    print("Demo complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
