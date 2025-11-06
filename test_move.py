from serial_msg.SerialControl import SerialControl

cablecam = SerialControl()
cablecam.open_serial()

while True:
    pos = input("Enter position in mm (or 'exit' to quit or 'home' to go home): ")
    if pos.lower() == 'exit':
        break
    elif pos.lower() == 'home':
        cablecam.home()
        continue
    try:
        mm = float(pos)
        cablecam.moveto_mm(mm)
    except ValueError:
        print("Please enter a valid number.")