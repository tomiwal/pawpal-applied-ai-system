#!/usr/bin/env python3
"""
PawPal AI System Demo
Demonstrates the complete orchestration flow for pet care scheduling.
"""

from models import Owner, Pet, Task
from ai_agent import AIAgent


def main():
    print("\n" + "=" * 70)
    print("PawPal AI - Pet Care Scheduling System")
    print("=" * 70)

    # Input Stage
    print("\n[INPUT]")

    owner = Owner(
        name="Sarah",
        preferences=["morning exercise", "consistent routine"],
        time_available_minutes=120
    )

    pet = Pet(
        name="Biscuit",
        species="Dog",
        age=5,
        special_needs=["high_energy", "daily_medication"]
    )

    print(f"Owner: {owner.name}")
    print(f"Available time: {owner.time_available_minutes} minutes")
    print(f"\nPet: {pet.name}")
    print(f"Species: {pet.species} (Age {pet.age})")
    print(f"Special needs: {', '.join(pet.special_needs)}")

    # Define available tasks
    available_tasks = [
        Task("Morning walk", "high", 30, "daily"),
        Task("Breakfast", "high", 10, "daily"),
        Task("Medication", "high", 5, "daily"),
        Task("Playtime", "medium", 45, "daily"),
        Task("Training", "medium", 30, "daily"),
        Task("Evening walk", "medium", 20, "daily"),
    ]

    print(f"\nAvailable tasks ({len(available_tasks)}):")
    for task in available_tasks:
        print(f"  • {task.title}: {task.duration_minutes}m ({task.priority} priority)")

    # Processing Stage
    print("\n" + "-" * 70)
    print("[PROCESSING]")
    print("-" * 70)

    ai_agent = AIAgent()
    schedule, reasoning, guidelines = ai_agent.orchestrate(pet, owner, available_tasks)

    # Output Stage
    print("\n" + "-" * 70)
    print("[RESULTS]")
    print("-" * 70)

    print(f"\nSchedule for {pet.name}")
    print(f"Total duration: {schedule.get_total_duration()} minutes")
    print(f"Tasks included: {len(schedule.tasks)}")

    print("\nScheduled activities:")
    current_time_minutes = 8 * 60
    for i, task in enumerate(schedule.tasks, 1):
        hours = current_time_minutes // 60
        minutes = current_time_minutes % 60
        print(f"  {i}. {hours:02d}:{minutes:02d} - {task.title} ({task.duration_minutes}m)")
        current_time_minutes += task.duration_minutes

    print(f"\nSystem reasoning:")
    print(f"  {reasoning}")

    print(f"\nPet care guidelines applied:")
    print(f"  • Daily exercise requirement: {guidelines['exercise_minutes']} minutes")
    print(f"  • Feeding frequency: {guidelines['feeding_times']} times per day")

    print("\n" + "=" * 70)
    print("Process complete")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
