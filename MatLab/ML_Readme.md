# SART (Sustained Attention to Response Task) in MATLAB

## Overview
This file contains MATLAB scripts for implementing the **Sustained Attention to Response Task (SART)**. The task is designed to measure sustained attention and response inhibition, and these scripts have been adapted for the **SLHIP project**.

These scripts have been adapted from the one used for the SART task published in: 
https://www.nature.com/articles/s41467-021-23890-7

## Experiment Description
The SART is a go/no-go task where participants respond to frequently presented stimuli while withholding responses to infrequent targets. The task measures reaction times, accuracy, and attentional lapses.

### Task Flow
1. **Training Phase** (`display_SART_training_SLHIP_v1.m`)
   - Participants undergo a training session to familiarize themselves with the task.
   
2. **Main Task Execution** (`main_SART_SLHIP_v1.m`)
   - Initializes the MATLAB environment and manages task execution.
   - Calls relevant scripts for displaying stimuli, collecting responses, and handling trials.

3. **Stimulus Presentation** (`display_SART_SLHIP_v1.m`)
   - Controls the randomization and display of digit sequences.
   - Ensures target digits appear at randomized but controlled positions.
   
4. **Probe Questions** (`probe_SART_SLHIP_v1.m`)
   - Introduces periodic probes to assess subjective states (e.g., mind-wandering, focus level).
   - Uses Psychtoolbox functions to manage visual and auditory cues.

## Requirements
### Software
- **MATLAB (R2018a or later)**
- **Psychtoolbox** (for stimulus presentation and response collection)

### Installation
1. Install MATLAB if not already installed.
2. Install **Psychtoolbox** 

### Set-Up
- **Brainvision EEG equipment**
- **Eyelink Eye Tracker**
If you are using a different type of EEG, eye tracker, or you just want the behaviour data, you will have to modify the script accordingly. 

## How to Run the Experiment
### Running in MATLAB
1. Ensure all scripts are in the same working directory.
2. Open MATLAB and set the root folder by running:
   ```matlab
   cd('path_to_scripts')
   ```
3. Start the experiment by executing:
   ```matlab
   main_SART_SLHIP_v1
   ```

## Data Output
- The experiment records participant responses, reaction times, and errors.
- Data is saved automatically in `.mat` or `.csv` format for further analysis.

## Customization
- **Modify stimulus timing and target frequency** in `display_SART_SLHIP_v1.m`.
- **Adjust the number of trials or block structure** in `main_SART_SLHIP_v1.m`.
- **Customize probe questions** in `probe_SART_SLHIP_v1.m`.

## License
This project is licensed under the **MIT License**.

## Citation
If you use this task in your research, please cite:
> Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) *PsychoPy2: Experiments in behavior made easy*. Behav Res 51: 195. [https://doi.org/10.3758/s13428-018-01193-y](https://doi.org/10.3758/s13428-018-01193-y)

---
This README provides a concise guide to running and modifying the MATLAB-based SART experiment. Let me know if you'd like any additional details!

