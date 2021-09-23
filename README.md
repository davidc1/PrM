# PrM
Analysis for LArCADe project


# Key functions:

Core code lives in `decode_new.py`. Main function used externally is `GetWaveformsNoiseRemoval` (`GetWaveforms`) does not apply noise removal. The main goal of the code in this script is to decode the waveform from their LabView format into numpy arrays. This function returns an array of arrays. The first index points to a given event in the run (i.e. our "runs" are typically 50 LED flasher events, which each trigger corresponding to one event and one pair of anode/cathode waveforms) The second index points to the anode (0) or cathoe (1) waveform.

```
from decode_new import GetWaveformsNoiseRemoval

ev_wf_v = GetWaveformsNoiseRemoval(datafile)

A_wf = ev_wf_v[n][0]
C_wf = ev_wf_v[n][1]
```

# 2021 analysis
data: https://drive.google.com/drive/folders/1nbhTVc3ZsQZuK2fGATmih39ovANRmhsl?usp=sharing

Once repository is downloaded, start a jupyter notebook (`jupyter notebook`).
Open the notebook `WFdisplay-2021.ipynb`.

The main blocks of code in the notebook are described below:

# Waveform by waveform Plotting

This code goes through all runs and stores average waveforms and amplitudes over each run in the containers below. The cell outputs plots of avg waveforms for each run.

```
# time-step
dt = 0.0005

# where to compute baseline
BaselineRange1 = [0.10,0.15]
BaselineRange2 = [0.18,0.20]

# where to integrate charge
IntegrationRange = [0.2,0.6]

# below, one entry per Run
# average waveforms for anode and cathode
ALL_AVG_C_WF_V = []
ALL_AVG_A_WF_V = []
# max/min amplitude at anode and cathode
AVG_A_MAX_V = []
AVG_C_MIN_V = []
# voltage
VOLTAGE_V = []
```
![exampleavg](https://user-images.githubusercontent.com/5184059/134537055-d5abc2c4-93c4-46e8-8fb6-d15cfac40c7c.png)

# Timing analysis 

This block of code identifies the crossings for the Cathode, CG, AG, and Anode.

Important blocks of code are:

Gather differential of waveforms (see `diffwf` function which specifies a time-tick offset to create derivative)

```
    waveformAR = diffwf(waveformAR)
    waveformCR = diffwf(waveformC)
```

Identify crossings by finding inflection points in waveform. Done for A and C waveforms separately. Key input is the amplitude difference needed for a crossing at 0 to trigger the identification of the crossing. This is typically a fraction of a volt but should be gauged from the waveforms. Values are hard-coded right now (0.3 and 0.2). Edit as needed. Example below:

```
if (ADC1 < -0.3 and ADC2 < -0.3):
    Ccrossing = tick
```
![exampletiming](https://user-images.githubusercontent.com/5184059/134536971-4f67a45b-7adf-4de4-ab37-3df78e07c69e.png)

# Timing results

The last cell plots the drift time and extrapolated E-field in each section of the PrM for different Runs.
