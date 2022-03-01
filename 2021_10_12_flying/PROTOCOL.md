# Wall approaching experiments

__Time__: Tuesday 12.10.2021, morning __and__ 28.10.2021, upstairs in BC325

__Recorded by__: Adrien, Frederike

__Place__: INR019

## Description

Flying experiments with new firmware (fixed mic cross-talk)

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

- hardware version3 (integrated buzzer)
- firmware version0.10 for audio_deck and version0.6 for crazyflie
- drone 8 (newly ordered)
- LCAV Thinkpad

### Protocol

experiments downstairs (12.10)
flow deck underestimates distance constantly.
-  first experiment (0:57) fail
-  1 (1:05): ok, doesn't hit
-  2 (0:46): ok, doesn't hit wall
...
-  6 (1:49, relevant up to 0:48): ok

new experiment series upstairs (28.10.2021), starting at 1m:
-  new3: full battery
-  new4: full battery
-  new6: same battery (start at 4)
starting at 1.20m:
-  new7: same battery (start at 3.99)
-  new8: did not film from side, same battery (start at 3.9)
-  new10: full battery

Realized after analysis: 
- new3: very good
- new4: did not change bin_sel to 5
- new6: ok, but too fast (bumped into wall after half)
- new7: did not change bin_sel to 5
- new8: messed up flow deck, very bad results because freqs messed up
- new10: bad results for some reason
- new12: bad results for some reason

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
measurement_pipeline with measure_wall()

### Data
<!--
Explain folder naming etc. 
-->

as always

### Observations
<!--
Anything unusual that happened during the experiments, such as
- Background noise
- Connection problems, low data rates, etc. 
- Hardware (battery failures, broken parts, etc)
-->
