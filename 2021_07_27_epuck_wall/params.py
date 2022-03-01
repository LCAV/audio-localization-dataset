global_params = {
    "duration": 17,  # seconds
    "source_type": "buzzer-onboard",
    "fs_soundcard": 44100,  # Hz
    "n_meas_mics": 1,  # number of measurement mics
}

MOTORS = "sweep_and_move"

params_list = []
for i in range(30): # 1.6 per centimeter
    params_list += [
        {
            "motors": MOTORS,
            "source": None,
            "distance": round(60-i*1.6, 1)
        }
    ]
