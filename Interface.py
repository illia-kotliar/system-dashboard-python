from rich.console import Group

from GPU_NVIDIA_checker_FUNCTION import nvidiasmicheck
from IGPU_intel_finder_FUNCTION import inteligpufind


def interfaceload(dict):
    # Intel IGPU info
    is_intel = inteligpufind()
    # NVIDIA GPU info
    is_nvidia = nvidiasmicheck()

    # Memory info
    RAM_temp_line = None
    if dict["memory"]["temp"]["1"] != "N/A":
        RAM_temp_line = (
            f"Memory temperature: [bold cyan]{dict['memory']['temp']['1']}°C"
        )

    # If NVIDIA and Intel GPUs are found
    if (
        is_nvidia != ["0", "0", "0", "0"]
        and is_intel
        and is_intel.startswith("is_intel")
    ):
        text = [
            f"CPU Usage: [bold cyan]{dict['cpu']['percent']}[/]%",
            f"CPU Temperature: [bold cyan]{dict['cpu']['temp']}[/]°C",
            "",
            f"Memory: [bold cyan]{dict['memory']['percent']}[/]% (used: [bold cyan]{dict['memory']['used']}[/]Gb [bold white]/[/] total: [bold cyan]{dict['memory']['total']}[/]Gb)",
        ]
        if RAM_temp_line:
            text.append(RAM_temp_line)

        text += [
            "",
            f"Gpu:[bold cyan]{dict['gpu']['name']}[/]",
            f"Gpu usage: [bold cyan]{dict['gpu']['percent']}[/]%",
            f"Gpu Temperature: [bold cyan]{dict['gpu']['temp']}[/]°C",
            f"Gpu VRAM: used:[bold cyan]{dict['gpu']['vram']['used']}[/]Gb / total:[bold cyan]{dict['gpu']['vram']['total']}[/]Gb",
            "",
            f"Gpu1:[bold cyan]{dict['igpu']['name']}",
            f"Gpu1 usage: [bold cyan]{dict['igpu']['percent']}[/]%",
            f"Gpu1 Temperature: [bold cyan]{dict['igpu']['temp']}[/]°C",
        ]

        return Group(*text)

    # If only Intel IGPU
    elif is_intel and is_intel.startswith("is_intel"):
        text = [
            f"CPU Usage: [bold cyan]{dict['cpu']['percent']}[/]%",
            f"CPU Temperature: [bold cyan]{dict['cpu']['temp']}[/]°C",
            "",
            f"Memory: [bold cyan]{dict['memory']['percent']}[/]% (used: [bold cyan]{dict['memory']['used']}[/]Gb [bold white]/[/] total: [bold cyan]{dict['memory']['total']}[/]Gb)",
        ]
        if RAM_temp_line:
            text.append(RAM_temp_line)
        text += [
            "",
            f"IGpu:[bold cyan]{dict['igpu']['name']}[/]",
            f"IGpu usage: [bold cyan]{dict['igpu']['percent']}[/]%",
            f"IGpu Temperature: [bold cyan]{dict['igpu']['temp']}[/]°C",
        ]

        return Group(*text)

    # If only NVIDIA GPU
    elif is_nvidia != ["0", "0", "0", "0"]:
        text = [
            f"CPU Usage: [bold cyan]{dict['cpu']['percent']}[/]%",
            f"CPU Temperature: [bold cyan]{dict['cpu']['temp']}[/]°C",
            "",
            f"Memory: [bold cyan]{dict['memory']['percent']}[/]% (used: [bold cyan]{dict['memory']['used']}[/]Gb [bold white]/[/] total: [bold cyan]{dict['memory']['total']}[/]Gb)",
        ]
        if RAM_temp_line:
            text.append(RAM_temp_line)
        text += [
            "",
            f"Gpu:[bold cyan]{dict['gpu']['name']}[/]",
            f"Gpu usage: [bold cyan]{dict['gpu']['percent']}[/]%",
            f"Gpu Temperature: [bold cyan]{dict['gpu']['temp']}[/]°C",
            f"Gpu VRAM: used:[bold cyan]{dict['gpu']['vram']['used']}[/]Gb / total:[bold cyan]{dict['gpu']['vram']['total']}[/]Gb",
        ]

        return Group(*text)

    else:
        text = [
            f"CPU Usage: [bold cyan]{dict['cpu']['percent']}[/]%",
            f"CPU Temperature: [bold cyan]{dict['cpu']['temp']}[/]°C",
            "",
            f"Memory: [bold cyan]{dict['memory']['percent']}[/]% (used: [bold cyan]{dict['memory']['used']}[/]Gb [bold white]/[/] total: [bold cyan]{dict['memory']['total']}[/]Gb)",
        ]
        if RAM_temp_line:
            text.append(RAM_temp_line)
        return Group(*text)
