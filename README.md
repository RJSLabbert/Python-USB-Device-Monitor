# USB Device Monitor 🔌🐍

Real-time USB connect/disconnect monitoring in the terminal with colour-coded output.

[![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python&logoColor=white)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)](https://pypi.org/project/usb-monitor)
[![usbmonitor](https://img.shields.io/badge/usbmonitor-cross--platform-orange)](https://pypi.org/project/usb-monitor)


---

## 🛠️ Why I built this

A practical utility I needed for monitoring USB events without a GUI. I wanted something lightweight that runs in the terminal and tells me exactly when a device connects or disconnects nothing more, nothing less. Simple, clean, gets the job done.

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
Connected: /dev/bus/usb/001/003
Disconnected: /dev/bus/usb/001/003
```

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `usb-monitor` | Cross-platform USB event detection (WMI on Windows, pyudev on Linux, I/O Registry on macOS) |
| `colorama` | Cross-platform ANSI colour output |

---

## 👤 Author

**RJS Labbert**

* GitHub: [@RJSLabbert](https://github.com/RJSLabbert)
* Blog: [rocksolidcode.co.za](https://rocksolidcode.co.za)
