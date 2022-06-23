import json
from pyautogui import *
import time
import keyboard
import random
import win32api, win32con
import pyautogui

print("1: Mouse Mode")
print("2: Keyboard Mode")
selectmode = input("Select Mode : ")

with open('config.json') as config_file:
    data = json.load(config_file)
tiles1x = data['tiles1x']
tiles1y = data['tiles1y']
tiles2x = data['tiles2x']
tiles2y = data['tiles2y']
tiles3x = data['tiles3x']
tiles3y = data['tiles3y']
tiles4x = data['tiles4x']
tiles4y = data['tiles4y']
key1 = data['key1']
key2 = data['key2']
key3 = data['key3']
key4 = data['key4']

if selectmode == '1':
    def click(x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    while keyboard.is_pressed("q")==False:
        if pyautogui.pixel(tiles1x, tiles1y)[0]==0: 
            click(tiles1x, tiles1y)
        if pyautogui.pixel(tiles2x, tiles2y)[0]==0:
            click(tiles2x, tiles2y)
        if pyautogui.pixel(tiles3x, tiles3y)[0]==0:
            click(tiles3x, tiles3y)
        if pyautogui.pixel(tiles4x, tiles4y)[0]==0:
            click(tiles4x, tiles4y)
elif selectmode == '2':
    while keyboard.is_pressed("=")==False:
        if pyautogui.pixel(tiles1x, tiles1y)[0]==0: 
            keyboard.send(key1)
        if pyautogui.pixel(tiles2x, tiles2y)[0]==0:
            keyboard.send(key2)
        if pyautogui.pixel(tiles3x, tiles3y)[0]==0:
            keyboard.send(key3)
        if pyautogui.pixel(tiles4x, tiles4y)[0]==0:
            keyboard.send(key4)
