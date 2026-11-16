import os
from groq import Groq
from dotenv import load_dotenv
from knowledge_retriever import KnowledgeRetriever
from constraint_validator import ConstraintValidator
from models import Scheduler

load_dotenv("APIkey.env")


class AIAgent:
    """Orchestrates the pet care scheduling system"""

    def __init__(self):
        """Initialize the AI agent with tools and API"""
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = "llama-3.3-70b-versatile"
        self.retriever = KnowledgeRetriever()
        self.validator = ConstraintValidator()
        self.conversation_history = []

    def orchestrate(self, pet, owner, available_tasks):
        """
        Coordinate scheduling system components to create an optimized schedule.

        Args:
            pet: Pet object
            owner: Owner object
            available_tasks: List of Task objects

        Returns:
            Tuple of (schedule, reasoning, guidelines)
        """
        print(f"Starting orchestration for {pet.name}...")

        # Retrieve pet care guidelines
        print(f"Loading guidelines for {pet.species}...")
        guidelines = self.retriever.retrieve_guidelines(pet.species)
        print(f"Guidelines loaded\n")

        schedule = None
        reasoning = ""
        max_attempts = 3

        for attempt in range(max_attempts):
            print(f"Attempt {attempt + 1}/{max_attempts}")

            reasoning = self._get_reasoning(pet, owner, available_tasks, guidelines, attempt)

            try:
                scheduler = Scheduler(owner, pet, available_tasks)
                schedule = scheduler.generate_plan(pet)

                validation = self.validator.validate_schedule(
                    schedule,
                    owner.time_available_minutes
                )

                if validation["valid"]:
                    print(f"Schedule validated successfully\n")
                    break
                else:
                    issue = validation['issues'][0]
                    print(f"Validation issue: {issue}")
                    if attempt < max_attempts - 1:
                        print(f"Refining schedule...\n")

            except ValueError as e:
                print(f"Error generating schedule: {e}\n")

        return schedule, reasoning, guidelines

    def _get_reasoning(self, pet, owner, available_tasks, guidelines, attempt):
        """
        Generate reasoning for the current scheduling attempt.
        """
        reasoning = (
            f"For {pet.name}, prioritize the {guidelines['exercise_minutes']} minutes "
            f"of daily exercise required for a {pet.species}. With {owner.time_available_minutes} "
            f"minutes available, schedule high-priority tasks first (feeding, medication, exercise) "
            f"then add enrichment activities."
        )

        self.conversation_history.append({"role": "user", "content": "Pet care scheduling"})
        self.conversation_history.append({"role": "assistant", "content": reasoning})

        return reasoning
