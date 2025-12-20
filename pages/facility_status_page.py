from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class FacilityStatusPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # =========================================================
    # STRATEGIC OVERVIEW TAB
    # =========================================================
    STRATEGIC_OVERVIEW = (
        By.XPATH, "//button[normalize-space()='Strategic Overview']"
    )

    STRATEGIC_OVERVIEW_TEXT = (
        By.XPATH, "//*[contains(text(),'Overall Fulfillment Rate')]"
    )

    # =========================================================
    # MAP LOCATORS (Highcharts – SAFE DEFAULTS)
    # =========================================================
    MAP_CONTAINER = (By.CSS_SELECTOR, "svg")
    FACILITY_POINTS = (By.CSS_SELECTOR, "path")
    TOOLTIP = (By.CSS_SELECTOR, "g.highcharts-tooltip")

    # =========================================================
    # ACTIONS
    # =========================================================
    def click_strategic_overview(self):
        self.wait.until(
            EC.element_to_be_clickable(self.STRATEGIC_OVERVIEW)
        ).click()

    def verify_strategic_overview_loaded(self):
        self.wait.until(
            EC.visibility_of_element_located(self.STRATEGIC_OVERVIEW_TEXT)
        )
        return True

    # =========================================================
    # MAP – ONE FACILITY HOVER
    # =========================================================
    def hover_on_first_facility(self):
        self.wait.until(
            EC.visibility_of_element_located(self.MAP_CONTAINER)
        )

        points = self.wait.until(
            EC.presence_of_all_elements_located(self.FACILITY_POINTS)
        )

        if not points:
            raise Exception("No map points found")

        ActionChains(self.driver).move_to_element(points[0]).perform()

    def is_tooltip_visible(self):
        self.wait.until(
            EC.visibility_of_element_located(self.TOOLTIP)
        )
        return True
