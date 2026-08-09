import os


def inteligpufind():
    drm_path = "/sys/class/drm"

    if not os.path.exists(drm_path):
        return None

    for item in os.listdir(drm_path):
        if item.startswith("card") and item[4:].isdigit():
            vendor_path = os.path.join(drm_path, item, "device/vendor")
            if os.path.exists(vendor_path):
                try:
                    with open(vendor_path, "r") as f:
                        if f.read().strip() == "0x8086":
                            Done = f"is_intel({item})"
                            return Done
                except OSError:
                    continue
    return None
