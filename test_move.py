from serial_msg.SerialControl import SerialControl

cablecam = SerialControl()
cablecam.open_serial()

cablecam.home()

while True:
    pos = input("Enter position in mm (or 'exit' to quit): ")
    if pos.lower() == 'exit':
        break
    try:
        mm = float(pos)
        cablecam.moveto_mm(mm)
    except ValueError:
        print("Please enter a valid number.")