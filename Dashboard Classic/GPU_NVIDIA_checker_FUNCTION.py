import subprocess


def nvidiasmicheck():
    try:
        nvidia_smi = subprocess.check_output(
            [
                "nvidia-smi",
                "--query-gpu=temperature.gpu,utilization.gpu,memory.used,memory.total",
                "--format=csv,noheader,nounits",
            ]
        )
        clean_nvidia_smi = nvidia_smi.decode("utf-8").strip()
        clean_text = clean_nvidia_smi.replace(" ", "")
        text = clean_text.split(",")

        return text
    except (subprocess.CalledProcessError, FileNotFoundError):
        clean_nvidia_smi = "0, 0, 0, 0"
        clean_text = clean_nvidia_smi.replace(" ", "")
        text = clean_text.split(",")

        return text
