import numpy as np


def combine_mfcc_pncc(
    mfcc,
    pncc
):
    """
    Combine MFCC and PNCC feature streams.

    Parameters
    ----------
    mfcc : ndarray
        MFCC feature stream.

    pncc : ndarray
        PNCC feature stream.

    Returns
    -------
    ndarray
        Multi-stream acoustic representation.
    """

    if mfcc.shape[1] != pncc.shape[1]:
        raise ValueError(
            "MFCC and PNCC streams must have "
            "the same number of frames."
        )

    return np.concatenate(
        [mfcc, pncc],
        axis=0
    )
