# Rule-Based Expert System (Forward Chaining)

A simple **Rule-Based Expert System** built using **Python** that demonstrates how artificial intelligence systems can infer conclusions from user-provided facts using **if–then rules** and **forward chaining**.

This project simulates a basic **medical diagnosis assistant** where users enter symptoms and the system applies rules to infer possible conditions and recommendations.

---

# 📌 Project Overview

Expert systems are one of the earliest forms of Artificial Intelligence. They mimic the decision-making ability of a human expert by using a **knowledge base of rules** and an **inference engine**.

In this project:

- Users provide symptoms as input
- The system evaluates rules
- New facts are inferred using **forward chaining**
- The reasoning process is logged step-by-step

---

# ⚙️ How It Works

The system consists of three main components:

### 1️⃣ Knowledge Base
Stores a set of **if–then rules**.

Example rule:
```bash
    IF fever AND cough
    THEN flu
```

---

### 2️⃣ Fact Base
Stores facts provided by the user.

Example:
```bash
    fever
    body_pain
```

---


### 3️⃣ Inference Engine
Applies rules using **Forward Chaining**.

Forward chaining works as:
```bash
    Facts → Match Rules → Infer New Facts → Repeat Until No More Rules Apply
```


---

# ✨ Features

- Simple rule engine using **if–then rules**
- Accepts **user symptoms as facts**
- Implements **forward chaining inference**
- Supports **multi-step rule chaining**
- Displays **step-by-step reasoning process**
- Generates conclusions based on inferred knowledge

---

# 🗂 Project Structure
```bash
    expert_system/
        │
        ├── main.py # Main program
        ├── rules.py # Knowledge base (rules)
        ├── inference_engine.py # Forward chaining logic
        └── README.md
```

---


---

# 📥 Installation

Clone the repository:

```bash
    git clone https://github.com/tayade-aniket/Syntecxhub_expert_system
```

Navigate to the project folder:

```bash
    cd Syntecxhub_expert_system
```


No external libraries are required. This project runs using **standard Python**.

---

# ▶️ Running the Program

Run the program using:
```bash
    python main.py
```

---

# 🧪 Example Execution

### Input
```bash
    Enter symptoms separated by comma
    Example: fever,cough,body_pain
    Symptoms: fever,body_pain
```

### Output
```bash
--- Reasoning Process ---
    Applied Rule: IF ['fever'] THEN possible_infection
    Applied Rule: IF ['body_pain'] THEN fatigue
```

--- Final Knowledge Base ---
```bash
    fever
    body_pain
    possible_infection
    fatigue
```

# 🔗 Example of Multi-Step Inference

Rules can trigger other rules.

Example chain:
```bash
    fever + cough → flu
    flu + body_pain → viral_infection
    viral_infection → doctor_visit
```

This allows the system to perform **multi-step reasoning**, similar to human expert decision-making.

---

# 📚 Author
Mr. Aniket Tayade.
tayadeanni@gmail.com
