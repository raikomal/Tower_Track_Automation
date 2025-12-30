
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    username_input = "//input[@placeholder='Username or email']"
    password_input = "//input[@placeholder='Password']"
    login_button = "//button[normalize-space()='LOGIN']"

    # ================= 1 BASIC ACTIONS =================
   #Script_ID:1
    def clear_fields(self):
        self.driver.find_element(By.XPATH, self.username_input).clear()
        self.driver.find_element(By.XPATH, self.password_input).clear()

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    # Script_ID:2
    def login(self, username, password):
        self.clear_fields()
        self.driver.find_element(By.XPATH, self.username_input).send_keys(username)
        self.driver.find_element(By.XPATH, self.password_input).send_keys(password)
        self.click_login()

    # Script_ID:3
    def enter_email(self, username):
        self.driver.find_element(By.XPATH, self.username_input).clear()
        self.driver.find_element(By.XPATH, self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_input).clear()
        self.driver.find_element(By.XPATH, self.password_input).send_keys(password)

    # ================= ALERT HANDLING =================
    # Script_ID:4
    def accept_alert_if_present(self):
        try:
            alert = self.driver.switch_to.alert
            print("Alert text:", alert.text)
            alert.accept()
            print("Alert OK clicked")
        except NoAlertPresentException:
            pass
        except:
            pass
