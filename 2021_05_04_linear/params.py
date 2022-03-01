global_params = {
    "duration": 15,
    "source_type": "buzzer-onboard",
    "fs_soundcard": 44100,  # Hz
    "n_meas_mics": 0,  # number of measurement mics
}

# MOTORS = "linear_3000"
MOTORS = "linear_3000_fast"
SOURCE = None  # "mono3000"

DISTANCE_LIST = [None]
DEGREE_LIST = [None]
SOURCE_LIST = [SOURCE]
MOTORS_LIST = [MOTORS]
WINDOW_TYPE = 2  # corresponds to flattop

params_list = [
    {
        "motors": MOTORS,
        "bin_selection": 3,
        "source": None,  # integrated in pipeline
        "min_freq": 2000,
        "max_freq": 6000,
        "window_type": WINDOW_TYPE,
    },
]
