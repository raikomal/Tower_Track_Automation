from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

class SliderPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_slider(self, slider_name):
        slider_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//button[normalize-space()='{slider_name}']")
            )
        )
        slider_button.click()

    def hover_and_click_facility_status_tracker(self):
        from selenium.webdriver.common.action_chains import ActionChains
        import time
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support import expected_conditions as EC

        facility_card = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//img[@alt='Facility Status Tracker']")
            )
        )

        actions = ActionChains(self.driver)

        # hover (visible)
        actions.move_to_element(facility_card).perform()
        time.sleep(2)

        # 🖱 click
        facility_card.click()
        time.sleep(2)
