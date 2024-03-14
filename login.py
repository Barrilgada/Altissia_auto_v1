from selenium import webdriver
import time
import pyautogui
import pyscreeze
import PILTools
from selenium.webdriver.common.by import By

def login_credentials(text, password):
    pyautogui.press('tab', presses=3)
    time.sleep(1)
    pyautogui.typewrite(text)
    time.sleep(1)
    pyautogui.press('tab', presses=1)
    time.sleep(1)
    pyautogui.typewrite(password)
    time.sleep(1)
    pyautogui.press('enter', presses=1)

