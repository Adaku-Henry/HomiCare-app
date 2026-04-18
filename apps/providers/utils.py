def calculate_provider_score(provider):

    score = (
        provider.rating * 2 +
        provider.jobs_completed
    )

    return score