from selenium import webdriver
import os


driver = webdriver.Chrome(executable_path="../../drivers/chromedriver.exe")
URL = "https://demoqa.com/browser-windows"
driver.get(URL)
driver.maximize_window()

# get the current window
parent_window = driver.current_window_handle
driver.find_element_by_id("windowButton").click()

# get all windows
all_windows = driver.window_handles

# switch to child window and get url
for window in all_windows:
    print(window)
    if window != parent_window:
        driver.switch_to.window(window)
        print(driver.current_url)
        assert driver.current_url == "https://demoqa.com/sample"

driver.quit()
os.system("Taskkill /IM chromedriver.exe /F")
