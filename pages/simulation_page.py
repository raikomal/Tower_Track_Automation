import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class SimulationPage:
    def __init__(self, driver, timeout=40):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # =====================================================
    # RENDER CHECK
    # =====================================================
    def is_rendered(self):
        try:
            self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//h2[normalize-space()='Simulation Planning Tool']")
                )
            )
            return True
        except Exception:
            return False

    # =====================================================
    # LOCATORS (SCOPED!)
    # =====================================================
    SIMULATION_CONTAINER = (
        By.XPATH,
        "//h2[normalize-space()='Simulation Planning Tool']/ancestor::div[contains(@class,'border-gray-600')]"
    )

    SIMULATE_BTN = (
        By.XPATH,
        ".//button[contains(text(),'Simulate')]"
    )

    COMBOBOXES = (By.XPATH, ".//select")

    QUANTITY_INPUT = (
        By.XPATH, ".//input[@placeholder='Quantity' or @name='Quantity']"
    )

    # 👉 SVG ONLY INSIDE SIMULATION TOOL
    SIMULATION_BARS = (
        By.XPATH,
        ".//*[name()='svg']//*[contains(@class,'highcharts-point')]"
    )

    # =====================================================
    # SLOW INTERNAL SCROLL (VISIBLE)
    # =====================================================
    def scroll_inside(self, container, steps=6):
        for _ in range(steps):
            self.driver.execute_script(
                "arguments[0].scrollTop += 180;", container
            )
            time.sleep(0.6)

    # =====================================================
    # RUN SIMULATION (CORRECT)
    # =====================================================
    def run_simulation_safe(self, source, destination, part, quantity):
        try:
            sim = self.wait.until(
                EC.presence_of_element_located(self.SIMULATION_CONTAINER)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", sim
            )
            time.sleep(2)

            combos = sim.find_elements(*self.COMBOBOXES)

            Select(combos[0]).select_by_visible_text(source)
            time.sleep(1)

            Select(combos[1]).select_by_visible_text(destination)
            time.sleep(1)

            Select(combos[2]).select_by_visible_text(part)
            time.sleep(1)

            qty = sim.find_element(*self.QUANTITY_INPUT)
            qty.clear()
            qty.send_keys(quantity)
            time.sleep(1)

            sim.find_element(*self.SIMULATE_BTN).click()
            print("✅ Simulate Reallocation clicked")

            time.sleep(4)
            return True

        except Exception as e:
            print(f"❌ Simulation failed: {e}")
            return False

    # =====================================================
    # ✅ CORRECT HOVER — ONLY SIMULATION CHARTS
    # =====================================================
    def hover_cost_graphs(self):
        try:
            sim = self.wait.until(
                EC.presence_of_element_located(self.SIMULATION_CONTAINER)
            )

            # scroll further DOWN to charts
            self.scroll_inside(sim, steps=8)

            bars = sim.find_elements(*self.SIMULATION_BARS)

            if not bars:
                raise Exception("No simulation bars found")

            print(f"🟢 Found {len(bars)} simulation bars")

            actions = ActionChains(self.driver)

            for i, bar in enumerate(bars[:4]):
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", bar
                )
                time.sleep(1)

                actions.move_to_element(bar).pause(1).perform()
                print(f"✅ Hovered SIMULATION bar {i+1}")
                time.sleep(2)

            print("✅ Simulation Planning Tool graph hover SUCCESS")
            return True

        except Exception as e:
            print(f"❌ Simulation hover failed: {e}")
            return False
