# Battery-Notifier

A simple Python battery monitoring program that continuously checks the laptop battery level and sends Windows notifications when the battery reaches low levels.

# Features

- Monitors the battery percentage every 60 seconds.
- Detects whether the charger is connected.
- Sends a warning when the battery drops to 30% or below while running on battery.
- Sends a critical warning when the battery drops to 15% or below.
- Prevents repeated notifications while the battery remains at the same warning level.

 # Technologies Used

- Python
- "psutil" — retrieves the current battery percentage and charging status.
- "winotify" — displays Windows desktop notifications.
- "winsound" — plays Windows system sounds.
- "time" — controls the monitoring interval.

# How to Run

Run the Python file:

battery.py

The program will continuously monitor the battery and check its status every 60 seconds.

# Battery Alerts

Low Battery — 30%

When the battery is 30% or below and the charger is disconnected, the program sends a warning notification.

# Example:

«Battery Low
28% Battery Remaining!»

A warning sound is also played.

# Critical Battery — 15%

When the battery reaches 15% or below while the charger is disconnected, the program sends a stronger warning.

# Example:

«Battery Low
12% Battery Remaining!»

A different, more noticeable system sound is played for this alert.

# How It Works

The program uses:

battery = psutil.sensors_battery()

to retrieve information about the battery.

It then gets:

percent = battery.percent
plugged = battery.power_plugged

where:

- "percent" represents the current battery percentage.
- "plugged" indicates whether the charger is connected.

The program checks the battery level every 60 seconds.

The "notified" variable prevents the same notification from being displayed repeatedly every minute.

Once the battery status no longer matches a warning condition, "notified" is reset, allowing a new notification to be triggered later.

# Platform

This project is designed for Windows because it uses "winotify" and "winsound".
