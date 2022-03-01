global_params = {
    "duration": 30,  # seconds, will be overwritten
    "source_type": "buzzer-onboard",
    "fs_soundcard": 44100,  # Hz
    "n_meas_mics": 0,  # number of measurement mics # used to be 1
}

MOTORS = "linear_buzzer_cont"
SOURCE = None
DISTANCE = None
WINDOW_TYPE = 2  # corresponds to flattop
BIN_SELECTION = 5

params_list = []
for i in range(10, 20):
    params_list += [
        {
            "distance": DISTANCE,
            "motors": MOTORS,
            "bin_selection": BIN_SELECTION,
            "source": SOURCE,
            "window_type": WINDOW_TYPE,
            "appendix": f"_new{i}",
        }
    ]
