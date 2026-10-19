from rules import rules
from inference_engine import forward_chaining


def get_user_facts():

    print("Enter symptoms separated by comma")
    print("Example: fever,cough,body_pain\n")

    user_input = input("Symptoms: ")

    facts = [symptom.strip() for symptom in user_input.split(",")]

    return facts


def main():

    print("==== Medical Expert System ====\n")

    facts = get_user_facts()

    inferred, reasoning_log = forward_chaining(rules, facts)

    print("\n--- Reasoning Process ---")

    for step in reasoning_log:
        print(step)

    print("\n--- Final Knowledge Base ---")

    for fact in inferred:
        print(fact)

    if "doctor_visit" in inferred:
        print("\nRecommendation: Please consult a doctor.")


if __name__ == "__main__":
    main()
