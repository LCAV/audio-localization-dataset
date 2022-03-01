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


MOTORS = "hover" 
SOURCE = "mono3000"
WINDOW_TYPE = 2  # corresponds to flattop
BIN_SELECTION = 3

params_list = []
for i in range(3):
    params_list += [
        {"window_type": WINDOW_TYPE, "motors": MOTORS, "source": SOURCE, "bin_selection": BIN_SELECTION}
    ]
