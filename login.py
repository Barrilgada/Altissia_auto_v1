from selenium import webdriver
import time
import pyautogui
import pyscreeze
import PILTools
from selenium.webdriver.common.by import By

def login_credentials(text, password, email_html, driver, password_html):
    email = driver.find_element(By.XPATH, email_html)
    email.click()
    time.sleep(1)
    pyautogui.typewrite(text)
    password_html = driver.find_element(By.XPATH, password_html)
    password_html.click()
    time.sleep(1)
    pyautogui.typewrite(password)
    pyautogui.press('enter', presses=1)

