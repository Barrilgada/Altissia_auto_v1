from selenium import webdriver
import time
import pyautogui
import pyscreeze
import PILTools
from selenium.webdriver.common.by import By
import login
import auto_play
#VARIÁVEIS

#URL's
altissia = "https://learn.altissia.org/platform/#/learning-path"
altissia_video = "https://learn.altissia.org/platform/#/learning-path/mission/STARTING_AND_FINISHING_PHONE_CALLS_OR_EMAILS/lesson/EN_GB_B1_JOB_ENDING_A_PHONE_CALL/activity/EN_GB_B1_JOB_ENDING_A_PHONE_CALL_VIDEO_ANIMATION_LESSON_5_EMAIL_AND_PHONE/video"

#LOGIN
email = "mateo.rodriguez@uscsonline.com.br"
password = ""

#BOTÃO
button_html = '//button[@aria-label="Play"]'
email_html = '//input[@data-test="email-field"]'
password_html = '//input[@data-test="password-field"]'
#############################################
driver = webdriver.Chrome()

driver.get(altissia)

time.sleep(5)#FOR LOADING

login.login_credentials(email, password, email_html, driver, password_html)

time.sleep(10)#FOR LOGIN

driver.get(altissia_video)

time.sleep(10)


while True:
    auto_play.button_for_play(driver, button_html)