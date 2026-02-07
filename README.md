# RCP hi robi
# Intelligent Pipeline Inspection Data Alignment & Corrosion Growth Prediction — README

## Overview

This solution was developed as part of the ILI Hackathon Challenge, focused on aligning In-Line Inspection (ILI) datasets and predicting corrosion growth in pipelines. The automated approach replaces time-consuming, error-prone manual processes with a robust system for anomaly matching, growth rate calculation, and exception handling, supporting safer and more efficient pipeline operations.

---

## Problem Statement

Pipeline operators need to compare ILI data from different inspection runs to understand corrosion and defect evolution. Manual alignment is slow, inconsistent, and struggles with challenges such as odometer drift, reference changes, and anomaly evolution. This solution automates:

- Reference point alignment (e.g., girth welds, valves)
- Anomaly matching between runs
- Corrosion growth computation
- Exception and new anomaly identification

---

## Features

- Aligns two ILI datasets from the same pipeline segment (CSV/Excel)
- Matches fixed features (girth welds, valves, etc.) between runs and applies distance correction
- Pairs anomalies based on corrected distance, clock position, feature type, and dimensions
- Calculates growth rates for matched anomalies (depth, length, width)
- Flags new/missing anomalies and uncertain matches
- Outputs a matched dataset with growth calculations

**Stretch Goals (Optional):**

- Confidence scoring for each match
- Machine learning-based matching and anomaly prediction
- Interactive visualization dashboard
- Multi-run (3+) analysis support
- API integration

---

## Data Inputs

You will require the following:

- ILI Run 1 Dataset (baseline inspection)
- ILI Run 2 Dataset (subsequent inspection)
- Reference Alignment Points (key features along pipeline, e.g., girth welds, valves)
- Data Dictionary (field definitions and units)

### Data Fields (examples)

- `feature_id`: Unique anomaly ID
- `distance`: Absolute distance from pipeline start
- `odometer`, `joint_number`, `relative_position`
- `clock_position`: Circumferential location (e.g., 4:30)
- `feature_type`: Anomaly classification
- `depth_percent`, `length`, `width`, `wall_thickness`, `weld_type`

---

## Algorithmic Approach

The workflow includes:

1. **Reference Point Alignment:** Match fixed features (girth welds, etc.) to establish common zones.
2. **Distance Correction:** Adjust anomaly locations for odometer drift or instrument error.
3. **Anomaly Matching:** Pair anomalies based on proximity (distance, clock position), compatible feature types, and similarity in size.
   - Example methods: Dynamic Time Warping (DTW), Iterative Closest Point (ICP), Hungarian matching, graph matching, ensemble of multiple criteria.
4. **Growth Calculation:** For matched pairs, compute depth, length, and width changes.
5. **Exception Handling:** Flag anomalies as new, missing, or uncertain matches.
6. **Output Generation:** Create a results file listing matches and growth rates.

---

## Getting Started

### Prerequisites

- Python (recommended), or R
- Key libraries: pandas, scikit-learn, scipy, networkx, streamlit, Plotly, TensorFlow/PyTorch (if using ML enhancements)

### Setup

1. Clone/download this repository.
2. Place your ILI datasets and reference points in the data/ folder.
3. Install dependencies using `pip install -r requirements.txt`.
4. Run the solution using:

```bash
python align_and_predict.py --run1 data/ili_run1.csv --run2 data/ili_run2.csv --refs data/alignment_points.csv
```

5. Results (matched dataset with growth rates) will be saved in the results/ folder.

---

## Deliverables

- **Source Code:** Main logic for data alignment and matching
- **README:** (this file) with setup and usage instructions
- **Demo:** Optional — run `demo.py` or navigate to provided dashboard for walkthrough
- **Results File:** CSV of matched anomalies and computed growth
- **Presentation:** (Slides/recording, if part of the hackathon submission)

---

## Evaluation

Your solution will be evaluated on:

- Matching accuracy (validated against an expert-matched subset)
- Handling of edge cases and data quality issues
- Usability and clarity of outputs
- Innovation in algorithm design or stretch features
- Scalability to large datasets
- Quality of documentation

---

## Resources

- Recommended Readings: ASME B31.8S, API 1163, NACE SP0502, PHMSA 49 CFR 192/195
- Useful tools: pandas, scikit-learn, TensorFlow, Plotly

---

## Glossary

- **ILI:** In-Line Inspection tool ("smart pig")
- **Anomaly:** Any pipeline deviation (corrosion, crack, weld, etc.)
- **Clock position:** Circumferential location, e.g., 4:30 means bottom-right
- **Girth weld:** Weld joining pipe sections
- **Wall thickness:** Pipe wall thickness, critical for depth estimates

---

## Acknowledgements

Data and instructions provided are anonymized/synthetic for confidentiality, based on pipeline inspection best practices and regulations.

---

## Contact / Issues

For support or questions, open an issue in the repository or contact the development team.

---

Good luck, and remember: your solution could help prevent the next pipeline incident! [1]
