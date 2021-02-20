from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:

    def test_valid_login(self):
        url = "https://courses.letskodeit.com"
        driver = webdriver.Chrome(executable_path="../../drivers/chromedriver.exe")
        driver.maximize_window()
        driver.get(url=url)

        sign_in_link = driver.find_element(By.XPATH, "//a[text()='Sign In']")
        sign_in_link.click()

        email_id = driver.find_element(By.ID, "email")
        email_id.send_keys("newkodeuser@test.com")

        password = driver.find_element(By.ID, "password")
        password.send_keys("brownwindow*03")

        login_button = driver.find_element(By.XPATH, "//input[@value='Login']")
        login_button.click()

        image_home = driver.find_element(By.XPATH, "//img[@class='img-fluid']")
        if image_home is not None:
            print("test successful")
        else:
            print("test failed")


test_login = TestLogin()
test_login.test_valid_login()
