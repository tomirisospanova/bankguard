def rule_score(tx):
    score = 0.0

    if tx.amount > 1_000_000:
        score += 0.4

    if tx.country != tx.home_country:
        score += 0.3

    if tx.device_new:
        score += 0.3

    return min(score, 1.0)
