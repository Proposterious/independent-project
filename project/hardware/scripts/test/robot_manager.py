"""RobotManager class"""
import serial

class RobotManager:
    """Handles Robot interaction and communication"""
    def __init__(self, port: str = '/dev/ttyACMO', baud_rate: str = "9600"):
        self.port = port
        self.baud_rate = baud_rate
    def __str__(self):
        return f"Robot {self.port} is running..."

    # Communicate with Arduino Uno
    def send_command(self, command: str):
        """Send encoded string to Arduino Uno"""
        ser = serial.Serial(self.port, self.baud_rate) # initiate connection
        ser.write(command.encode()) # send command to arduino
