import serial


class Car:
    #  ----------------------------------------------Constantes---------------------------------------------------------
    STOP_CODE = b'1'
    STRAIGHT_MOVE_CODE = b'2'
    RIGHT_TURN_CODE = b'3'
    LEFT_TURN_CODE = b'4'
    # ------------------------------------------------------------------------------------------------------------------

    def __init__(self, bluetooth_port):
        self.connection = serial.Serial(bluetooth_port, 9600, timeout=1)

    def stop(self):
        self.connection.write(self.STOP_CODE)

    def straight_move(self):
        self.connection.write(self.STRAIGHT_MOVE_CODE)

    def right_turn(self):
        self.connection.write(self.RIGHT_TURN_CODE)

    def left_turn(self):
        self.connection.write(self.LEFT_TURN_CODE)


