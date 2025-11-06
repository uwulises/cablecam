from serial_msg.SerialControl import SerialControl
import time

cablecam = SerialControl()
cablecam.open_serial()

while True:
    pos = input("Enter position in mm (or 'exit' to quit or 'home' to go home): ")
    if pos.lower() == 'exit':
            break
    elif pos.lower() == 'home':
        cablecam.home()
        print("homing")
        time.sleep(2)
        continue
    try:
        if float(pos) == mm:
            print("You are already at this position.")
        else:
            mm = float(pos)
            cablecam.moveto_mm(mm)
    except ValueError:
        print("Please enter a valid number.")