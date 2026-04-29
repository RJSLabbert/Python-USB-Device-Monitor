from colorama import init, Fore, Style
from usbmonitor import USBMonitor

init(autoreset=True)
# 1. Define what happens when a device is plugged in
def on_connect(device_id, device_info):
    print(f"{Fore.GREEN}Connected: {device_id}")
    # You can access detailed info, e.g., device_info.get(ID_MODEL)

# 2. Define what happens on device plugged out
def on_disconnect(device_id, device_info):
    print(f"{Fore.RED}Disconnected: {device_id}")

# 3. Initialize and start monitoring
# The monitor runs in a separate thread (daemon)
monitor = USBMonitor()
monitor.start_monitoring(on_connect=on_connect, on_disconnect=on_disconnect)

# 4. Keep the main thread alive, otherwise the script will exit
try:
    input("Monitoring USB devices. \nConnect or disconnect devices to any USB port on the system.\n(Press Enter to close the program).\nStatus:\n")
finally:
    # 5. Stop the monitor cleanly
    monitor.stop_monitoring()
