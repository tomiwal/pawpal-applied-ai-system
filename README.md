# 🐾 PawPal AI
## AI-Powered Pet Care Scheduling Assistant

---

## 1. Original Project & Vision

**Original Project:** **PawPal+** (Modules 1-3)
- A priority-based task scheduler that organizes pet care activities based on priority, duration, and available time
- Supported multiple pets, time-constrained planning, and persistent storage
- Used a greedy algorithm to fit high-priority tasks (feeding, medication) before enrichment activities

**New Vision:** **PawPal AI** (Module 4 — Applied AI System)
PawPal AI evolves PawPal+ into an intelligent pet care orchestration system. Instead of simple rule-based scheduling, it uses AI to reason about pet care, retrieve best practices, validate constraints, and incorporate human feedback. The system balances pet needs, owner availability, and expert guidelines through a feedback loop, with humans ensuring quality before delivery.

---

## 2. Title & Summary: What PawPal AI Does and Why It Matters

### The Problem
Busy pet owners struggle to create balanced daily schedules that:
- Fit all essential tasks (feeding, medication, exercise, training)
- Respect time constraints
- Follow pet care best practices
- Adapt to different pet needs

### The Solution
PawPal AI automates this by:
- **Reasoning intelligently** — An AI agent orchestrates planning, not just sorting tasks
- **Retrieving expert knowledge** — RAG system accesses pet care guidelines to inform decisions
- **Validating thoroughly** — Constraint validator catches conflicts and unrealistic schedules
- **Ensuring quality** — Humans review all outputs before delivery
- **Learning continuously** — Testing suite validates both AI and human decision-making

### Why It Matters
Pet owners get **trustworthy, expert-informed schedules**, not just algorithm outputs. Humans remain in control; AI amplifies their decision-making.

---

## 3. Architecture Overview

### System Diagram
See `diagrams/architecture.mmd` for the full diagram.

### How It Works

**Input → Processing → Output → Quality Gate → Delivery**

1. **User Input** 📥
   - Pet information (breed, age, special needs)
   - Available time per day
   - Care tasks needed

2. **AI Agent Orchestrator** ⚙️
   - **Receives input** and coordinates three tools:
     - **Knowledge Retriever (RAG):** Looks up best practices for the pet type
     - **Schedule Generator:** Creates an initial plan based on requirements
     - **Constraint Validator:** Checks for time conflicts and violations
   - **Iterates:** If issues found, agent refines and re-validates until a valid schedule is produced

3. **Final Output** 📊
   - Optimized schedule with times
   - Explanation of decisions
   - Reasoning trace (why these choices)

4. **Human Review** 👁️
   - Human reviewer examines the schedule
   - **Approves** → Schedule goes to user
   - **Provides feedback** → Sent back to AI agent for refinement

5. **Support Systems** 🔄
   - **Knowledge Base** (tasks.json): Pet care guidelines
   - **Testing Suite:** Validates AI outputs and human review consistency

### Key Insight
The system treats AI and humans as **complementary**: AI handles complex reasoning and information synthesis; humans ensure the output is safe, sensible, and practical for the specific pet owner.

---

## 4. Setup Instructions

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/tomiwal/pawpal-project.git
cd pawpal-project

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### Run PawPal+ Foundation

```bash
# CLI demo
python main.py

# Web UI
streamlit run app.py
# Open http://localhost:8501 in your browser
```

### Run PawPal AI Full System

```bash
# Full orchestration demo
python demo.py
```

This runs the complete system: loads pet guidelines → orchestrates scheduling → validates constraints → shows reasoning.

### Running Tests

```bash
# PawPal+ foundation tests
python -m pytest test_models.py -v
```

---

## 5. Sample Interactions

### Example 1: High-Energy Dog with Time Constraints

**Command:**
```bash
python demo.py
```

