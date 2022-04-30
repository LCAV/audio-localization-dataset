# Audio localization dataset

Datasets for acoustic echolocation and sound source localization on Crazyflie drone and e-puck2 robot.

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

```
F. Dümbgen, A. Hoffet, A. Scholefield, and M. Vetterli, "Blind as a bat: 
audible echolocation on tiny robots", submitted to IEEE/RSJ International 
Conference on Intelligent Robotis and Systems, 2022.
```


```
F. Dümbgen, "Blind as a bat: spatial perception without sight", 
Ph.D. disseration, École Polytechnique Fédérale de Lausanne, 2021.
```
