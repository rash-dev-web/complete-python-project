from selenium import webdriver
import os
import time

driver = webdriver.Chrome(executable_path="../../drivers/chromedriver.exe")
driver.get("https://demoqa.com/alerts")
driver.maximize_window()

# normal alert
driver.find_element_by_id("alertButton").click()
alert = driver.switch_to.alert
alert.accept()

time.sleep(3)

# timer alert
driver.find_element_by_id("timerAlertButton").click()
time.sleep(5)
alert.accept()

# dismiss option
time.sleep(3)
driver.find_element_by_id("confirmButton").click()
alert.dismiss()

# with prompt box
time.sleep(3)
driver.find_element_by_id("promtButton").click()
new_alert = driver.switch_to.alert
new_alert.send_keys("Mir")
new_alert.accept()

time.sleep(3)
driver.quit()
os.system("Taskkill /IM chromedriver.exe /F")
