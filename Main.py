import sys
import time

from rich.console import Console
from rich.live import Live

from Interface import interfaceload
from Nested_Dicts import systemstats

console = Console(highlight=False)


def main():

    with Live(console=console, screen=True, refresh_per_second=8) as live:
        while True:
            stats = systemstats()

            interface = interfaceload(stats)

            # Draw interface
            live.update(interface)
            time.sleep(1)


# Check system compitable
if not sys.platform.startswith("linux"):
    print("Sorry, this utility was created for Linux")
    input("Press Enter for exit")
    sys.exit(1)
if __name__ == "__main__":
    main()
