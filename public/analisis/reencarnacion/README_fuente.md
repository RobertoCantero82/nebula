# CORT Intermission Time — Data and Analysis Code

This repository contains the open data and analysis code accompanying:

Sadeghi, S., Pehlivanova, M., & Cozzolino, P. J. (2026). *A large-scale analysis of temporal patterns in children's purported past-life memories: Shorter intervals following unexpected deaths.* **Psychology of Consciousness: Theory, Research, and Practice.** https://doi.org/10.1037/cns0000493

## Files

- `CORT_IT_open_data.csv` — de-identified case-level data used in the study.
- `CORT_IT_analysis.R` — R code reproducing the statistical analyses reported in the paper.
- `CORT_IT_codebook.txt` — definitions and coding information for all variables in the dataset.

The dataset contains the full sample of **2,254 cases**. Most analyses reported in the paper use the subset of cases in which the previous person was identified (`is_verified = TRUE`).

Case identifiers are anonymized sequential IDs and do not correspond to identifiers in the original research database. Missing values are represented as blank cells.
