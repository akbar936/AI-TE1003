def forward_chaining(rules, facts):

    inferred = set(facts)
    reasoning_log = []

    changed = True

    while changed:

        changed = False

        for rule in rules:

            if all(condition in inferred for condition in rule.conditions):

                if rule.conclusion not in inferred:

                    inferred.add(rule.conclusion)

                    reasoning_log.append(
                        f"Applied Rule: IF {rule.conditions} THEN {rule.conclusion}"
                    )

                    changed = True

    return inferred, reasoning_log
