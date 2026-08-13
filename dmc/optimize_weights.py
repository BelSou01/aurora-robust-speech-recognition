import numpy as np


def weighted_log_likelihood(
    log_likelihoods,
    weights
):
    """
    Compute a weighted combination of log-likelihoods.

    Parameters
    ----------
    log_likelihoods : ndarray
        Log-likelihood values from the different streams.

    weights : ndarray
        Stream weights.

    Returns
    -------
    float
        Combined score.
    """

    log_likelihoods = np.asarray(
        log_likelihoods
    )

    weights = np.asarray(
        weights
    )

    if len(log_likelihoods) != len(weights):
        raise ValueError(
            "Number of likelihood streams and weights "
            "must be identical."
        )

    return np.sum(
        weights * log_likelihoods
    )


def initialize_weights():
    """
    Initialize DMC stream weights.
    """

    return np.array(
        [1.0, 1.0, 1.0]
    )
