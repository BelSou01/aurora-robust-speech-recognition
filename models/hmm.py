from hmmlearn.hmm import GaussianHMM


def create_hmm(
    n_states=16,
    n_mix=3
):
    """
    Create a Gaussian HMM.

    Parameters
    ----------
    n_states : int
        Number of HMM states.

    n_mix : int
        Number of Gaussian mixture components.

    Returns
    -------
    model
        HMM model.
    """

    model = GaussianHMM(
        n_components=n_states,
        covariance_type="diag",
        n_iter=100
    )

    return model
