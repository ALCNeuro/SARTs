# SART (Sustained Attention to Response Task) - Repository Overview

## Overview
This repository contains two implementations of the **Sustained Attention to Response Task (SART)**, a widely used cognitive task designed to measure sustained attention and response inhibition. The task is available in both **MATLAB** and **PsychoPy** formats.

## Repository Structure
This repository is organized into two main directories:

### 1. `MatLab/`
Contains MATLAB scripts for running the SART experiment using **Psychtoolbox**.
- **Key scripts:**
  - `main_SART_SLHIP_v1.m`: Initializes and runs the full experiment.
  - `display_SART_SLHIP_v1.m`: Manages stimulus presentation.
  - `display_SART_training_SLHIP_v1.m`: Runs a training session before the main experiment.
  - `probe_SART_SLHIP_v1.m`: Handles periodic probe questions to assess participant state.

**Requirements:** MATLAB (R2018a or later) with **Psychtoolbox** installed.

### 2. `Psychopy/`
Contains the PsychoPy implementation of the SART, developed using the **PsychoPy Builder**.
- **Key script:**
  - `SART_ALC_lastrun.py`: The PsychoPy-generated script that runs the experiment.
  - `SART_ALC.psyexp`: The PsychoPy Builder file that will allow you to open the SART in the builder and easily do the modifications.

**Requirements:** Python 3.x with **PsychoPy (v2023.2.3 or later)**.

## Running the Experiment
- **For MATLAB:** Navigate to the `MatLab/` directory and run:
  ```matlab
  main_SART_SLHIP_v1
  ```
- **For PsychoPy:** Navigate to the `Psychopy/` directory and either:
  - Open the script in PsychoPy and click "Run"

## Data Output
- **MATLAB:** Saves responses and reaction times in `.mat` files.
- **PsychoPy:** Saves responses in `.csv` format inside the `data/` folder.

---
This README serves as the main landing page, guiding users to the appropriate SART implementation based on their preferred software environment. Refer to the specific `README` files inside each folder for further details.
