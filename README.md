# USB Device Monitor 🔌🐍

Real-time USB connect/disconnect monitoring in the terminal with colour-coded output.

[![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python&logoColor=white)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)](https://pypi.org/project/usb-monitor)
[![usb-monitor](https://img.shields.io/badge/usbmonitor-cross--platform-orange)](https://pypi.org/project/usb-monitor)


---

## 🛠️ Why I built this

A practical tool used to monitor USB devices connected to a system. Originally built to possibly automate backups when an external drive is connected, but also useful day-to-day for checking how many devices are active and whether USB ports are working correctly.

---

## ✨ Features

* 🟢 **Connect events** — prints the device ID in green when a USB device is plugged in
* 🔴 **Disconnect events** — prints the device ID in red when a USB device is removed
* 🧵 **Background thread** — monitor runs as a daemon so the main thread stays free
* 🛑 **Clean shutdown** — press Enter to stop monitoring gracefully

---

## 🖥️ Requirements

* Python 3.7+
* Windows, Linux, or macOS

---

## 🚀 Quick Setup

1. Clone the repository:

```bash
git clone https://github.com/RJSLabbert/Python-USB-Device-Monitor.git
cd Python-USB-Device-Monitor
```

2. (Optional) Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the monitor:

```bash
python usb_monitor.py
```

---

## 📟 Example Output

```
Monitoring USB devices.
Connect or disconnect devices to any USB port on the system.
(Press Enter to close the program).
Status:
Connected: USB\VID_046D&PID_C077\1234567890
Disconnected: USB\VID_046D&PID_C077\1234567890
```

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `usb-monitor` | Cross-platform USB event detection (WMI on Windows, pyudev on Linux, I/O Registry on macOS) |
| `colorama` | Cross-platform ANSI colour output |

---

## 🔮 Future Plans

* **Config file** — define backup paths and target devices.
* **Plug and play backup** — auto-trigger backup when a specific drive connects.
* **Expanded device info** — USB speed, vendor, and model details.

---

## 👤 Author

**RJS Labbert**

* GitHub: [@RJSLabbert](https://github.com/RJSLabbert)
* Blog: [rocksolidcode.co.za](https://rocksolidcode.co.za)
