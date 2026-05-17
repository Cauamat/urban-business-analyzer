def calcular_score(lugares):

    concorrentes = len(lugares)

    if concorrentes == 0:
        return {
            "score": 0,
            "concorrentes": 0,
            "rating_medio": 0,
            "reviews_medio": 0
        }

    rating_medio = (
        sum(l["rating"] for l in lugares)
        / concorrentes
    )

    reviews_medio = (
        sum(l["reviews"] for l in lugares)
        / concorrentes
    )

    # NORMALIZAÇÕES

    rating_score = (rating_medio / 5) * 30

    reviews_score = min(reviews_medio / 500, 1) * 40

    concorrencia_score = max(0, 30 - concorrentes)

    score = (
        rating_score
        + reviews_score
        + concorrencia_score
    )

    score = round(min(score, 100), 2)

    return {
        "score": score,
        "concorrentes": concorrentes,
        "rating_medio": round(rating_medio, 2),
        "reviews_medio": round(reviews_medio, 2)
    } 