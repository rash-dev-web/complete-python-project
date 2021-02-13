from selenium import webdriver
import os


driver = webdriver.Chrome(executable_path="../../drivers/chromedriver.exe")
URL = "https://demoqa.com/browser-windows"
driver.get(URL)
driver.maximize_window()

# current window
current_window = driver.current_window_handle
driver.find_element_by_id("messageWindowButton").click()

# get all windows
all_windows = driver.window_handles
for window in all_windows:
    if current_window != window:
        driver.switch_to.window(window)
        # print(driver.current_url)
        # print(driver.page_source)

driver.quit()
os.system("Taskkill /IM chromedriver.exe /F")