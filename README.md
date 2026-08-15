# System Monitor Widget

A stylish, minimalist TUI widget for monitoring your PC's system components in real time.

**Built exclusively for Linux.**

## Features

The widget displays:

- **CPU status** — load, temperature
- **RAM status** — usage percentage, used space (GB), total capacity
- **GPU status** — discrete NVIDIA and integrated Intel graphics, shown together or separately depending on available hardware (load, temperature, used VRAM, total VRAM)

## Supported hardware

**CPU:** any processor for which `psutil`/`lm-sensors` can find a temperature sensor (Intel `coretemp`, AMD `k10temp`/`zenpower`, and a few other common variants).

**GPU:** NVIDIA only (via `nvidia-smi`) and integrated Intel graphics. AMD discrete GPUs are not currently supported.

**RAM:** any RAM works, though temperature sensor availability isn't guaranteed on all models.

## Known limitations

- No support for AMD GPUs (no hardware available for testing)
- Possible bugs — the widget was built by a single person and hasn't undergone wide-scale testing

## Screenshots

**Usage example in end_4 dotfiles:**

![Widget with NVIDIA GPU](preview_screenshots/in_use/using.png)

**Classic style preview in terminal:**

Widget with NVIDIA GPU:

![Widget with NVIDIA GPU](preview_screenshots/DashboradClassic/dashboard_GPU.png)

Widget with Intel iGPU:

![Widget with Intel iGPU](preview_screenshots/DashboradClassic/dashboard_IGPU.png)

Widget with NVIDIA GPU + Intel iGPU:

![Widget with NVIDIA GPU and Intel iGPU](preview_screenshots/DashboradClassic/dashboard_GPU_IGPU.png)

Widget if NVIDIA GPU and Intel iGPU are not found:

![Widget if NVIDIA GPU and Intel iGPU are not found](preview_screenshots/DashboradClassic/dashboard_without_GPU_and_IGPU.png)

**Rich Panels style preview in terminal:**

Widget with NVIDIA GPU:

![Widget with NVIDIA GPU](preview_screenshots/DashboardPanels/dashboard_GPU_Panels.png)

Widget with Intel iGPU:

![Widget with Intel iGPU](preview_screenshots/DashboardPanels/dashboard_IGPU_Panels.png)

Widget with NVIDIA GPU + Intel iGPU:

![Widget with NVIDIA GPU and Intel iGPU](preview_screenshots/DashboardPanels/dashboard_GPU_IGPU_Panels.png)

Widget if NVIDIA GPU and Intel iGPU are not found:

![Widget if NVIDIA GPU and Intel iGPU are not found](preview_screenshots/DashboardPanels/dashboard_without_GPU_and_IGPU_Panels.png)

## Running

1. Open a terminal in the widget's project folder
2. Run:


       python3 Main.py

## Requirements

- Python 3.x
- `psutil`
- `rich`
- For NVIDIA GPU support: NVIDIA drivers installed (`nvidia-smi` must be available in PATH)