global_params = {
    "duration": 0,  # seconds, will be overwritten
    "source_type": "buzzer-onboard",
    "fs_soundcard": 44100,  # Hz
    "n_meas_mics": 1,  # number of measurement mics
}

MOTORS = "all45000"
SOURCE = "sweep_new"

DEGREE_LIST = [None]
DISTANCE_LIST = range(50)
SOURCE_LIST = [SOURCE]
MOTORS_LIST = [0, MOTORS]
WINDOW_TYPE = 2  # corresponds to flattop

params_list = []
for d in DISTANCE_LIST:
    for bin_selection in [5, 6]:
        for motors in MOTORS_LIST:
            params_list += [
                {
                    "distance": d,
                    "motors": motors,
                    "bin_selection": bin_selection,
                    "source": SOURCE,
                    "window_type": WINDOW_TYPE,
                }
            ]
