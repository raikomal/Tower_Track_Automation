# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import ActionChains
# import time
#
# class SliderPage:
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#
#     def click_slider(self, name):
#         if name in self.driver.page_source:
#             return  # already on page
#         self.wait.until(
#             EC.element_to_be_clickable(
#                 (By.XPATH, f"//button[normalize-space()='{name}']")
#             )
#         ).click()
#
#     def hover_and_click_facility_status_tracker(self):
#         from selenium.webdriver.common.action_chains import ActionChains
#         import time
#         from selenium.webdriver.common.by import By
#         from selenium.webdriver.support import expected_conditions as EC
#
#         facility_card = self.wait.until(
#             EC.visibility_of_element_located(
#                 (By.XPATH, "//img[@alt='Facility Status Tracker']")
#             )
#         )
#
#         actions = ActionChains(self.driver)
#
#         # hover (visible)
#         actions.move_to_element(facility_card).perform()
#         time.sleep(2)
#
#         # 🖱 click
#         facility_card.click()
#         time.sleep(2)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SliderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # =========================================================
    # BACKWARD COMPATIBILITY (DO NOT REMOVE)
    # =========================================================
    def click_slider(self, slider_name: str):
        """
        Legacy method used by existing tests
        """
        self.click_slider_button(slider_name)


    def hover_and_click_facility_status_tracker(self):
        """
        Legacy combined navigation used by older tests
        """
        self.navigate_to_part_allocation_insights()
        self.open_facility_status_tracker()


    # ---------------- SLIDER BUTTONS ONLY ----------------
    def click_slider_button(self, name):
        """
        Click slider button by exact text
        NO hover
        NO mouse movement
        """
        btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//button[normalize-space()='{name}']")
            )
        )
        self.driver.execute_script("arguments[0].click();", btn)

    def navigate_to_part_allocation_insights(self):
        """
        As per test case:
        Demand → Capacity → Supply → Part Allocation
        ONLY CLICK BUTTONS
        """
        self.click_slider_button("Demand Insights")
        self.click_slider_button("Capacity Insights")
        self.click_slider_button("Supply Insights")
        self.click_slider_button("Part Allocation Insights")

    # Script_ID:7
    # ---------------- FACILITY STATUS TRACKER ONLY ----------------
    def open_facility_status_tracker(self):
        """
        NO hover
        NO mouse move
        Direct click on Facility Status Tracker image
        """
        tracker_img = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//img[@alt='Facility Status Tracker']")
            )
        )
        self.driver.execute_script("arguments[0].click();", tracker_img)

