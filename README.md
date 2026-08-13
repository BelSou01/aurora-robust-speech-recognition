# Aurora Robust Speech Recognition Using MFCC, PNCC and Discriminative Model Combination

## Overview

This repository presents a robust speech recognition framework developed for noisy speech recognition using the Aurora database.

The work investigates the integration of Power-Normalized Cepstral Coefficients (PNCC) with conventional Mel-Frequency Cepstral Coefficients (MFCC) and the optimization of acoustic stream weights using a Discriminative Model Combination (DMC) approach.

The proposed framework was developed for distributed speech recognition in noisy environments.

---

## Associated Publication

**Weighting Schemes Based Discriminative Model Combination Technique for Robust Speech Recognition**

**Authors:**  
Soumeya Belabbas  
Djamel Addou

**Conference:** IC-AIRES 2021

**Publication:** Lecture Notes in Networks and Systems, Volume 361, 2022

**DOI:** 10.1007/978-3-030-92038-8_43

**Publisher:** Springer

---

## Research Objective

The main objective is to improve the robustness of speech recognition systems under noisy acoustic conditions.

The proposed approach investigates:

- MFCC acoustic features.
- PNCC acoustic features.
- Multi-stream acoustic modeling.
- Combination of MFCC and PNCC streams.
- Discriminative optimization of stream weights.
- Robust speech recognition at different SNR levels.

---

## Aurora Database

The experiments are based on the Aurora database derived from the TIDigits corpus.

The database contains continuous digit sequences recorded from adult North American speakers.

The original recordings are sampled at 20 kHz and are downsampled to 8 kHz for the experimental framework.

The noisy test conditions include SNR values ranging from -5 dB to 20 dB.

The database contains three test sets:

- Test A
- Test B
- Test C

The original speech database is not distributed with this repository.

Users must obtain the dataset from the appropriate official source and comply with its terms of use.

---

## Baseline System

The conventional baseline uses the ETSI Advanced Frontend based on:

- 12 MFCC coefficients
- Log-energy
- First-order derivatives
- Second-order derivatives

The resulting feature vector contains 39 coefficients:

```text
MFCC_E_D_A = 39 dimensions
```

The acoustic parameters are calculated every 10 ms using a 25 ms Hamming window.

---

## PNCC Frontends

Three PNCC configurations are investigated:

```text
PNCC_E_D_A = 39 dimensions
PNCC_D_A   = 36 dimensions
PNCC_D_A   = 30 dimensions
```

The experiments investigate the influence of feature dimensionality on recognition performance.

---

## Multi-Stream Acoustic Representation

The proposed frontend combines MFCC and PNCC information.

The main configurations include:

```text
MFCC-E-D-PNCC = 39 dimensions
MFCC-D-PNCC   = 36 dimensions
```

The 36-dimensional configuration combines:

- MFCC coefficients
- First-order MFCC derivatives
- PNCC coefficients

without the energy component.

---

## Discriminative Model Combination

The DMC approach optimizes the weights associated with the acoustic streams.

The optimization is based on a discriminative objective involving recognition hypotheses and Levenshtein distance.

The optimized weights reported in the study for the three MFCC-E-D-A streams are:

```text
λ0 = 0.38
λ1 = 0.95
λ2 = 1.50
```

These weights are obtained using a validation set and the DMC optimization procedure.

---

## Recognition Model

The original experimental system uses Hidden Markov Models (HMMs).

Each digit is modeled using:

- 16 HMM states
- 3 Gaussian mixtures per state

Silence models are also used for the beginning and end of sequences.

The original experiments were performed using the HTK toolkit.

---

## Experimental Pipeline

```text
Aurora Speech
      |
      v
Preprocessing
      |
      +------------------+
      |                  |
      v                  v
    MFCC                PNCC
      |                  |
      +--------+---------+
               |
               v
       Multi-Stream Model
               |
       +-------+-------+
       |               |
       v               v
 Equal Weights        DMC
       |               |
       |               v
       |       Optimized Weights
       |               |
       +-------+-------+
               |
               v
          HMM Decoder
               |
               v
        Recognition Results
               |
               v
        Accuracy vs SNR
```

