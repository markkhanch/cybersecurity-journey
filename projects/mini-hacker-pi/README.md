# Mini Hacker Pi Project

This project documents the build of a portable “mini hacker” device based on the Raspberry Pi Zero 2 W. The goal is to provide a minimal skeleton to get started quickly and to track your progress over time.

## What is this?

A modular hand‑held tool built around a Pi Zero 2 W with a 1.3‑inch Waveshare ST7789 display and a simple joystick/button input. It’s intended for educational and legal experiments only: network monitoring within your own lab, simple utilities, games and other personal projects.

## Hardware

- **Raspberry Pi Zero 2 WH** – pre‑soldered header, quad‑core 1 GHz, Wi‑Fi & Bluetooth.
- **Waveshare 1.3 inch LCD HAT (ST7789)** – 240×240 px IPS screen communicating over SPI.
- **USB dongle breakout** – optional convenience board to expose USB ports.
- **Micro SD card (128 GB)** – optional; a 16 GB or 32 GB card is usually sufficient.

## Recommended OS

Use **Raspberry Pi OS Lite (32‑bit)**. You can flash it with Raspberry Pi Imager. It’s lightweight, has broad library support and works well on the Pi Zero 2 W.

## Quick Start

1. Flash Raspberry Pi OS Lite to a micro SD card.
2. Enable SSH by creating an empty file named `ssh` in the `/boot` partition.
3. Boot the Pi and connect via SSH.
4. Clone this repository inside `/home/pi`:
   ```sh
   git clone https://github.com/markkhanch/cybersecurity-journey.git
   cd cybersecurity-journey/projects/mini-hacker-pi
   ```
5. Install dependencies and enable SPI/I2C using the provided script:
   ```sh
   sudo ./scripts/install.sh
   ```
6. Run the shell:
   ```sh
   python3 src/shell/main.py
   ```
   You should see “Hello, Mini Hacker Pi!” on the display.

## Modules (pick what you need)

Optional modules live in `src/modules/`. Each module contains its own README and code. To enable a module, copy its folder into your working directory and import it into the shell.

- `snake/` – a simple Snake game to test the display and input.

## Controls

The default shell uses a joystick (up, down, left, right, centre press) to navigate menus. Buttons can be assigned in future modules.

## Progress

Keep a running log of your work here. Employers or collaborators can see how the project evolves.

- 2025‑10‑19 – Skeleton structure created; initial README; install script and Hello World shell.

## Ethics

This project is for learning and experimentation in controlled environments. Do not use it to access or interfere with networks or devices without permission.

## License

This project uses the MIT License (see `LICENSE` for details).