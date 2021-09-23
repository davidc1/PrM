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
