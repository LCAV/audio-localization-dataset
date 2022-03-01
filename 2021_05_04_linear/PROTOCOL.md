# Linear wall approach experiments

__Time__: Tuesday 04.05.2021, afternoon

__Recorded by__: Adrien Hoffet, Frederike Duembgen

__Place__: BC325

## Description

###  Hardware
<!--
Checklist: 
- Drone number
- Speaker type
- Microphone type
- Motors for linear/rotational movement
- Computer
- Drone type, decks used
- Soundcard
-->
- hardware version 3 (integrated buzzer)
- firmware version0.6 for both audio_deck and crazyflie
- added kalmanFilter requirement
- drone 8 (newly ordered)
- flag IIR_FILTERING activated
- N_SPI_PER_NOTE: 1
- LCAV Thinkpad

### Protocol

- slow1: +45 (front)
- slow2: -45 (back)
- slow3: 90 (middle)
- slow4: -30 (back)
- slow5: 30 (front)
- fast1: -45 (back)
- fast2: +45 (front)
- fast3: 90 (middle)
- fast4: 30 (front)
- fast5: -30 (back)

### Parameters
<!--
Checklist: 
If available:
- parameters file location
- soundcard settings
Otherwise: 
- Sampling rate
- Motor thrust value 
- Audio files used
- Scripts used
- Other parameters used
-->
measurement_pipeline with measure_wall_flying()

### Data
<!--
Explain folder naming etc. 
-->
nosnr corresponds to snr=3
otherwise as always

### Observations
<!--
Anything unusual that happened during the experiments, such as
- Background noise
- Connection problems, low data rates, etc. 
- Hardware (battery failures, broken parts, etc)
-->
