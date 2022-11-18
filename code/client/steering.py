import math
from command import COMMAND, COMMAND_SEPARATOR, COMMAND_TERMINATOR
import statistics

class Steering:
    def __init__(self, control):
        self.control = control

    def steer(self, lines):
        if lines is not None and len(lines) > 0:
            line_angles = []
            for line in lines:
                x1,y1,x2,y2 = line[0]
                line_angles.append(self.line_to_deg([x1, y1, x2, y2]))
                print(line_angles)
                turn_direction,turn_angle = self.get_turn(line_angles)
                # positives
            self.forward()
            print('forward')
        else:
            self.stop()
            print('stop')

    def line_to_deg(self, line):
        angle_rad = math.atan2(line[1] - line[3], line[0] - line[2])
        angle_deg = int(angle_rad * 180 / math.pi)
        return angle_deg

    def stop(self):
        stop = COMMAND_SEPARATOR + str(0) + COMMAND_SEPARATOR + str(0) + COMMAND_SEPARATOR + str(
            0) + COMMAND_SEPARATOR + str(0) + COMMAND_TERMINATOR
        self.control.send_data(COMMAND.CMD_MOTOR + stop)

    def forward(self):
        forward = COMMAND_SEPARATOR + str(1000) + COMMAND_SEPARATOR + str(1000) + COMMAND_SEPARATOR + str(
            1000) + COMMAND_SEPARATOR + str(1000) + COMMAND_TERMINATOR
        self.control.send_data(COMMAND.CMD_MOTOR + forward)

    def turn_left(self):
        turn_left = COMMAND_SEPARATOR + str(-4095) + COMMAND_SEPARATOR + str(-1500) + COMMAND_SEPARATOR + str(
            1500) + COMMAND_SEPARATOR + str(1500) + COMMAND_TERMINATOR
        self.control.send_data(COMMAND.CMD_MOTOR + turn_left)

    def backwards(self):
        backwards = COMMAND_SEPARATOR + str(-4095) + COMMAND_SEPARATOR + str(-4095) + COMMAND_SEPARATOR + str(
            -4095) + COMMAND_SEPARATOR + str(-4095) + COMMAND_TERMINATOR
        self.control.send_data(COMMAND.CMD_MOTOR + backwards)

    def turn_right(self):
        turn_right = COMMAND_SEPARATOR + str(1500) + COMMAND_SEPARATOR + str(1500) + COMMAND_SEPARATOR + str(
            -1500) + COMMAND_SEPARATOR + str(-1500) + COMMAND_TERMINATOR
        self.control.send_data(COMMAND.CMD_MOTOR + turn_right)

    def get_turn(self, line_angles):
        pos = list(filter(lambda angle: angle >= 0 and angle < 175, line_angles))
        posMedian = None
        negMedian = None
        if pos is not None and len(pos) > 0:
            posMedian = statistics.median(pos)
        neg = list(filter(lambda angle: angle < 0 and angle > -175, line_angles))
        if neg is not None and len(neg) > 0:
            negMedian = statistics.median(neg)
        # left are positive

        # right are negative

        turn_direction = 0
        turn_angle = 10
        return turn_direction, turn_angle

if __name__ == '__main__':
    pass
