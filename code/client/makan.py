from threading import Thread, Timer
from video import VideoStreaming
from control import Control
import cv2
import numpy as np
import struct

class Car:
    def __init__(self):
        self.display_timer = None
        self.display_thread = None
        self.recv_message = None
        self.streaming_thread = None
        self.video_streaming = None
        self.control = None
        self.receive_thread = None
        self.connected = False
        self.target_host = '192.168.8.123'

    def exec(self):
        cv2.startWindowThread()
        cv2.namedWindow('video')

        cv2.waitKey(0)
        print("Initiating Executing ... ")
        if not self.connected:
            print("Connecting ....")
            try:
                self.control = Control(self.target_host)
                self.receive_thread = Thread(target=self.recv_message)
                self.receive_thread.start()
            except Exception as e:
                print(e)
                print('control error')
                return
            print("Getting the Stream ...")
            try:
                self.video_streaming = VideoStreaming(self.target_host)
                self.streaming_thread = Thread(target=self.video_streaming.start_processing())
                self.display_timer = RepeatTimer(1, self.video_streaming.display_video())
                self.display_thread.start()
                self.streaming_thread.start()
            except Exception as e:
                print(e)
                print('video error')
                return
            print('Server address:' + str(self.target_host) + '\n')
            self.connected = True
        print("Got Executed")


class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

if __name__ == '__main__':
    car = Car()

    car.exec()
