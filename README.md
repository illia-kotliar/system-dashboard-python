# System Dashboard

A stylish, minimalist TUI dashboard for monitoring your PC's system components in real time.

**Built exclusively for Linux.**

## Features

The dashboard displays:

- **CPU status** — load, temperature
- **RAM status** — usage percentage, used space (GB), total capacity
- **GPUʼ status** — discrete NVIDIA and integrated Intel graphics, shown together or separately depending on available hardware (load, temperature, used VRAM, total VRAM)

## Supported hardware

**CPU:** any processor for which `psutil`/`lm-sensors` can find a temperature sensor (Intel `coretemp`, AMD `k10temp`/`zenpower`, and a few other common variants).

**GPU:** NVIDIA only (via `nvidia-smi`) and integrated Intel graphics. AMD discrete GPUs are not currently supported.

**RAM:** any RAM works, though temperature sensor availability isn't guaranteed on all models.

## Known limitations

- No support for AMD GPUs (no hardware available for testing)
- Possible bugs — the dashboard was built by a single person and hasn't undergone wide-scale testing

## Screenshots

**Dashborad Classic preview in terminal:**

Dashboard with NVIDIA GPU:

![Dashboard with NVIDIA GPU](preview_screenshots/DashboradClassic/dashboard_GPU.png)

Dashboard with Intel iGPU:

![Dashboard with Intel iGPU](preview_screenshots/DashboradClassic/dashboard_IGPU.png)

Dashboard with NVIDIA GPU + Intel iGPU:

![Dashboard with NVIDIA GPU and Intel iGPU](preview_screenshots/DashboradClassic/dashboard_GPU_IGPU.png)

Dashboard if NVIDIA GPU and Intel iGPU are not found by the program:

![Dashboard if NVIDIA GPU and Intel iGPU are not found by the program](preview_screenshots/DashboradClassic/dashboard_without_GPU_and_IGPU.png)

**Dashborad with Rich Panels preview in terminal:**

Dashboard with NVIDIA GPU:

![Dashboard with NVIDIA GPU](preview_screenshots/DashboardPanels/dashboard_GPU_Panels.png)

Dashboard with Intel iGPU:

![Dashboard with Intel iGPU](preview_screenshots/DashboardPanels/dashboard_IGPU_Panels.png)

Dashboard with NVIDIA GPU + Intel iGPU:

![Dashboard with NVIDIA GPU and Intel iGPU](preview_screenshots/DashboardPanels/dashboard_GPU_IGPU_Panels.png)

Dashboard if NVIDIA GPU and Intel iGPU are not found by the program:

![Dashboard if NVIDIA GPU and Intel iGPU are not found by the program](preview_screenshots/DashboardPanels/dashboard_without_GPU_and_IGPU_Panels.png)

## Running

1. Open a terminal in the dashboard's project folder
2. Run:

\`\`\`bash
python3 Main.py
\`\`\`

## Requirements

- Python 3.x
- `psutil`
- `rich`
- For NVIDIA GPU support: NVIDIA drivers installed (`nvidia-smi` must be available in PATH)