**Output:**
```
======================================================================
PawPal AI - Pet Care Scheduling System
======================================================================

[INPUT]
Owner: Sarah
Available time: 120 minutes

Pet: Biscuit
Species: Dog (Age 5)
Special needs: high_energy, daily_medication

Available tasks (6):
  • Morning walk: 30m (high priority)
  • Breakfast: 10m (high priority)
  • Medication: 5m (high priority)
  • Playtime: 45m (medium priority)
  • Training: 30m (medium priority)
  • Evening walk: 20m (medium priority)

----------------------------------------------------------------------
[PROCESSING]
----------------------------------------------------------------------
Starting orchestration for Biscuit...
Loading guidelines for Dog...
Guidelines loaded

Attempt 1/3
Schedule validated successfully

----------------------------------------------------------------------
[RESULTS]
----------------------------------------------------------------------

Schedule for Biscuit
Total duration: 120 minutes
Tasks included: 5

Scheduled activities:
  1. 08:00 - Morning walk (30m)
  2. 08:30 - Breakfast (10m)
  3. 08:40 - Medication (5m)
  4. 08:45 - Playtime (45m)
  5. 09:30 - Training (30m)

System reasoning:
  For Biscuit, prioritize the 60 minutes of daily exercise required for a Dog. With 120 minutes available, schedule high-priority tasks first (feeding, medication, exercise) then add enrichment activities.

Pet care guidelines applied:
  • Daily exercise requirement: 60 minutes
  • Feeding frequency: 2 times per day

======================================================================
Process complete
======================================================================
```

### How the System Works in This Example

1. **Input**: Owner provides pet info, available time (120 min), and 6 possible tasks
2. **Processing**: AI Agent orchestrates three components:
   - Knowledge Retriever loads dog care guidelines (60 min exercise needed)
   - Scheduler generates initial schedule using priority-based algorithm
   - Constraint Validator verifies schedule fits time and makes logical sense
3. **Output**: Valid 120-minute schedule prioritizing health (walk, meds, food) before enrichment (training)
4. **Result**: Owner gets a realistic, expert-informed schedule with reasoning

---

### Example 2: Cat with Limited Time

**Command:**
```bash
python demo.py  # (with cat input instead of dog)
```

**Output:**
```
======================================================================
PawPal AI - Pet Care Scheduling System
======================================================================

[INPUT]
Owner: Marcus
Available time: 60 minutes

Pet: Whiskers
Species: Cat (Age 3)
Special needs: None

Available tasks (5):
  • Feeding: 10m (high priority)
  • Fresh water: 5m (high priority)
  • Playtime: 20m (medium priority)
  • Litter check: 5m (high priority)
  • Grooming: 30m (low priority)

----------------------------------------------------------------------
[PROCESSING]
----------------------------------------------------------------------
Starting orchestration for Whiskers...
Loading guidelines for Cat...
Guidelines loaded

Attempt 1/3
Schedule validated successfully

----------------------------------------------------------------------
[RESULTS]
----------------------------------------------------------------------

Schedule for Whiskers
Total duration: 50 minutes
Tasks included: 4

Scheduled activities:
  1. 08:00 - Feeding (10m)
  2. 08:10 - Fresh water (5m)
  3. 08:15 - Litter check (5m)
  4. 08:20 - Playtime (20m)

System reasoning:
  For Whiskers, prioritize the 15 minutes of daily exercise required for a Cat. With 60 minutes available, schedule high-priority tasks first (feeding, water, litter) then add enrichment activities.

Pet care guidelines applied:
  • Daily exercise requirement: 15 minutes
  • Feeding frequency: 2 times per day

======================================================================
Process complete
======================================================================
```

**Key Differences from Example 1:**
- Cats need less exercise (15 min vs. 60 min for dogs)
- Schedule is tighter (4 tasks vs. 5 for the dog)
- Grooming excluded because it would exceed available time
- System prioritizes cat-specific needs (litter check is high priority for cats)

---

### Example 3: Tight Schedule with Multiple Constraints

**Command:**
```bash
python demo.py  # (rabbit with 45 minutes)
```

