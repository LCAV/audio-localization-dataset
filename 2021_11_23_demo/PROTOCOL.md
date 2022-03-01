# First working demo exerpiments

__Time__: Tuesday 23.11.2021, afternoon

__Recorded__ __by__: Adrien, Frederike

__Place__: BC325

## Description

First live demo experiments, including the ones used for public defense.

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
- Frederike's laptop

### Protocol

- first success: 14:57 (+1) avoid wall once, false positive, avoid wall, land
- hover1: 15:28 (+1') avoid wall once, avoid other thing too, bump slightly into wall, false positive, avoid, false positive, bump, land
- hover2+3: 2:where Adrian came in. Nicely avoided first wall, then false positive.
- hover4+5: 4: fail, then ok: but not the metal shield. 
- hover6: nicely avoided wall once, but drifted a lot. Avoided for a second time even! Changed velocity to 7cm/s from here on
- hover7: did a false positive very early. 
- hover8: best one so far! Avoids wall 3 times in a row
- hover9: first one with new wall, bumps into wall a lot
- hover10: avoids wall way too early  (false positive)
- hover11: first okay one with new wall, but touched wall slightly
- hover12: reduce the velocity back to 5cm/s, works very well

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

Use `ros2 launch wall_approach_fslice.launch`

### Data
<!--
Explain folder naming etc.
-->

manual naming, since all parameters same throughout experiment.

### Observations
<!--
Anything unusual that happened during the experiments, such as
- Background noise
- Connection problems, low data rates, etc. 
- Hardware (battery failures, broken parts, etc)
-->
