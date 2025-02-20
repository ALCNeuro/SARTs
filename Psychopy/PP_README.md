# SART (Sustained Attention to Response Task) in PsychoPy

## Overview
This file contains a PsychoPy implementation of the **Sustained Attention to Response Task (SART)**, developed using the **PsychoPy Builder** interface. The task is designed to measure sustained attention and response inhibition.

## Experiment Description
The SART is a go/no-go task in which participants are required to respond to frequently presented stimuli while withholding responses to infrequent targets. The experiment typically measures reaction time, accuracy, and lapses in attention.

### Task Flow
1. **Instruction Screen**: The experiment begins with a screen displaying instructions to the participant.
2. **Stimulus Presentation**: Single digits (0–9) are presented in sequence.
3. **Response Collection**: Participants must press a key in response to every digit *except* a designated target number. (3)
4. **Inter-Trial Interval**: A brief pause between trials.
5. **Block Completion**: Data is recorded at the end of each block.
6. **End of Experiment**: A message appears indicating the task is complete.

## Requirements
### Software
- **PsychoPy (v2023.2.3 or later)**
- Python 3.x
- Dependencies listed in `requirements.txt` (if applicable)

### Installation
Ensure you have PsychoPy (v2023.2.3) installed.

## How to Run the Experiment
### Using the PsychoPy Application
1. Open **PsychoPy**.
2. Load `SART_ALC_lastrun.py`.
3. Click **Run** to start the experiment.

## Data Output
- Participant responses, reaction times, and errors are recorded.
- Data is saved automatically in a `.csv` or `.psydat` format inside the `data/` directory.

## Customization
- Modify parameters such as stimulus duration, response keys, and inter-trial intervals directly in PsychoPy’s **Builder** or by editing `SART_ALC_lastrun.py`.
- Adjust block length or number of trials in the experiment settings.

---
This README provides a concise guide to running and modifying the SART experiment. Let me know if you'd like any additional details!