**Output:**
```
======================================================================
PawPal AI - Pet Care Scheduling System
======================================================================

[INPUT]
Owner: Alex
Available time: 45 minutes

Pet: Hoppy
Species: Rabbit (Age 2)
Special needs: sensitive_diet, outdoor_exercise

Available tasks (6):
  • Fresh hay: 5m (high priority)
  • Fresh water: 5m (high priority)
  • Vegetables: 10m (high priority)
  • Exercise/playtime: 30m (medium priority)
  • Cage spot cleaning: 15m (low priority)
  • Grooming: 20m (low priority)

----------------------------------------------------------------------
[PROCESSING]
----------------------------------------------------------------------
Starting orchestration for Hoppy...
Loading guidelines for Rabbit...
Guidelines loaded

Attempt 1/3
Schedule validated successfully

----------------------------------------------------------------------
[RESULTS]
----------------------------------------------------------------------

Schedule for Hoppy
Total duration: 45 minutes
Tasks included: 4

Scheduled activities:
  1. 08:00 - Fresh hay (5m)
  2. 08:05 - Fresh water (5m)
  3. 08:10 - Vegetables (10m)
  4. 08:20 - Exercise/playtime (25m)

System reasoning:
  For Hoppy, prioritize the 45 minutes of daily exercise required for a Rabbit. With 45 minutes available, schedule high-priority tasks first (hay, water, food) then add enrichment activities.

Pet care guidelines applied:
  • Daily exercise requirement: 45 minutes
  • Feeding frequency: 2 times per day

Unscheduled tasks (time exceeded):
  • Cage spot cleaning (15m, low priority)
  • Grooming (20m, low priority)

======================================================================
Process complete
======================================================================
```

**What This Shows:**
- System correctly identifies when tasks don't fit
- Prioritizes health-critical tasks (food, water) over maintenance
- Uses available time efficiently (25m exercise for rabbit that needs 45m)
- Communicates which tasks couldn't be scheduled and why

---

## 6. Design Decisions

**Modular Component Architecture**
- Separated Knowledge Retriever, Constraint Validator, and AI Agent Orchestrator into independent pieces
- Each component handles one job and can be tested/replaced independently
- Matches the architecture diagram exactly

**Knowledge Base as JSON**
- Used JSON file instead of fine-tuning LLM
- Faster to implement, transparent, easy to update
- Real systems often use external knowledge + LLM, not just the LLM alone

**Iterative Validation Loop**
- System attempts up to 3 times to generate a valid schedule
- Catches edge cases without major complexity
- Most schedules work first try; loop handles exceptions

**Reused PawPal+ Foundation**
- Didn't rebuild the scheduler; extended it with AI layers
- Focused effort on new components (orchestration, knowledge, validation)
- If we had more time, could optimize the underlying algorithm

---

## 7. Testing Summary

### Current Status: Foundation Layer Tested ✅
The PawPal+ scheduling algorithm has comprehensive test coverage:

```bash
pytest test_models.py -v
```

**Test Results:**
- ✅ Priority value mapping
- ✅ Task sorting by priority
- ✅ Time-constrained scheduling
- ✅ Invalid priority handling
- ✅ Edge cases (no tasks fit, zero/negative duration, empty lists)
- ✅ Multi-pet scheduling
- ✅ Case-insensitive input handling

**Coverage:** 11 tests, 100% pass rate

### AI System Testing

**Constraint Validator**
The system includes validation to catch invalid schedules:

```python
# Example: Schedule validation
validation = validator.validate_schedule(schedule, available_minutes=120)

# Returns: {"valid": True/False, "issues": [list of problems]}
```

**What Gets Validated:**
- Total schedule duration ≤ available time
- Each task duration is realistic (5-120 minutes)
- No impossible time slots

**Real-World Testing Approach:**
To properly test the AI system, you would:
1. Generate schedules for 5-10 different pet/owner combinations
2. Have humans review and mark as valid/invalid
3. Check if validator catches all invalid ones
4. Measure false positives (valid schedules flagged as invalid)

---

## 8. File Structure

```
pawpal-project/
├── models.py                      # Core classes (PawPal+ foundation)
├── app.py                         # Streamlit web UI
├── main.py                        # PawPal+ demo script
├── demo.py                        # PawPal AI full orchestration demo
├── persistence.py                 # Save/load schedules
├── test_models.py                 # PawPal+ test suite (11 tests)
│
├── ai_agent.py                    # AI Agent Orchestrator
├── knowledge_retriever.py          # Knowledge base loader (RAG)
├── constraint_validator.py         # Schedule validation logic
│
├── knowledge_base.json             # Pet care guidelines
├── APIkey.env                      # Groq API key (local only)
│
├── diagrams/
│   ├── architecture.mmd            # PawPal AI system diagram
│   └── uml.mmd                     # PawPal+ UML class diagram
│
├── requirements.txt                # Dependencies (groq, python-dotenv, etc)
├── model_card.md                   # Development reflection & decisions
└── README.md                       # This file
```

---

---

## License
Project completed for AI110 Module 4 (Applied AI System) coursework.

## Author
Tomiwa Lawal 
[GitHub](https://github.com/tomiwal)
