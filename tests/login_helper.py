# from browser.browser_setup import chrome_setup
# from pages.login_page import LoginPage
# from utils.csv_writer import write_test_report
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# def handle_alert_if_present(driver, timeout=4):
#     try:
#         WebDriverWait(driver, timeout).until(EC.alert_is_present())
#         alert = driver.switch_to.alert
#         alert.accept()
#         time.sleep(2)
#     except:
#         pass

# def login_and_reach_dashboard():
#     driver = chrome_setup()
#     driver.get("http://103.204.95.212:8084/")
#     login_page = LoginPage(driver)

#     # 1️⃣ Empty login
#     login_page.clear_fields()
#     login_page.click_login()
#     login_page.accept_alert_if_present()
#     time.sleep(4)


#     write_test_report(
#         "Tower Track","Web","Login Module",
#         "Login without credentials",
#         "Click login without entering data",
#         "Validation message should appear",
#         "Validation message displayed",
#         "Pass","", "1923",""
#     )

#     # 2️⃣ Invalid login
#     login_page.login("user@123", "123467")
#     handle_alert_if_present(driver)

#     write_test_report(
#         "Tower Track","Web","Login Module",
#         "Login with invalid credentials",
#         "Enter wrong email/password",
#         "Error alert should appear",
#         "Error alert displayed",
#         "Pass","Alert handled", "1923",""
#     )

#     # 3️⃣ Valid login
#     driver.refresh()
#     login_page = LoginPage(driver)
#     login_page.login("user@gmail.com", "12345")

#     # ✅ WAIT FOR DASHBOARD
#     WebDriverWait(driver, 15).until(
#         EC.visibility_of_element_located(
#             ("xpath", "//div[@class='dashboard-card-container flex flex-wrap']")
#         )
#     )

#     write_test_report(
#         "Tower Track","Web","Login Module",
#         "Login with valid credentials",
#         "Enter correct email/password",
#         "Dashboard should load",
#         "Dashboard loaded successfully",
#         "Pass","", "1923",""
#     )

#     print("✅ Dashboard reached after login")
#     return driver   # 🔥 IMPORTANT

# from browser.browser_setup import chrome_setup
# from pages.login_page import LoginPage
# from utils.csv_writer import write_test_report
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
#
# def handle_alert_if_present(driver, timeout=4):
#     try:
#         WebDriverWait(driver, timeout).until(EC.alert_is_present())
#         alert = driver.switch_to.alert
#         alert.accept()
#         time.sleep(2)
#     except:
#         pass
#
#
# def login_and_reach_dashboard():
#     # 1️⃣ Launch Browser
#     driver = chrome_setup()
#     write_test_report(
#         "Tower Track", "Web", "Login Module",
#         "Launch browser",
#         "Open Chrome browser",
#         "Browser should launch",
#         "Browser launched successfully",
#         "Pass", "", "1923", ""
#     )
#
#     # 2️⃣ Open Application URL
#     driver.get("http://103.204.95.212:8084/")
#     write_test_report(
#         "Tower Track", "Web", "Login Module",
#         "Open Tower Track URL",
#         "Navigate to application URL",
#         "Login page should load",
#         "Login page loaded",
#         "Pass", "", "1923", ""
#     )
#
#     login_page = LoginPage(driver)
#
#     # 3️⃣ Empty Login Validation
#     login_page.clear_fields()
#     login_page.click_login()
#     login_page.accept_alert_if_present()
#     time.sleep(2)
#
#     write_test_report(
#         "Tower Track", "Web", "Login Module",
#         "Login without credentials",
#         "Click login without entering data",
#         "Validation message should appear",
#         "Validation message displayed",
#         "Pass", "", "1923", ""
#     )
#
#     # 4️⃣ Invalid Login Validation
#     login_page.login("user@123", "123467")
#     handle_alert_if_present(driver)
#
#     write_test_report(
#         "Tower Track", "Web", "Login Module",
#         "Login with invalid credentials",
#         "Enter wrong email and password",
#         "Error alert should appear",
#         "Error alert displayed",
#         "Pass", "Alert handled", "1923", ""
#     )
#
#     # 5️⃣ Valid Login
#     driver.refresh()
#     login_page = LoginPage(driver)
#     login_page.login("user@gmail.com", "12345")
#
#     # 6️⃣ Dashboard Verification
#     WebDriverWait(driver, 15).until(
#         EC.visibility_of_element_located(
#             ("xpath", "//div[@class='dashboard-card-container flex flex-wrap']")
#         )
#     )
#
#     write_test_report(
#         "Tower Track", "Web", "Login Module",
#         "Login with valid credentials",
#         "Enter correct email and password",
#         "Dashboard should load",
#         "Dashboard loaded successfully",
#         "Pass", "", "1923", ""
#     )
#
#     print("✅ Dashboard reached after login")
#     return driver
from browser.browser_setup import chrome_setup
from pages.login_page import LoginPage
from utils.csv_writer import write_test_report

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_and_reach_dashboard():
    # 1️⃣ Launch Browser
    driver = chrome_setup()

    write_test_report(
        "Tower Track", "Web", "Login Module",
        "Launch browser",
        "Open Chrome browser",
        "Browser should launch",
        "Browser launched successfully",
        "Pass", "", "LG-01", ""
    )

    # 2️⃣ Open Application URL
    driver.get("http://103.204.95.212:8084/facility_tracker")

    write_test_report(
        "Tower Track", "Web", "Login Module",
        "Open Tower Track URL",
        "Navigate to application URL",
        "Login page should load",
        "Login page loaded",
        "Pass", "", "LG-02", ""
    )

    login = LoginPage(driver)

    # 3️⃣ Empty login
    login.clear_fields()
    login.click_login()
    login.accept_alert_if_present()
    time.sleep(1)

    write_test_report(
        "Tower Track", "Web", "Login Module",
        "Empty Login",
        "Click login without credentials",
        "Validation should appear",
        "Validation shown",
        "Pass", "", "LG-03", ""
    )

    # 4️⃣ Invalid login
    login.login("user@123", "123456")
    login.accept_alert_if_present()

    write_test_report(
        "Tower Track", "Web", "Login Module",
        "Invalid Login",
        "Enter wrong credentials",
        "Error alert should appear",
        "Error alert shown",
        "Pass", "", "LG-04", ""
    )
    # Script_ID:5
    # 5️⃣ Valid login
    driver.refresh()
    login = LoginPage(driver)

    login.enter_email("user@gmail.com")
    login.enter_password("12345")
    login.click_login()
    login.accept_alert_if_present()

    # Script_ID:6
    # 6️⃣ Dashboard verification
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            ("xpath", "//div[@class='dashboard-card-container flex flex-wrap']")
        )
    )

    write_test_report(
        "Tower Track", "Web", "Login Module",
        "Verify Dashboard",
        "Wait for dashboard",
        "Dashboard should load",
        "Dashboard loaded",
        "Pass", "", "LG-08", ""
    )

    print("✅ Dashboard reached after login")
    return driver
