# Audio localization dataset

Datasets for acoustic echolocation and sound source localization on Crazyflie drone and e-puck2 robot.

## Overview

This repository is part of the experimental framework described in the [paper](https://doi.org/10.1109/LRA.2022.3194669):
```
F. Dümbgen, A. Hoffet, M. Kolundžija, A. Scholefield, and M. Vetterli, "Blind as a bat: audible 
echolocation on small robots", IEEE Robotics and Automation Letters (Early Access), 2022.
```

The framework includes all components listed below. The components are kept modular so that researchers may focus only on what's relevant to them. For instance, to recreate the audio extension deck and perform more research on audio-based navigation on drones, only repository 2. is necessary; to run the audio-based algorithms in ROS but for a different robot, only repository 1. is enough as a starting point.      

1. [ROS processing pipeline](https://github.com/LCAV/audioROS) for processing audio for tasks such as obstacle detection and sound source localization. 
2. [Audio deck firmware](https://github.com/LCAV/crazyflie-audio), which also includes the PCB files for reproducing the audio deck. 
3. [Public datasets](https://github.com/LCAV/audio-localization-dataset) (**this repository**), for audio-based localization on the e-puck2 robot and the Crazyflie drone. 
4. [Crazyflie firmware](https://github.com/LCAV/crazyflie-firmware) (fork from official vendor firmware), with an added [audio deck driver](https://github.com/LCAV/crazyflie-firmware/blob/master/src/deck/drivers/src/audio_deck.c).
5. [Gtsam extension](https://github.com/duembgen/gtsam) for performing factor-graph inference using the echolocation measurements. 

## Dataset description

Locations: rooms in computer science buildings at EPFL.

- `INR018`: carpeted sound lab of ca. 4 by 4 meters, curtains on walls, whiteboards used as reflectors.
- `BC325`: office space of ca. 7 by 9 meters, glass walls and textured, painted concrete walls used as reflectors.

Details on the specific experiments can be found in the respective `PROTOCOL.md` files, placed within each experiment folder. 

## Echolocation experiments

Experiments corresponding to the IROS paper, and Chapter 6 of the thesis.

- `2021_07_08_stepper_fast`: drone measure interference function on stepper motor, BC325.
- `2021_07_27_epuck_wall`: epuck2 measures interference function, BC325.
- `2021_10_12_flying`: drone flies towards wall, in INR018 and BC325.
- `2021_11_23_demo`: drone avoids glass or normal wall + moving metal shield, BC325.
- `2022_01_27_demo`: drone avoids opposing whiteboards, in INR018.
- `2021_05_04_linear`: drone approaches wall while playing single frequency.

## DOA experiments

Experiments corresponding to the methods described in Chapter 5 of the thesis.

- `2021_10_12_doa_flying`: drone hovers in place and locates external fixed sound source, INR018.
- `2021_10_12_doa_stepper`: drone translates and rotates on stepper motor with external fixed sound source, INR018.

## References

Please refer to the below publications for more information. 

[1] [RA-L paper](https://doi.org/10.1109/LRA.2022.3194669) (main reference)
```
F. Dümbgen, A. Hoffet, M. Kolundžija, A. Scholefield, and M. Vetterli, "Blind as a bat: audible 
echolocation on small robots", IEEE Robotics and Automation Letters (Early Access), 2022. 
```

[2] [Ph.D. dissertation](https://infoscience.epfl.ch/record/290057) (including additional methods and experimental analysis):  
```
F. Dümbgen, "Blind as a bat: spatial perception without sight", Ph.D. disseration, 
École Polytechnique Fédérale de Lausanne, 2021.
```

