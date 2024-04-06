from selenium import webdriver
import time
import pyautogui
import pyscreeze
import PILTools
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import login

def button_for_play(driver, button_html):
        max_retries = 3
        attempt = 0
        while attempt < max_retries:
                try:
                        button_play = driver.find_element(By.XPATH, button_html)
                        button_play.click()
                        time.sleep(45)
                        driver.refresh()
                        time.sleep(7)
                        break
                except NoSuchElementException:
                        attempt += 1






'''def button_for_play(imagem):
    position = pyautogui.locateCenterOnScreen(imagem)
    return position

buttonPos = button_for_play('assets/button.png')

while True:
    if buttonPos:
        pyautogui.click(buttonPos)
    time.sleep(10)
    driver.refresh()
    pyautogui.moveTo(centerX, centerY)
    time.sleep(7)  # for loading

# fecha o navegador
#driver.quit()'''
