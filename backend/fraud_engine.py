from rules import rule_score
from ml_model import ml_score

def fraud_decision(tx):
    rule = rule_score(tx)
    ml = ml_score(tx)

    final_score = 0.6 * ml + 0.4 * rule

    if final_score > 0.75:
        decision = "FRAUD"
    elif final_score > 0.4:
        decision = "REVIEW"
    else:
        decision = "APPROVED"

    return {
        "rule_score": round(rule, 2),
        "ml_score": round(ml, 2),
        "final_score": round(final_score, 2),
        "decision": decision
    }