---

## Results

### Aurora Babble Noise

The reported average recognition accuracies are:

| System | 15 dB | 10 dB | 5 dB | 0 dB | -5 dB |
|---|---:|---:|---:|---:|---:|
| ETSI-AFE MFCC-E-D-A (39) | 96.67 | 92.05 | 81.35 | 53.87 | 23.76 |
| PNCC-E-D-A (39) | 97.82 | 94.86 | 80.37 | 46.10 | 14.54 |
| PNCC-D-A (36) | 97.54 | 94.26 | 79.63 | 44.98 | 15.60 |
| PNCC-D-A (30) | 97.55 | 93.05 | 77.09 | 39.21 | 12.45 |
| MFCC-E-D-PNCC (39) | 97.78 | 92.42 | 83.45 | 60.15 | 27.86 |
| MFCC-D-PNCC (36) | 98.15 | 95.40 | 89.63 | 71.39 | 40.19 |

The MFCC-D-PNCC 36-dimensional representation provides the strongest performance in the reported experiments, particularly under highly noisy conditions.

---

## DMC Results

The DMC approach was evaluated on Aurora test sets A and B.

### Babble — Test A

| System | 15 dB | 10 dB | 5 dB | 0 dB |
|---|---:|---:|---:|---:|
| MFCC-E-D-A | 60.02 | 39.62 | 19.79 | 17.73 |
| DMC-MFCC-E-D-A | 71.85 | 55.02 | 30.75 | 22.54 |

### Car — Test B

| System | 15 dB | 10 dB | 5 dB | 0 dB |
|---|---:|---:|---:|---:|
| MFCC-E-D-A | 68.88 | 41.21 | 22.58 | 19.98 |
| DMC-MFCC-E-D-A | 73.33 | 54.90 | 28.47 | 20.93 |

---

## Key Findings

The experiments demonstrate that:

1. PNCC features can improve robustness under noisy conditions.
2. Combining MFCC and PNCC provides complementary acoustic information.
3. The 36-dimensional MFCC-D-PNCC representation provides a favorable trade-off between recognition accuracy and computational cost.
4. DMC-based stream weighting improves recognition performance compared with the conventional MFCC frontend.
5. Reducing the feature dimensionality from 39 to 36 can reduce computational and storage requirements while maintaining strong recognition performance.

---

## Technologies

- Python
- NumPy
- SciPy
- Librosa
- Scikit-learn
- PyTorch
- Hidden Markov Models
- HTK-compatible experimental protocol
- MFCC
- PNCC
- DMC
- Aurora

---

## Repository Structure

```text
aurora-robust-speech-recognition/
│
├── preprocessing/
├── features/
├── models/
├── dmc/
├── training/
├── evaluation/
├── experiments/
├── results/
└── notebooks/
```

---

## Reproducibility

Each experiment should specify:

- Dataset configuration
- Sampling rate
- Frame duration
- Frame shift
- Acoustic feature configuration
- Feature dimensionality
- HMM topology
- Number of Gaussian mixtures
- Training protocol
- SNR condition
- Recognition metric

---

## Citation

If you use this work, please cite:

Belabbas, S., & Addou, D. (2022). Weighting Schemes Based Discriminative Model Combination Technique for Robust Speech Recognition. Lecture Notes in Networks and Systems, 361, 430–438.

DOI:

https://doi.org/10.1007/978-3-030-92038-8_43

---

## Author

**Soumeya Belabbas**

PhD in Telecommunications and Information Processing

Research interests:

- Robust Speech Recognition
- Speech Processing
- Acoustic Modeling
- Pathological Speech
- Speech Enhancement
- MFCC
- PNCC
- Deep Learning
- Distributed Speech Recognition
