STRESS_PRESETS = {
    "COVID_Crash_2020": 0.35,
    "Dotcom_Burst_2000": 0.25,
    "Rate_Spike_2022": 0.20,
    "2008_Global_Financial_Crisis": 0.45,
    "Mild_Correction": 0.10
}

def get_stress_factor(preset_name):
    return STRESS_PRESETS.get(preset_name, 0.10)