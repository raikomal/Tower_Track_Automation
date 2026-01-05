#
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoAlertPresentException
#
#
# class LoginPage:
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     # Locators
#     username_input = "//input[@placeholder='Username or email']"
#     password_input = "//input[@placeholder='Password']"
#     login_button = "//button[normalize-space()='LOGIN']"
#
#     # ================= 1 BASIC ACTIONS =================
#    #Script_ID:1
#     def clear_fields(self):
#         self.driver.find_element(By.XPATH, self.username_input).clear()
#         self.driver.find_element(By.XPATH, self.password_input).clear()
#
#     def click_login(self):
#         self.driver.find_element(By.XPATH, self.login_button).click()
#
#     # Script_ID:2
#     def login(self, username, password):
#         self.clear_fields()
#         self.driver.find_element(By.XPATH, self.username_input).send_keys(username)
#         self.driver.find_element(By.XPATH, self.password_input).send_keys(password)
#         self.click_login()
#
#     # Script_ID:3
#     def enter_email(self, username):
#         self.driver.find_element(By.XPATH, self.username_input).clear()
#         self.driver.find_element(By.XPATH, self.username_input).send_keys(username)
#
#     def enter_password(self, password):
#         self.driver.find_element(By.XPATH, self.password_input).clear()
#         self.driver.find_element(By.XPATH, self.password_input).send_keys(password)
#
#     # ================= ALERT HANDLING =================
#     # Script_ID:4
#     def accept_alert_if_present(self):
#         try:
#             alert = self.driver.switch_to.alert
#             print("Alert text:", alert.text)
#             alert.accept()
#             print("Alert OK clicked")
#         except NoAlertPresentException:
#             pass
#         except:
#             pass
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # ================= LOCATORS =================
    username_input = "//input[@placeholder='Username or email']"
    password_input = "//input[@placeholder='Password']"
    login_button = "//button[normalize-space()='LOGIN']"

    remember_me_label = "//label[normalize-space()='Remember Me']"
    remember_me_checkbox = "//label[normalize-space()='Remember Me']/preceding-sibling::input | //label[normalize-space()='Remember Me']/input"

    # ================= BASIC ACTIONS =================
    # Script_ID:1
    def clear_fields(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.username_input))).clear()
        self.driver.find_element(By.XPATH, self.password_input).clear()

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_button))).click()

    # ================= REMEMBER ME =================
    # Script_ID:1A
    def click_remember_me_if_not_selected(self):
        """
        Click Remember Me checkbox ONLY if not already selected
        """
        try:
            checkbox = self.driver.find_element(By.XPATH, self.remember_me_checkbox)

            if not checkbox.is_selected():
                self.driver.find_element(By.XPATH, self.remember_me_label).click()
                print("✅ Remember Me checkbox selected")
            else:
                print("ℹ️ Remember Me already selected")

        except Exception as e:
            print("⚠️ Remember Me checkbox not found or not clickable:", e)

    # ================= LOGIN FLOWS =================
    # Script_ID:2
    def login(self, username, password, remember_me=False):
        self.clear_fields()

        self.driver.find_element(By.XPATH, self.username_input).send_keys(username)
        self.driver.find_element(By.XPATH, self.password_input).send_keys(password)

        if remember_me:
            self.click_remember_me_if_not_selected()

        self.click_login()

    # Script_ID:3
    def enter_email(self, username):
        field = self.driver.find_element(By.XPATH, self.username_input)
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.driver.find_element(By.XPATH, self.password_input)
        field.clear()
        field.send_keys(password)

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
        except Exception:
            pass
