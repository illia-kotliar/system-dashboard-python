from GPU_NVIDIA_checker_FUNCTION import nvidiasmicheck
from IGPU_intel_finder_FUNCTION import inteligpufind
from rich.console import Group
from rich.panel import Panel


def interfaceload(dict):
    # Intel IGPU info
    is_intel = inteligpufind()
    # NVIDIA GPU info
    is_nvidia = nvidiasmicheck()

    # Memory info
    RAM_temp_line = None
    if dict["memory"]["temp"]["1"] != "N/A":
        RAM_temp_line = (
            f"Temperature: [bold cyan]{dict['memory']['temp']['1']}°C"
        )



    # Dict blocks
    block = {
        "cpu": Group(
            f"Usage: [bold cyan]{dict['cpu']['percent']}[/]%",
            f"Temperature: [bold cyan]{dict['cpu']['temp']}[/]°C"
        ),
        "gpu": Group(
            f"Brand:[bold cyan]{dict['gpu']['name']}[/]",
            f"Usage: [bold cyan]{dict['gpu']['percent']}[/]%",
            f"Temperature: [bold cyan]{dict['gpu']['temp']}[/]°C",
            f"VRAM: used:[bold cyan]{dict['gpu']['vram']['used']}[/]Gb / total:[bold cyan]{dict['gpu']['vram']['total']}[/]Gb"
        ),
        "igpu": Group(
            f"Brand:[bold cyan]{dict['igpu']['name']}[/]",
            f"Usage: [bold cyan]{dict['igpu']['percent']}[/]%",
            f"Temperature: [bold cyan]{dict['igpu']['temp']}[/]°C"           
        )
    }



    # Panels
    cpu = Panel(
        block['cpu'],
        title="[bold cyan]CPU[/]",
        title_align="left",
        expand=False
    )
    gpu = Panel(
        block['gpu'],
        title="[bold cyan]GPU[/]",
        title_align="left",
        expand=False
    )
    igpu = Panel(
        block['igpu'],
        title="[bold cyan]IGPU[/]",
        title_align="left",
        expand=False
    )



    # RAM Panel
    mem = [f"Usage: [bold cyan]{dict['memory']['percent']}[/]% (used: [bold cyan]{dict['memory']['used']}[/]Gb [bold white]/[/] total: [bold cyan]{dict['memory']['total']}[/]Gb)"]

    if RAM_temp_line:
                mem.append(RAM_temp_line)

    ram = Panel(
        Group(*mem),
        title="[bold cyan]RAM[/]",
        title_align="left",
        expand=False
    )




    # If NVIDIA and Intel GPUs are found
    if (
        is_nvidia != ["0", "0", "0", "0"]
        and is_intel
        and is_intel.startswith("is_intel")
    ):

        return Group(cpu, ram, gpu, igpu)


    # If only Intel IGPU
    elif is_intel and is_intel.startswith("is_intel"):

        return Group(cpu, ram, igpu)


    # If only NVIDIA GPU
    elif is_nvidia != ["0", "0", "0", "0"]:

        return Group(cpu, ram, gpu)


    # If GPU and IGPU not found
    else:

        return Group(cpu, ram)