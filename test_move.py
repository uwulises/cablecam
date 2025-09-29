from serial_msg.SerialControl import SerialControl

cablecam = SerialControl()
cablecam.open_serial()

cablecam.home()
