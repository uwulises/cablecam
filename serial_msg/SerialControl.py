from serial import Serial
import time


class SerialControl:

    def __init__(self, port="COM9"):
        self.port = port
        self.serial = None

    def open_serial(self):
        try:
            self.serial = Serial(
                self.port, 9600, timeout=1, write_timeout=0.1)
            print("The port is available")
            serial_port = "Open"
            time.sleep(2)
        except:
            print("The port is at use")
            self.serial.close()
            self.serial.open()

    def close_serial(self):
        time.sleep(0.2)
        self.serial.close()
    
    # Send a command to the Arduino
    def send_command(self, cmd_vel=[90,90,90]):
        # Match case structure to send the right command to arduino
        pos= str(int(cmd_vel[0])).zfill(3) + str(int(cmd_vel[1])).zfill(3) + str(int(cmd_vel[2])).zfill(3)
        
        # Get the function from switcher dictionary
        func = 'MOVEAX' + pos + '\n'
        # Execute the function
        self.serial.write(func.encode())

    def home(self):
        self.serial.write("Homing\n".encode())

    def disable_stepper(self):
        self.serial.write("Disable_Stepper\n".encode())

    def ensable_stepper(self):
        self.serial.write("Enable_Stepper\n".encode())

    #En coordenadas absolutas desde la posicion home (0)
    def moveto_mm(self, mm=0):
        pos= str(int(mm)).zfill(7)
        func = 'Moveto_mm' + pos + '\n'
        self.serial.write(func.encode())

mono = SerialControl()
mono.open_serial()

mono.moveto_mm(mm=1000)

mono.close_serial()