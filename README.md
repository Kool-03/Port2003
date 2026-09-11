# 📡 port2003 — LAN Session Monitor

A lightweight Python application that tracks login/logout sessions across computers on a local network using **UDP broadcast**.

One computer runs as the **Receiver** (server), while other computers run as **Senders** (clients). When a sender starts or ends a session, the receiver logs it in real time and calculates the session duration.

---

## 🎯 Features

- **Mode Selection Menu** — Choose to run as a Receiver or Sender from a simple GUI.
- **One-Click Session Toggle** — Start and end sessions with a single button press.
- **UDP Broadcast** — Automatic device discovery on the local network, no IP configuration needed.
- **Real-Time Logging** — The receiver instantly prints session events as they happen.
- **Duration Tracking** — Automatically calculates and displays how long each session lasted.

---

## 📁 Project Structure

```
port2003/
├── app.py          # Main entry point — mode selection menu
├── sender.py       # Sender (client) — broadcasts session events
├── receiver.py     # Receiver (server) — listens and logs sessions
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.6+**
- No external dependencies — uses only the Python standard library (`tkinter`, `socket`, `time`).

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/port2003.git
cd port2003
```

### Usage

Run the application on each computer:

```bash
python app.py
```

A menu window will appear. Choose one of the two modes:

| Mode | Description |
|------|-------------|
| **Receiver** | Listens on the network and logs all session activity to the console. Run this on **one** computer. |
| **Sender** | Opens a GUI to start/stop sessions. Run this on **any number** of computers. |

---

## 🖥️ How It Works

```
┌────────────┐       UDP Broadcast        ┌────────────┐
│  Sender A  │ ──── LOGIN / LOGOUT ─────▶ │            │
└────────────┘        (Port 2003)         │  Receiver  │
                                          │  (Server)  │
┌────────────┐       UDP Broadcast        │            │
│  Sender B  │ ──── LOGIN / LOGOUT ─────▶ │            │
└────────────┘        (Port 2003)         └────────────┘
```

1. The **Sender** identifies itself using the computer's hostname.
2. When the user clicks the session button, a `LOGIN:<hostname>` or `LOGOUT:<hostname>` message is broadcast over UDP on port **2003**.
3. The **Receiver** picks up the broadcast, records the login timestamp, and — on logout — calculates and prints the session duration.

### Message Protocol

| Message Format | Description |
|----------------|-------------|
| `LOGIN:<device_name>` | A device has started a session |
| `LOGOUT:<device_name>` | A device has ended a session |

---

## 📸 Screenshots

### Mode Selection Menu
> A simple window lets you choose whether this computer will be a Receiver or a Sender.

### Sender Window
> A toggle button switches between **Start Session (LOGIN)** and **End Session (LOGOUT)**. The button changes color to reflect the current state (green = inactive, red = active).

### Receiver Console
```
--- RECEIVER MODE ACTIVE ---
Listening for connections on port 2003...

[DESKTOP-ABC123] Session started.
[DESKTOP-ABC123] Session ended. Duration: 342.17 seconds.
```

---

## ⚠️ Notes

- All computers must be on the **same local network** (LAN/Wi-Fi).
- Only **one** Receiver should be running at a time.
- The Receiver runs in the **terminal/console** — keep the terminal window open.
- Session data is stored **in memory only** and is lost when the Receiver is closed.
- Port **2003** must not be blocked by a firewall. If needed, allow it:
  - **Windows:** `netsh advfirewall firewall add rule name="port2003" dir=in action=allow protocol=UDP localport=2003`
  - **Linux/macOS:** `sudo ufw allow 2003/udp`

---

## 🛠️ Configuration

The broadcast port can be changed by editing the `SERVER_PORT` variable in both [`sender.py`](sender.py) and [`receiver.py`](receiver.py):

```python
SERVER_PORT = 2003  # Change to any available port
```

> **Important:** The port must match in both files.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.
