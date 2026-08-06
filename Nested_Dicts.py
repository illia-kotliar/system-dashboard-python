import psutil

from CPU_temp_check_FUNCTION import cpuinfo
from GPU_NVIDIA_checker_FUNCTION import nvidiasmicheck


def RAMtempcheck():
    current_sensors = psutil.sensors_temperatures()
    sensors_list = [
        "jc42",
        "spd5118",
    ]  # You can past it your RAM temperature sensor name

    for sensor in sensors_list:
        if sensor in current_sensors:
            return sensor
    return None


def systemstats():
    # CPU info
    listcpu = cpuinfo()

    # Memory info
    memory = psutil.virtual_memory()
    RAMtempsensor = RAMtempcheck()

    if RAMtempsensor:
        ram_temp_sensor = psutil.sensors_temperatures()[RAMtempsensor]
        ram_temp_line = {
            "1": ram_temp_sensor[0].current,
            "2": ram_temp_sensor[1].current,
        }
    else:
        ram_temp_line = {"1": "N/A", "2": "N/A"}

    # NVIDIA GPU info
    listnvidia = nvidiasmicheck()
    gpu_name = "NVIDIA"

    # Intel IGPU info
    igpu_name = "Intel"

    # Making Dicts
    return {
        "cpu": {"percent": listcpu[0], "temp": listcpu[1]},
        "memory": {
            "percent": memory.percent,
            "used": round(memory.used / (1024**3), 1),
            "total": round(memory.total / (1024**3), 1),
            "temp": ram_temp_line,
        },
        "gpu": {
            "name": gpu_name,
            "temp": listnvidia[0],
            "percent": listnvidia[1],
            "vram": {
                "used": round(float(listnvidia[2]) / 1024, 1),
                "total": round(float(listnvidia[3]) / 1024, 1),
            },
        },
        "igpu": {"name": igpu_name, "temp": listcpu[1], "percent": "N/A"},
    }
