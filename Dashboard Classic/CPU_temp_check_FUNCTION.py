import psutil


def tempsensorcheck():
    current_sensor = psutil.sensors_temperatures()
    Cpu_Temp_Sensors_Names = (
        "k10temp",
        "coretemp",
        "zenpower",
        "cpu_thermal",
        "cpu-thermal",
        "soc_thermal",
        "thermal_zone0",
        "acpitz",
    )
    sensor = None
    for sensor in Cpu_Temp_Sensors_Names:
        if sensor in current_sensor:
            Done = sensor
            return Done
    return "sensor not found"


def cpuinfo():
    Done = tempsensorcheck()

    if Done == "sensor not found":
        return [psutil.cpu_percent(interval=None, percpu=False), "N/A"]
    current_sensor = psutil.sensors_temperatures()
    cpu_info = [
        round(psutil.cpu_percent(interval=None, percpu=False), 1),
        round(current_sensor[Done][0].current, 1)
    ]
    return cpu_info
