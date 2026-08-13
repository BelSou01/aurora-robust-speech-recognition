import numpy as np


def accuracy(
    reference,
    hypothesis
):
    """
    Compute recognition accuracy.
    """

    reference = np.asarray(reference)
    hypothesis = np.asarray(hypothesis)

    if len(reference) != len(hypothesis):
        raise ValueError(
            "Reference and hypothesis must have "
            "the same length."
        )

    return np.mean(
        reference == hypothesis
    ) * 100.0
