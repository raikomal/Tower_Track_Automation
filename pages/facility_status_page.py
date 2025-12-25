# # import time
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait, Select
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.webdriver.common.action_chains import ActionChains
#
#
# # class FacilityStatusPage:
# #     DEMO_MODE = True
# #     DEMO_DELAY = 3
#
# #     def __init__(self, driver):
# #         self.driver = driver
# #         self.wait = WebDriverWait(driver, 40)
#
# #     # ---------------- DEMO CONTROL ----------------
# #     def demo_pause(self, multiplier=1):
# #         time.sleep(self.DEMO_DELAY * multiplier)
#
# #     # =========================================================
# #     # STRATEGIC OVERVIEW
# #     # =========================================================
# #     def click_strategic_overview(self):
# #         self.wait.until(
# #             EC.element_to_be_clickable(
# #                 (By.XPATH, "//button[normalize-space()='Strategic Overview']")
# #             )
# #         ).click()
#
# #     def verify_strategic_overview_loaded(self):
# #         self.wait.until(
# #             EC.presence_of_element_located(
# #                 (By.XPATH, "//*[name()='path' and contains(@class,'highcharts-point')]")
# #             )
# #         )
# #         return True
#
# # # =========================================================
# # # MAP – STATUS OF ALL FACILITIES
# # # =========================================================
#
# # def get_facility_map_points(self):
# #     """
# #     Returns all Highcharts map circles (facility points)
# #     """
# #     self.wait.until(
# #         EC.presence_of_element_located(
# #             (By.XPATH, "//*[name()='path' and contains(@class,'highcharts-point')]")
# #         )
# #     )
# #     return self.driver.find_elements(
# #         By.XPATH, "//*[name()='path' and contains(@class,'highcharts-point')]"
# #     )
#
#
# # def hover_on_map_point(self, point):
# #     """
# #     Hover single map circle
# #     """
# #     ActionChains(self.driver).move_to_element(point).pause(0.5).perform()
#
#
# # def hover_multiple_map_circles(self, count=5):
# #     """
# #     Demo-friendly map hover:
# #     - picks 4–5 circles
# #     - 0.5s pause between
# #     """
# #     points = self.get_facility_map_points()
#
# #     if not points:
# #         return False
#
# #     count = min(count, len(points))
#
# #     for p in points[:count]:
# #         self.driver.execute_script(
# #             "arguments[0].scrollIntoView({block:'center'});", p
# #         )
# #         ActionChains(self.driver).move_to_element(p).pause(0.5).perform()
#
# #     return True
#
#
#
# # # def get_facility_map_points(self):
# # #     return self.driver.find_elements(
# # #         By.XPATH, "//*[name()='path' and contains(@class,'highcharts-point')]"
# # #     )
#
# # # def hover_on_map_point(self, point):
# # #     """
# # #     Single map hover (used by old tests)
# # #     """
# # #     ActionChains(self.driver).move_to_element(point).pause(1).perform()
#
#
# # # # 🔥 NEW METHOD — CLIENT DEMO SAFE
# # # def hover_multiple_map_circles(self, count=5):
# # #     """
# # #     Hover 4–5 random facility circles
# # #     0.5s gap → realistic demo
# # #     """
# # #     import random
#
# # #     circles = self.wait.until(
# # #         EC.presence_of_all_elements_located(
# # #             (
# # #                 By.XPATH,
# # #                 "//div[contains(@id,'highcharts')]//*[name()='path' and contains(@class,'highcharts-point')]"
# # #             )
# # #         )
# # #     )
#
# # #     if not circles:
# # #         return False
#
# # #     count = min(count, len(circles))
# # #     selected = random.sample(circles, count)
#
# # #     for circle in selected:
# # #         self.driver.execute_script(
# # #             "arguments[0].scrollIntoView({block:'center'});", circle
# # #         )
# # #         ActionChains(self.driver) \
# # #             .move_to_element(circle) \
# # #             .pause(0.5) \
# # #             .perform()
#
# # #     return True
#
#
# #     # =========================================================
# #     # KPI TABLE
# #     # =========================================================
# #     def scroll_to_kpi_table(self):
# #         row = self.wait.until(
# #             EC.visibility_of_element_located(
# #                 (By.XPATH, "//tr[contains(@class,'font-semibold')]")
# #             )
# #         )
# #         self.driver.execute_script(
# #             "arguments[0].scrollIntoView({block:'center'});", row
# #         )
#
# #     def get_all_kpi_facilities(self):
# #         rows = self.wait.until(
# #             EC.presence_of_all_elements_located(
# #                 (By.XPATH, "//tbody//td[1]")
# #             )
# #         )
# #         return [r.text.strip() for r in rows if r.text.strip()]
#
# #     def demo_hover_kpi_table_rows(self, count=5):
# #      facilities = self.get_all_kpi_facilities()
#
# #     if not facilities:
# #         return False
#
# #     count = min(count, len(facilities))
#
# #     for facility in facilities[:count]:
# #         cell = self.wait.until(
# #             EC.visibility_of_element_located(
# #                 (By.XPATH, f"//td[normalize-space()='{facility}']")
# #             )
# #         )
# #         self.driver.execute_script(
# #             "arguments[0].scrollIntoView({block:'center'});", cell
# #         )
# #         ActionChains(self.driver).move_to_element(cell).pause(0.5).perform()
#
# #     return True
#
#
#
#
# #     # def hover_on_kpi_row(self, facility):
# #     #     cell = self.wait.until(
# #     #         EC.visibility_of_element_located(
# #     #             (By.XPATH, f"//td[normalize-space()='{facility}']")
# #     #         )
# #     #     )
# #     #     ActionChains(self.driver).move_to_element(cell).pause(1).perform()
#
#
#
#
# #     # =========================================================
# #     # KPI BAR CHART
# #     # =========================================================
# #     def switch_kpi_view(self, view="barchart"):
# #         dropdown = self.wait.until(
# #             EC.presence_of_element_located(
# #                 (
# #                     By.XPATH,
# #                     "//h2[normalize-space()='Facility KPIs']/following::select[1]"
# #                 )
# #             )
# #         )
# #         Select(dropdown).select_by_value(view)
# #         self.demo_pause(2)
#
# #     # def get_kpi_bars(self):
# #     #     """
# #     #     Return ONLY KPI bar chart bars (scoped to Facility KPIs section)
# #     #     """
# #     #     return self.wait.until(
# #     #         EC.presence_of_all_elements_located(
# #     #             (
# #     #                 By.XPATH,
# #     #                 "//h2[normalize-space()='Facility KPIs']"
# #     #                 "/ancestor::div[contains(@class,'rounded')]"
# #     #                 "//*[name()='path' and contains(@class,'highcharts-point')]"
# #     #             )
# #     #         )
# #     #     )
#
# #     def get_kpi_bars(self):
# #      """
# #     Return ONLY KPI bar chart bars (scoped & stable)
# #      """
# #     # Wait until KPI section is visible (IMPORTANT)
# #     self.wait.until(
# #         EC.visibility_of_element_located(
# #             (By.XPATH, "//h2[normalize-space()='Facility KPIs']")
# #         )
# #     )
#
# #     return self.wait.until(
# #         EC.presence_of_all_elements_located(
# #             (
# #                 By.XPATH,
# #                 "//h2[normalize-space()='Facility KPIs']"
# #                 "/ancestor::div[contains(@class,'rounded')]"
# #                 "//*[name()='path' and contains(@class,'highcharts-point')]"
# #             )
# #         )
# #     )
#
#
# #     # def hover_kpi_bar_by_index(self, index=0):
# #     #     """
# #     #     SAFE KPI bar hover:
# #     #     - isolate KPI chart
# #     #     - scroll into view
# #     #     - re-fetch bars every time
# #     #     """
# #     #     bars = self.get_kpi_bars()
#
# #     #     if not bars or index >= len(bars):
# #     #         return False
#
# #     #     bar = bars[index]
#
# #     #     # Move viewport away from map
# #     #     self.driver.execute_script(
# #     #         "arguments[0].scrollIntoView({block:'center'});", bar
# #     #     )
# #     #     self.demo_pause(1)
#
# #     #     ActionChains(self.driver) \
# #     #         .move_to_element(bar) \
# #     #         .move_by_offset(3, 3) \
# #     #         .pause(1) \
# #     #         .perform()
#
# #     #     return True
#
# #     def hover_kpi_bar_by_index(self, index=0):
# #      """
# #     SAFE KPI bar hover:
# #     - isolate KPI chart
# #     - scroll into view
# #     - re-fetch bars every time
# #      """
# #     bars = self.get_kpi_bars()
#
# #     if not bars or index >= len(bars):
# #         return False
#
# #     bar = bars[index]
#
# #     self.driver.execute_script(
# #         "arguments[0].scrollIntoView({block:'center'});", bar
# #     )
# #     self.demo_pause(0.5)
#
# #     ActionChains(self.driver) \
# #         .move_to_element(bar) \
# #         .move_by_offset(3, 3) \
# #         .pause(0.6) \
# #         .perform()
#
# #     return True
#
#
# #     # =========================================================
# #     # DISTRIBUTOR → FACILITY FLOW (SANKEY)
# #     # =========================================================
# #     def select_distributor_facility(self, value):
# #         dropdown = self.wait.until(
# #             EC.presence_of_element_located(
# #                 (
# #                     By.XPATH,
# #                     "//h2[contains(text(),'Distributor')]/following::select[1]"
# #                 )
# #             )
# #         )
# #         Select(dropdown).select_by_visible_text(value)
# #         self.demo_pause(2)
#
# #     def get_flow_links(self):
# #         return self.driver.find_elements(
# #             By.XPATH, "//*[name()='path' and contains(@class,'highcharts-link')]"
# #         )
#
# #     def hover_flow_links(self):
# #         links = self.get_flow_links()
# #         for link in links[:5]:
# #             ActionChains(self.driver).move_to_element(link).pause(1).perform()
#
# #     # =========================================================
# #     # FACILITY STATUS READINESS SUMMARY
# #     # =========================================================
# #     def select_readiness_view(self, value):
# #         dropdown = self.wait.until(
# #             EC.presence_of_element_located(
# #                 (
# #                     By.XPATH,
# #                     "//h2[contains(text(),'Readiness')]/following::select[1]"
# #                 )
# #             )
# #         )
# #         Select(dropdown).select_by_visible_text(value)
# #         self.demo_pause(2)
#
# #     def get_readiness_bars(self):
# #         return self.wait.until(
# #             EC.presence_of_all_elements_located(
# #                 (
# #                     By.XPATH,
# #                     "//div[contains(text(),'Readiness')]//*[name()='rect']"
# #                 )
# #             )
# #         )
#
# #     def hover_readiness_bars(self):
# #         bars = self.get_readiness_bars()
# #         for bar in bars[:5]:
# #             ActionChains(self.driver).move_to_element(bar).pause(1).perform()
#
# import time
# import random
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# class FacilityStatusPage:
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 40)
#
#     # ================= DOM STABILITY (CRITICAL) =================
#     def wait_for_dom_stability(self, timeout=15):
#         """
#         Wait until:
#         - No DOM mutations
#         - No active fetch / XHR
#         - No running animations
#         """
#         script = """
#         const callback = arguments[arguments.length - 1];
#         let lastMutation = Date.now();
#
#         const observer = new MutationObserver(() => {
#             lastMutation = Date.now();
#         });
#
#         observer.observe(document.body, {
#             childList: true,
#             subtree: true,
#             attributes: true
#         });
#
#         let activeRequests = 0;
#
#         const origFetch = window.fetch;
#         window.fetch = function() {
#             activeRequests++;
#             return origFetch.apply(this, arguments)
#                 .finally(() => activeRequests--);
#         };
#
#         const origOpen = XMLHttpRequest.prototype.open;
#         XMLHttpRequest.prototype.open = function() {
#             activeRequests++;
#             this.addEventListener('loadend', () => activeRequests--);
#             return origOpen.apply(this, arguments);
#         };
#
#         function check() {
#             const now = Date.now();
#             const animationsRunning = document
#                 .getAnimations()
#                 .some(a => a.playState === 'running');
#
#             if (
#                 now - lastMutation > 800 &&
#                 activeRequests === 0 &&
#                 !animationsRunning
#             ) {
#                 observer.disconnect();
#                 callback(true);
#             } else {
#                 setTimeout(check, 200);
#             }
#         }
#         check();
#         """
#         self.driver.execute_async_script(script)
#
#
#     # =========================================================
#     # STRATEGIC OVERVIEW LOAD (MAP SVG = PAGE READY)
#     # =========================================================
#     def verify_map_visible(self):
#         """
#         Verifies that Status of All Facilities map SVG is present
#         """
#         self.wait.until(
#             EC.presence_of_element_located(
#                 (
#                     By.XPATH,
#                     "//h2[normalize-space()='Status of All Facilities']"
#                     "/ancestor::section//*[name()='svg']"
#                 )
#             )
#         )
#         return True
#
#     # =========================================================
#     # SCROLL HELPERS
#     # =========================================================
#     def scroll_to_map_section(self):
#         """
#         Scroll to Status of All Facilities (Map section)
#         """
#         header = self.wait.until(
#             EC.presence_of_element_located(
#                 (By.XPATH, "//h2[normalize-space()='Status of All Facilities']")
#             )
#         )
#         self.driver.execute_script(
#             "arguments[0].scrollIntoView({block:'center'});", header
#         )
#         time.sleep(0.5)
#
#     def scroll_to_kpi_table(self):
#         """
#         Scroll to Facility KPIs table
#         """
#         header = self.wait.until(
#             EC.presence_of_element_located(
#                 (By.XPATH, "//h2[normalize-space()='Facility KPIs']")
#             )
#         )
#         self.driver.execute_script(
#             "arguments[0].scrollIntoView({block:'center'});", header
#         )
#         time.sleep(0.5)
#
#     # =========================================================
#     # KPI CARDS (TOP METRICS)
#     # =========================================================
#     def get_kpi_card_values(self):
#         """
#         Read KPI cards at top (percentage values)
#         """
#         cards = self.wait.until(
#             EC.presence_of_all_elements_located(
#                 (
#                     By.XPATH,
#                     "//div[contains(@class,'relative flex items-center justify-center')]"
#                     "//span[contains(text(),'%')]"
#                 )
#             )
#         )
#
#         values = []
#         for c in cards:
#             text = c.text.strip()
#             if "%" in text:
#                 try:
#                     values.append(float(text.replace("%", "")))
#                 except ValueError:
#                     pass
#
#         return values
#
#     # =========================================================
#     # MAP FUNCTIONS (HIGHCHARTS SVG)
#     # =========================================================
#     def get_facility_map_points(self):
#         """
#         Returns ONLY map circles from Status of All Facilities
#         (scoped to correct container, not bar chart)
#         """
#
#         # Locate map container FIRST
#         map_container = self.wait.until(
#             EC.presence_of_element_located(
#                 (
#                     By.XPATH,
#                     "//h2[normalize-space()='Status of All Facilities']"
#                     "/ancestor::section | "
#                     "//h2[normalize-space()='Status of All Facilities']"
#                     "/ancestor::div"
#                 )
#             )
#         )
#
#         # Now search SVG INSIDE this container only
#         points = map_container.find_elements(
#             By.XPATH,
#             ".//*[name()='svg']//*[name()='path' and contains(@class,'highcharts-point')]"
#         )
#
#         return points
#
#     def hover_on_map_point(self, point):
#         """
#         Hover a single map circle
#         """
#         self.driver.execute_script(
#             "arguments[0].scrollIntoView({block:'center'});", point
#         )
#         ActionChains(self.driver).move_to_element(point).pause(0.5).perform()
#
#     def hover_multiple_map_circles(self, count=5):
#         points = self.get_facility_map_points()
#         for p in points[:count]:
#             self.driver.execute_script(
#                 "arguments[0].scrollIntoView({block:'center'});", p
#             )
#             ActionChains(self.driver).move_to_element(p).pause(0.4).perform()
#         return True
#
#     # =========================================================
#     # KPI TABLE
#     # =========================================================
#     def wait_for_kpis_to_load(self):
#         self.wait.until(
#             EC.presence_of_element_located(
#                 (By.XPATH, "//tbody/tr")
#             )
#         )
#         return True
#
#     def get_all_kpi_values(self):
#         rows = self.wait.until(
#             EC.presence_of_all_elements_located(
#                 (By.XPATH, "//tbody/tr")
#             )
#         )
#
#         values = []
#         for row in rows:
#             cols = row.find_elements(By.TAG_NAME, "td")
#             for col in cols[1:]:  # skip facility name
#                 txt = col.text.strip()
#                 if "%" in txt:
#                     try:
#                         values.append(int(txt.replace("%", "")))
#                     except ValueError:
#                         pass
#
#         return values
#
#     def get_all_kpi_facilities(self):
#         rows = self.wait.until(
#             EC.presence_of_all_elements_located(
#                 (By.XPATH, "//tbody/tr")
#             )
#         )
#
#         facilities = []
#         for row in rows:
#             cols = row.find_elements(By.TAG_NAME, "td")
#             if cols:
#                 facilities.append(cols[0].text.strip())
#
#         return facilities
#     def hover_on_kpi_row(self, facility_name):
#         """
#         Hover a KPI table row by facility name
#         """
#         cell = self.wait.until(
#             EC.visibility_of_element_located(
#                 (By.XPATH, f"//td[normalize-space()='{facility_name}']")
#             )
#         )
#         self.driver.execute_script(
#             "arguments[0].scrollIntoView({block:'center'});", cell
#         )
#         ActionChains(self.driver).move_to_element(cell).pause(0.5).perform()
#
#     # =========================================================
#     # KPI VIEW DROPDOWN (TABLE / BAR CHART)
#     # =========================================================
#     def switch_kpi_view(self, view="table"):
#         """
#         Switch KPI dropdown view
#         values: 'table' or 'barchart'
#         """
#         dropdown = self.wait.until(
#             EC.presence_of_element_located(
#                 (By.XPATH, "//h2[normalize-space()='Facility KPIs']/following::select[1]")
#             )
#         )
#         Select(dropdown).select_by_value(view)
#         time.sleep(1)
#
#     # =========================================================
#     # KPI BAR CHART
#     # =========================================================
#     def get_kpi_bars(self):
#         """
#         Returns ONLY KPI bar chart columns (not map points)
#         """
#         return self.wait.until(
#             EC.presence_of_all_elements_located(
#                 (
#                     By.XPATH,
#                     "//*[name()='svg']"
#                     "//g[contains(@class,'highcharts-column-series')]"
#                     "//path[contains(@class,'highcharts-point')]"
#                 )
#             )
#         )
#
#     def hover_on_kpi_bar(self, bar):
#         self.driver.execute_script(
#             "arguments[0].scrollIntoView({block:'center'});", bar
#         )
#
#         ActionChains(self.driver) \
#             .move_to_element(bar) \
#             .pause(0.2) \
#             .move_by_offset(6, -6) \
#             .pause(0.6) \
#             .perform()
#
#
#
#
#
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class FacilityStatusPage:
    """
    Page Object: Facility Status Tracker – Strategic Overview
    Highcharts-safe implementation (NO infinite waits)
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    # =========================================================
    # ONE-TIME PAGE READY (MAP SVG LOAD)
    # =========================================================
    def wait_for_map_svg_once(self):
        """
        Wait ONLY ONCE for Highcharts map bubbles to exist.
        This must be called immediately after navigation.
        """
        self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "g.highcharts-mapbubble-series path.highcharts-point")
            )
        )
        return True

    # =========================================================
    # SCROLL HELPERS
    # =========================================================
    def scroll_to_map_section(self):
        header = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[normalize-space()='Status of All Facilities']")
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", header
        )
        time.sleep(0.3)

    def scroll_to_kpi_table(self):
        header = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[normalize-space()='Facility KPIs']")
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", header
        )
        time.sleep(0.3)

    # =========================================================
    # KPI CARDS (TOP SUMMARY)
    # =========================================================
    def get_kpi_card_values(self):
        """
        Reads KPI cards at top (80.10%, 12.40%, 7.50%)
        """
        # KPI cards are the BIG % numbers at top
        cards = self.wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    "//div[contains(@class,'rounded-lg')]"
                    "//div[contains(text(),'%')]"
                )
            )
        )

        values = []
        for c in cards:
            txt = c.text.strip()
            if "%" in txt:
                try:
                    values.append(float(txt.replace("%", "")))
                except ValueError:
                    pass

        return values

    # =========================================================
    # MAP → FULFILLMENT RATE ONLY
    # =========================================================
    def get_facility_map_points(self):
        """
        Returns map bubbles ONLY.
        No waits here (already loaded).
        """
        self.scroll_to_map_section()

        return self.driver.find_elements(
            By.CSS_SELECTOR,
            "g.highcharts-mapbubble-series path.highcharts-point"
        )

    def hover_multiple_map_circles(self, count=5):
        points = self.get_facility_map_points()
        assert len(points) > 0, "No map points found"

        for p in points[:count]:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", p
            )
            ActionChains(self.driver).move_to_element(p).pause(0.4).perform()

        return True

    # =========================================================
    # KPI TABLE → MISALLOCATION RATE
    # =========================================================
    def wait_for_kpis_to_load(self):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//tbody/tr"))
        )
        return True

    def get_all_kpi_facilities(self):
        rows = self.driver.find_elements(By.XPATH, "//tbody/tr")

        facilities = []
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if cols:
                facilities.append(cols[0].text.strip())

        return facilities

    def get_misallocation_rate_values(self):
        rows = self.driver.find_elements(By.XPATH, "//tbody/tr")

        values = []
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 3:
                txt = cols[2].text.strip()
                if "%" in txt:
                    try:
                        values.append(float(txt.replace("%", "")))
                    except ValueError:
                        pass
        return values

    def hover_on_kpi_row(self, facility_name):
        cell = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//td[normalize-space()='{facility_name}']")
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", cell
        )
        ActionChains(self.driver).move_to_element(cell).pause(0.4).perform()

    # =========================================================
    # KPI VIEW SWITCH
    # =========================================================
    def switch_kpi_view(self, view="table"):
        """
        view = 'table' or 'barchart'
        """
        dropdown = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[normalize-space()='Facility KPIs']/following::select[1]")
            )
        )
        Select(dropdown).select_by_value(view)
        time.sleep(0.8)

    # =========================================================
    # BAR CHART → REALLOCATION RATE ONLY
    # =========================================================
    def get_bar_chart_columns(self):
        """
        Returns bar chart columns ONLY (Facility Status Readiness Summary)
        """
        # wait only for column-series group (NOT aria-label)
        self.wait.until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "g.highcharts-series.highcharts-column-series"
                )
            )
        )

        bars = self.driver.find_elements(
            By.CSS_SELECTOR,
            "g.highcharts-series.highcharts-column-series path.highcharts-point"
        )

        return bars

    def hover_on_bar(self, bar):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", bar
        )

        ActionChains(self.driver) \
            .move_to_element(bar) \
            .pause(0.3) \
            .move_by_offset(10, -10) \
            .pause(0.5) \
            .perform()
