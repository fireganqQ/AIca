# by https://github.com/fireganqQ #

import pyaudio, pyfirmata, serial, threading, os, time

board = None
boardBool = None

try:
    board = pyfirmata.Arduino("COM5")
    boardBool = True
except serial.serialutil.SerialException:
    boardBool = False