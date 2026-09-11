import psutil
import time
from winotify import Notification
import winsound

notified = False

while True:
    battery = psutil.sensors_battery()

    percent = battery.percent
    plugged = battery.power_plugged

    print(f"Battery : {percent}% | Charger : {plugged}")

    if percent <= 30 and not plugged:

        if not notified:
            notification = Notification(
                app_id = "Battery Monitor",
                title = "Battery Low",
                msg = f"{percent}% Battery Remaining!"
            )

            winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
            notification.show()
            notified = True

    elif percent == 79 and  plugged:

        if not notified:
                notification = Notification(
                    app_id = "Battery Monitor",
                    title = "Battery Low",
                    msg = f"{percent}% Battery Remaining!"
                )
        
                winsound.MessageBeep(winsound.MB_ICONHAND)
                notification.show()
                notified = True

    else:
        notified = False

    time.sleep(60)

