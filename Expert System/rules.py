class Rule:

    def __init__(self, conditions, conclusion):
        self.conditions = conditions
        self.conclusion = conclusion


rules = [
    Rule(["fever", "cough"], "flu"),
    Rule(["flu", "body_pain"], "viral_infection"),
    Rule(["viral_infection"], "doctor_visit"),

    Rule(["fever"], "possible_infection"),
    Rule(["body_pain"], "fatigue")
]
