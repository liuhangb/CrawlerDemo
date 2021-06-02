# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# coding=utf-8

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {
  'platformName': 'Android',
  'deviceName': '192.168.2.6:5555',
  'platformVersion': '9',
  'appPackage': 'com.meitu.camera.samples',
  'appActivity': 'com.meitu.camera.samples.MainActivity'
 }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
wait = WebDriverWait(driver, 300)
login_btn = wait.until(EC.element_to_be_clickable((By.ID, "com.meitu.camera.samples:id/button_ar_fragment")))
login_btn.click()

change_login_btn = wait.until(EC.element_to_be_clickable((By.ID, "com.meitu.camera.samples:id/ibtn_take_media")))
change_login_btn.click()