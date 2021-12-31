#! usr/bin/env python3
import sys
import os
import time
import socket
from datetime import datetime
from subprocess import call

os.system("echo Helloooooooo")

import sys
sys.path.append("../") # set system path to top

from devices import dfrobot_epaper
from display_extension.freetype_helper import Freetype_Helper

fontFilePath = "/home/pi/DFRobot_RPi_Display_V3/display_extension/wqydkzh.ttf" # fonts file

# peripheral params
RASPBERRY_SPI_BUS = 0
RASPBERRY_SPI_DEV = 0
RASPBERRY_PIN_CS = 27
RASPBERRY_PIN_CD = 17
RASPBERRY_PIN_BUSY = 4
RASPBERRY_PIN_RST = 26
epaper = dfrobot_epaper.DFRobot_Epaper_SPI(RASPBERRY_SPI_BUS, RASPBERRY_SPI_DEV, RASPBERRY_PIN_CS, RASPBERRY_PIN_CD, RASPBERRY_PIN_BUSY,RASPBERRY_PIN_RST) # create epaper object

# clear screen
epaper.begin()

epaper.clearScreen();


# config extension fonts
ft = Freetype_Helper(fontFilePath)
ft.setDisLowerLimite(112) # set display lower limit, adjust this to effect fonts color depth
epaper.setExFonts(ft) # init with fonts file
epaper.setTextFormat(1, epaper.BLACK, epaper.WHITE, 1, 1)


def get_ip_address():
 ip_address = '';
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 s.connect(("8.8.8.8",80))
 ip_address = s.getsockname()[0]
 s.close()
 return ip_address

print('Local IP Address:\n')
print(get_ip_address())


# print test
epaper.setExFontsFmt(32, 32) # set extension fonts width and height
epaper.setTextCursor(69, 0)
epaper.printStr("IP address")
epaper.flush(epaper.PART)
time.sleep(1)

epaper.setExFontsFmt(24, 24) # set extension fonts width and height
epaper.setTextCursor(0, 32)
epaper.printStr(get_ip_address())
epaper.flush(epaper.PART)
time.sleep(1)

now = datetime.now()

current_date = now.strftime("%d/%m/%Y")
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

epaper.setExFontsFmt(24, 24) # set extension fonts width and height
epaper.setTextCursor(0, 60)
epaper.printStr(current_time)
epaper.setTextCursor(0, 80)
epaper.printStr(current_date)
epaper.flush(epaper.PART)
time.sleep(1)