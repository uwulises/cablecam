from serial_msg import SerialControl

cablecam = SerialControl()
cablecam.open_serial()

cablecam.home()
