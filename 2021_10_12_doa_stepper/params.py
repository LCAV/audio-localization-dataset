global_params = {
    "duration": 27,  # seconds, will be overwritten
    "source_type": "soundcard",
    "fs_soundcard": 44100,  # Hz
    "n_meas_mics": 1,  # number of measurement mics
}

source_params = {
    'min_dB': -30,
    'max_dB': 10
}


MOTORS = "all45000"
WINDOW_TYPE = 2  # corresponds to flattop
SOURCE = "mono3000" 
BIN_SELECTION = 3

params_list = [
    {"window_type": 2, "distance": 300, "motors": 0, "source": SOURCE, "bin_selection": BIN_SELECTION},
    {"window_type": 2, "distance": -300, "motors": MOTORS, "source": SOURCE, "bin_selection": BIN_SELECTION},
    {"window_type": 2, "distance": 15, "degree": 360, "motors": 0, "source": SOURCE, "bin_selection": BIN_SELECTION},
    {"window_type": 2, "distance": 15, "degree": -360, "motors": MOTORS, "source": SOURCE, "bin_selection": BIN_SELECTION},
]
