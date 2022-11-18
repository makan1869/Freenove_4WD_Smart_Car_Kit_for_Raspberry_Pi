import math
from command import COMMAND, COMMAND_SEPARATOR, COMMAND_TERMINATOR
import statistics
import collections

class Steering:

    buffer = collections.deque(maxlen=5)

    def __init__(self, control):
        self.control = control
        self.calibrate_servo()

    def steer(self, lines):
        if lines is not None and len(lines) > 0:
            self.buffer.append(lines)
            line_angles = []
            for buffer_item in self.buffer:
                for line in buffer_item:
                    x1,y1,x2,y2 = line[0]
                    line_angles.append(self.line_to_deg([x1, y1, x2, y2]))
            self.get_turn(line_angles)
        else:
            self.stop()
            # print('stop')

    def line_to_deg(self, line):
        angle_rad = math.atan2(line[1] - line[3], line[0] - line[2])
        angle_deg = int(angle_rad * 180 / math.pi)
        return angle_deg

    def stop(self):
        stop = COMMAND_SEPARATOR + str(0) + COMMAND_SEPARATOR + str(0) + COMMAND_SEPARATOR + str(
            0) + COMMAND_SEPARATOR + str(0) + COMMAND_TERMINATOR
        self.control.send_data(COMMAND.CMD_MOTOR + stop)

    def forward(self):
        forward = COMMAND_SEPARATOR + str(600) + COMMAND_SEPARATOR + str(600) + COMMAND_SEPARATOR + str(
            600) + COMMAND_SEPARATOR + str(600) + COMMAND_TERMINATOR
        self.control.send_data(COMMAND.CMD_MOTOR + forward)

    def turn_left(self):
        turn_left = COMMAND_SEPARATOR + str(0) + COMMAND_SEPARATOR + str(0) + COMMAND_SEPARATOR + str(
            600) + COMMAND_SEPARATOR + str(600) + COMMAND_TERMINATOR
        self.control.send_data(COMMAND.CMD_MOTOR + turn_left)

    def backwards(self):
        backwards = COMMAND_SEPARATOR + str(-4095) + COMMAND_SEPARATOR + str(-4095) + COMMAND_SEPARATOR + str(
            -4095) + COMMAND_SEPARATOR + str(-4095) + COMMAND_TERMINATOR
        self.control.send_data(COMMAND.CMD_MOTOR + backwards)

    def turn_right(self):
        turn_right = COMMAND_SEPARATOR + str(600) + COMMAND_SEPARATOR + str(600) + COMMAND_SEPARATOR + str(
            0) + COMMAND_SEPARATOR + str(0) + COMMAND_TERMINATOR
        self.control.send_data(COMMAND.CMD_MOTOR + turn_right)

    def get_turn(self, line_angles):
        pos = list(filter(lambda angle: angle >= 0 and angle < 175, line_angles))
        posMedian = 0
        negMedian = 0
        if pos is not None and len(pos) > 0:
            posMedian = statistics.median(pos)
        neg = list(filter(lambda angle: angle < 0 and angle > -175, line_angles))
        if neg is not None and len(neg) > 0:
            negMedian = statistics.median(neg)
        print(str(posMedian) + ' ' + str(negMedian))
        if (negMedian == 0 or posMedian > 160):
            print('right')
            self.turn_right()
        elif (posMedian == 0 or negMedian > -100):
            print('left')
            self.turn_left()
        else:
            print('forward')
            self.forward()
        pass

    def calibrate_servo(self):
        self.control.send_data(
            COMMAND.CMD_SERVO + COMMAND_SEPARATOR + '0' + COMMAND_SEPARATOR + str(96) + COMMAND_TERMINATOR)

if __name__ == '__main__':
    pass
