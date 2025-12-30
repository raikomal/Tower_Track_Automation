from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class FacilityStatusPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    # =========================================================
    # IMPACT ANALYSIS TAB
    # =========================================================
    # Script_ID:36
    def go_to_impact_analysis(self):
        tab = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Impact Analysis']")
            )
        )
        tab.click()

        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[normalize-space()='Allocation Recommendation']")
            )
        )

        print("✅ Impact Analysis page loaded")
        return True

    # =========================================================
    # FILTERS
    # =========================================================
    # Script_ID:37
    def get_impact_filters(self):
        filters = {}

        try:
            facility = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//select[contains(@class,'rounded-md')]")
                )
            )
            filters["facility"] = Select(facility).first_selected_option.text.strip()
        except:
            filters["facility"] = ""

        try:
            filters["start_date"] = self.driver.find_element(
                By.XPATH, "//label[contains(text(),'Start Date')]/following::input[1]"
            ).get_attribute("value")
        except:
            filters["start_date"] = ""

        try:
            filters["end_date"] = self.driver.find_element(
                By.XPATH, "//label[contains(text(),'End Date')]/following::input[1]"
            ).get_attribute("value")
        except:
            filters["end_date"] = ""

        print(f"ℹ️ Impact Filters: {filters}")
        return filters

    def select_impact_facility(self, facility_name):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//select[contains(@class,'rounded-md')]")
            )
        )
        Select(dropdown).select_by_visible_text(facility_name)
        print(f"✅ Facility selected: {facility_name}")

    def select_impact_start_date(self, value):
        el = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[contains(text(),'Start Date')]/following::input[1]")
            )
        )
        el.clear()
        el.send_keys(value)

    def select_impact_end_date(self, value):
        el = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[contains(text(),'End Date')]/following::input[1]")
            )
        )
        el.clear()
        el.send_keys(value)

    # Script_ID:38
    def click_get_recommendation(self):
        btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Get Recommendation']")
            )
        )
        btn.click()
        print("✅ Recommendation requested")

    # Script_ID:39
    def wait_for_recommendation_to_finish(self, timeout=20):
        """
        SAFE wait:
        Recommendation is complete when cost charts (Highcharts) appear
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//*[name()='svg' and ancestor::div[contains(@class,'highcharts')]]"
                    )
                )
            )
            print("✅ Recommendation backend processing finished")
            return True
        except:
            print("⚠️ Recommendation finished but charts not detected (non-blocking)")
            return False

    # =========================================================
    # MODIFY ALLOCATION + COST
    # =========================================================
    # Script_ID:40
    def modify_allocation_and_compute_cost(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Modify Allocation']")
            )
        ).click()

        values = ["20", "50", "70"]
        cells = [
            "//tbody/tr[1]/td[3]",
            "//tbody/tr[2]/td[3]",
            "//tbody/tr[3]/td[3]"
        ]

        for xp, val in zip(cells, values):
            cell = self.wait.until(EC.presence_of_element_located((By.XPATH, xp)))
            self.driver.execute_script("""
                arguments[0].innerText='';
                arguments[0].innerText=arguments[1];
                arguments[0].dispatchEvent(new Event('input',{bubbles:true}));
            """, cell, val)
        # Script_ID:41
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Compute Cost Impact']")
            )
        ).click()

        self.hover_cost_graphs()

    # Script_ID:42
    def hover_cost_graphs(self):
        svgs = self.driver.find_elements(
            By.XPATH, "//*[name()='svg' and ancestor::div[contains(@class,'highcharts')]]"
        )

        for svg in svgs:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", svg)
            ActionChains(self.driver).move_to_element(svg).pause(0.3).perform()

        print("✅ Cost graphs hovered")

    # =========================================================
    # SIMULATION PLANNING TOOL (SAFE)
    # =========================================================
    def simulation_tool_ready(self, timeout=20):
        """
        Simulation tool is READY only when Part dropdown has real options
        """
        try:
            part_select = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//label[contains(text(),'Part')]/following::select[1]")
                )
            )

            WebDriverWait(self.driver, timeout).until(
                lambda d: len(Select(part_select).options) > 1
            )

            parts = [
                o.text.strip()
                for o in Select(part_select).options
                if o.text.strip() and "Select" not in o.text
            ]

            print(f"✅ Simulation Tool READY (Parts loaded: {parts})")
            return True

        except Exception as e:
            print(f"❌ Simulation Tool not ready: {e}")
            return False

    def run_simulation_planning_flow(self):
        """
        Full Simulation Planning Tool flow:
        Select Source, Destination, Part, Quantity
        Click Simulate
        Hover Simulation graph
        """

        # Ensure Simulation section is visible
        sim_header = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h3[normalize-space()='Simulation Planning Tool']")
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", sim_header
        )
        time.sleep(1)

        # ---------------- Source Facility ----------------
        source = Select(
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//label[contains(text(),'Source Facility')]/following::select[1]")
                )
            )
        )
        source.select_by_visible_text("PHX1 (Chandler, AZ)")
        time.sleep(0.8)

        # ---------------- Destination Facility ----------------
        dest = Select(
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//label[contains(text(),'Destination Facility')]/following::select[1]")
                )
            )
        )
        dest.select_by_visible_text("PHX2 (Chandler, AZ)")
        time.sleep(0.8)

        # ---------------- Part ----------------
        part = Select(
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//label[contains(text(),'Part')]/following::select[1]")
                )
            )
        )
        part.select_by_visible_text("Generator")
        time.sleep(0.8)

        # ---------------- Quantity ----------------
        qty = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[contains(text(),'Quantity')]/following::input[1]")
            )
        )
        qty.clear()
        qty.send_keys("50")
        time.sleep(0.5)

        # ---------------- Simulate Button ----------------
        simulate_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Simulate')]")
            )
        )
        simulate_btn.click()
        print("✅ Simulation Reallocation clicked")

        # ---------------- WAIT FOR SIMULATION GRAPH ----------------
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[name()='svg' and ancestor::div[contains(text(),'Reallocation Cost Impact')]]")
            )
        )

        # ---------------- HOVER SIMULATION GRAPH ----------------
        svgs = self.driver.find_elements(
            By.XPATH,
            "//*[name()='svg' and ancestor::div[contains(text(),'Reallocation Cost Impact')]]"
        )

        for svg in svgs:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", svg
            )
            ActionChains(self.driver).move_to_element(svg).pause(0.6).perform()

        print("✅ Simulation graph hovered successfully")
        return True

    # =========================================================
    # WINDOW / TAB HANDLING
    # =========================================================
    def wait_for_new_window(self, old_window, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > 1
            )

    def run_simulation_planning_flow_safe(self):
        """
        Run simulation with safest possible inputs
        """
        try:
            Select(
                self.wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//label[contains(text(),'Source Facility')]/following::select[1]")
                    )
                )
            ).select_by_index(1)

            Select(
                self.wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//label[contains(text(),'Destination Facility')]/following::select[1]")
                    )
                )
            ).select_by_index(1)

            part_select = Select(
                self.wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//label[contains(text(),'Part')]/following::select[1]")
                    )
                )
            )
            part_select.select_by_index(1)

            qty = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//label[contains(text(),'Quantity')]/following::input[1]")
                )
            )
            qty.clear()
            qty.send_keys("20")

            self.driver.find_element(
                By.XPATH, "//button[contains(text(),'Simulate')]"
            ).click()

            print("✅ Simulation Reallocation triggered")
            time.sleep(3)
            return True

        except Exception as e:
            print(f"❌ Simulation execution failed: {e}")
            return False

    def hover_simulation_cost_graphs(self):
        """
        Hover Highcharts graph under 'Reallocation Cost Impact'
        """
        try:
            header = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//h3[contains(text(),'Reallocation Cost Impact')]")
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", header
            )

            WebDriverWait(self.driver, 20).until(
                lambda d: len(
                    d.find_elements(
                        By.XPATH,
                        "//h3[contains(text(),'Reallocation Cost Impact')]"
                        "/following::svg[1]//*[name()='path']"
                    )
                ) > 0
            )

            bars = self.driver.find_elements(
                By.XPATH,
                "//h3[contains(text(),'Reallocation Cost Impact')]"
                "/following::svg[1]//*[name()='path']"
            )

            for bar in bars:
                ActionChains(self.driver).move_to_element(bar).pause(0.4).perform()

            print("✅ Simulation graph hovered")
            return True

        except Exception as e:
            print(f"⚠️ No simulation graphs found to hover: {e}")
            return False

    # =========================================================
    # ONE-TIME PAGE READY (MAP SVG LOAD)
    # =========================================================
    def wait_for_map_svg_once(self):
        """
        Wait ONLY ONCE for Highcharts map bubbles to exist.
        Call immediately after navigation.
        """
        self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,
                 "g.highcharts-mapbubble-series path.highcharts-point")
            )
        )
        return True

    # =========================================================
    # STRATEGIC OVERVIEW – FULL PAGE READY CHECK
    # =========================================================
    # Script_ID:9
    def verify_strategic_overview_loaded(self):
        """
        Verify Strategic Overview page is fully loaded.
        Used by Strategic Overview flow + E2E flow.
        """
        # Script_ID:10
        # 1️⃣ Page header check
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[normalize-space()='Status of All Facilities']")
            )
        )
        # Script_ID:11
        # 2️⃣ Highcharts map bubbles (true readiness signal)
        self.wait.until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "g.highcharts-mapbubble-series path.highcharts-point"
                )
            )
        )

        print("✅ Strategic Overview loaded successfully")
        return True


    # =========================================================
    # SCROLL HELPERS
    # =========================================================
    # Script_ID:12
    def scroll_to_map_section(self):
        header = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "//h2[normalize-space()='Status of All Facilities']")
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            header
        )
        time.sleep(0.3)

    def scroll_to_simulation_section(self):
        """
        SAFE scroll – simulation tool may or may not exist
        """
        headers = self.driver.find_elements(
            By.XPATH, "//h3[contains(text(),'Simulation Planning Tool')]"
        )

        if not headers:
            print("ℹ️ Simulation Planning Tool not rendered (valid backend state)")
            return False

        header = headers[0]
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", header
        )
        time.sleep(1)
        return True

    # Script_ID:16
    def scroll_to_kpi_table(self):
        header = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "//h2[normalize-space()='Facility KPIs']")
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            header
        )
        time.sleep(0.5)

    # =========================================================
    # KPI CARDS (TOP SUMMARY)
    # =========================================================
    def get_kpi_card_values(self):
        """
        Reads KPI cards at top (80.10%, 12.40%, 7.50%)
        """
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
        for card in cards:
            txt = card.text.strip()
            if "%" in txt:
                try:
                    values.append(float(txt.replace("%", "")))
                except ValueError:
                    pass

        return values

    # =========================================================
    # MAP → FULFILLMENT RATE
    # =========================================================
    def get_facility_map_points(self):
        """
        Returns map bubbles ONLY.
        """
        self.scroll_to_map_section()

        return self.driver.find_elements(
            By.CSS_SELECTOR,
            "g.highcharts-mapbubble-series path.highcharts-point"
        )

    def hover_multiple_map_circles(self, count=5):
        points = self.get_facility_map_points()
        assert len(points) > 0, "No map points found"

        for point in points[:count]:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                point
            )
            ActionChains(self.driver)\
                .move_to_element(point)\
                .pause(0.4)\
                .perform()

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
            "arguments[0].scrollIntoView({block:'center'});",
            cell
        )
        ActionChains(self.driver)\
            .move_to_element(cell)\
            .pause(0.4)\
            .perform()

    # =========================================================
    # KPI VIEW SWITCH
    # =========================================================
    # Script_ID:13
    def switch_kpi_view(self, view="table"):
        """
        view = 'table' or 'barchart'
        """
        dropdown = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "//h2[normalize-space()='Facility KPIs']/following::select[1]")
            )
        )
        Select(dropdown).select_by_value(view)
        time.sleep(0.8)

    # =========================================================
    # BAR CHART → REALLOCATION RATE
    # =========================================================
    # Script_ID:14
    def get_bar_chart_columns(self):
        self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,
                 "g.highcharts-series.highcharts-column-series")
            )
        )

        return self.driver.find_elements(
            By.CSS_SELECTOR,
            "g.highcharts-series.highcharts-column-series "
            "path.highcharts-point"
        )

    # Script_ID:15
    def hover_on_bar(self, bar):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            bar
        )

        ActionChains(self.driver)\
            .move_to_element(bar)\
            .pause(0.3)\
            .move_by_offset(10, -10)\
            .pause(0.5)\
            .perform()

    # =========================================================
    # =========================================================
    # SANKEY CHART (SAFE VERSION)
    # =========================================================

    def hover_flow_links(self, count=5):
        """
        Hover over Sankey flow links (Highcharts path elements)
        """
        links = self.get_flow_links()
        count = min(count, len(links))

        for link in links[:count]:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", link
            )
            ActionChains(self.driver) \
                .move_to_element(link) \
                .pause(0.5) \
                .perform()

        return True

    # Script_ID:17
    def verify_sankey_chart_visible(self):
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[name()='path' and contains(@class,'highcharts-link')]")
            )
        )
        return True

    def get_flow_links(self):
        return self.driver.find_elements(
            By.XPATH,
            "//*[name()='path' and contains(@class,'highcharts-link')]"
        )

    def hover_single_flow_link(self):
        links = self.get_flow_links()
        assert links, "No Sankey links found"

        link = links[0]
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", link
        )
        ActionChains(self.driver).move_to_element(link).pause(0.6).perform()

    # Script_ID:20
    def get_sankey_tooltip_text(self):
        tooltips = self.driver.find_elements(
            By.XPATH,
            "//*[name()='g' and contains(@class,'highcharts-tooltip')]//*[name()='text']"
        )
        return " ".join(t.text.strip() for t in tooltips if t.text.strip())

    def validate_sankey_tooltip_structure(self, tooltip_text: str):
        """
        Valid Sankey tooltip can be:
        - Node tooltip (label only)
        - OR Link tooltip (source → target with value)
        """
        if not tooltip_text:
            return False

        has_text = any(char.isalpha() for char in tooltip_text)
        has_number = any(char.isdigit() for char in tooltip_text)
        has_arrow = "→" in tooltip_text or "to" in tooltip_text.lower()

        # Accept node OR link tooltip
        return has_text and (has_number or has_arrow)

    # Script_ID:1
    def hover_multiple_sankey_links(self, count=5):
        links = self.get_flow_links()
        hovered = 0

        for link in links[:count]:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", link
            )
            ActionChains(self.driver).move_to_element(link).pause(0.4).perform()
            hovered += 1

        return hovered

    def sankey_tooltip_has_non_zero_value(self, tooltip_text):
        numbers = []
        for part in tooltip_text.replace(",", "").split():
            try:
                numbers.append(float(part))
            except ValueError:
                pass
        return any(n > 0 for n in numbers)

    # =========================================================
    # SANKEY DROPDOWN (Distributor → Facility Flow)
    # =========================================================
    # Script_ID:18
    def change_sankey_flow_view(self, visible_text=None):
        """
        Change Sankey dropdown (Distributor → Facility flow)
        React-safe + waits for re-render
        """

        dropdown = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(@class,'items-center')]//select"
                )
            )
        )

        select = Select(dropdown)
        # Script_ID:19
        # Pick second option by default if none provided
        if visible_text:
            select.select_by_visible_text(visible_text)
        else:
            if len(select.options) < 2:
                print("⚠️ Sankey dropdown has only one option")
                return False
            select.select_by_index(1)

        # 🔥 Force React redraw
        self.driver.execute_script(
            """
            arguments[0].dispatchEvent(
                new Event('change', { bubbles: true })
            );
            """,
            dropdown
        )

        # ✅ WAIT for Sankey SVG to update
        self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//*[name()='svg']//*[name()='path' and contains(@class,'highcharts-point')]"
                )
            )
        )

        print("✅ Sankey dropdown changed and flow updated")
        return True

    # ================= FACILITY STATUS READINESS SUMMARY =================
    # Script_ID:21
    def verify_readiness_chart_visible(self):
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Readiness')]")
            )
        )
        return True

    def select_readiness_viewpoint(self, view):
        """
        Switch Readiness dropdown (Facility / Resource / Alert / Transportation)
        SAME PAGE – React state change
        """

        value_map = {
            "Facility": "facility",
            "Resource": "resource",
            "Alert": "alert",
            "Transportation": "transportation",
        }
        # Script_ID:22

        # ✅ EXACT Readiness dropdown (anchored to Readiness header)
        select_el = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//h2[contains(text(),'Readiness')]/following::select[1]"
                )
            )
        )

        # 🔥 React-safe change
        self.driver.execute_script(
            """
            const select = arguments[0];
            select.value = arguments[1];
            select.dispatchEvent(new Event('input', { bubbles: true }));
            select.dispatchEvent(new Event('change', { bubbles: true }));
            """,
            select_el,
            value_map[view]
        )

        print(f"✅ Readiness switched to {view}")
        return True

    # Script_ID:20
    def verify_transportation_readiness_loaded(self):
        """
        Verifies Transportation readiness view
        (same page, NOT new tab)
        """
        self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//h2[normalize-space()='Transportation Dependency Readiness Summary']"
                )
            )
        )

        print("✅ Transportation readiness section loaded")
        return True

    # Script_ID:23
    def hover_readiness_bars(self):
        """
        Hover ONLY readiness bars (Facility ViewPoint only)
        """

        bars = self.wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    "//*[name()='path' and contains(@class,'highcharts-point') "
                    "and contains(@aria-label,'Readiness Score')]"
                )
            )
        )

        assert len(bars) > 0, "No readiness bars found (Facility ViewPoint)"

        for bar in bars[:5]:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", bar
            )
            ActionChains(self.driver).move_to_element(bar).pause(0.4).perform()

        return True

    # Script_ID:24

    def click_transportation_arrow(self):
        """
        Click MdArrowOutward and switch to new tab
        """

        parent = self.driver.current_window_handle

        arrow_svg = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//h2[contains(text(),'Transportation Dependency')]"
                    "/following-sibling::div//*[name()='svg']"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", arrow_svg
        )

        self.driver.execute_script(
            "arguments[0].dispatchEvent(new MouseEvent('click',{bubbles:true}));",
            arrow_svg
        )

        # 🔑 WAIT FOR NEW TAB
        self.wait.until(lambda d: len(d.window_handles) > 1)

        # 🔑 SWITCH TO NEW TAB
        for handle in self.driver.window_handles:
            if handle != parent:
                self.driver.switch_to.window(handle)
                break

        return True

    # Script_ID:26
    def verify_transportation_view_page_loaded(self):
        """
        New-tab-safe verification
        """

        # Wait for routing
        self.wait.until(lambda d: "transportation_view" in d.current_url)

        # Wait for DOM ready
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        # Buffer for heavy SVG
        time.sleep(2)

        return True

    # Script_ID:27
    def select_transportation_facility(self, facility_name="PHX1"):
        select_el = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[normalize-space()='Facility:']/following-sibling::select")
            )
        )

        Select(select_el).select_by_visible_text(facility_name)
        time.sleep(2)

    # Script_ID:27
    def select_transportation_phase(self, phase_name="Phase B"):
        select_el = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[normalize-space()='Phase:']/following-sibling::select")
            )
        )

        Select(select_el).select_by_visible_text(phase_name)
        time.sleep(2)

    # Script_ID:28
    def remove_part_category(self, category_name="Other"):
        """
        Remove a Part Category chip if present (safe, non-blocking)
        """

        time.sleep(1.5)  # allow chips to render after phase change

        chips = self.driver.find_elements(
            By.XPATH,
            f"//span[normalize-space()='{category_name}']/ancestor::div[contains(@class,'flex')]"
        )

        # If category is not present, do nothing (important)
        if not chips:
            print(f"ℹ️ Part Category '{category_name}' not present, skipping removal")
            return True

        chip = chips[0]

        # Find SVG inside the chip
        cross_icons = chip.find_elements(By.XPATH, ".//*[name()='svg']")

        if not cross_icons:
            print(f"⚠️ No remove icon found for '{category_name}', skipping")
            return True

        cross = cross_icons[0]

        # Scroll + JS click (SVG-safe)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", cross
        )

        self.driver.execute_script(
            """
            arguments[0].dispatchEvent(
                new MouseEvent('click', { bubbles: true, cancelable: true })
            );
            """,
            cross
        )

        time.sleep(1.5)  # allow UI update

        print(f"✅ Removed Part Category '{category_name}'")
        return True

    def scroll_to_dependency_graph(self):
        header = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h1[normalize-space()='Dependency Graph']")
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", header
        )
        time.sleep(1.5)

    # Script_ID:29
    def change_dependency_graph_view_slowly(self):
        dropdown = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h1[normalize-space()='Dependency Graph']/following::select[1]")
            )
        )

        select = Select(dropdown)

        for option in select.options:
            select.select_by_visible_text(option.text)
            time.sleep(2.5)  # 👀 human-visible

    def get_transportation_top_summary(self):
        """
        Reads top summary values on Transportation View
        """

        summary = {}

        summary["facility"] = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[contains(text(),'Facility')]/following::div[1]")
            )
        ).text.strip()

        summary["phase"] = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[contains(text(),'Phase')]/following::div[1]")
            )
        ).text.strip()

        summary["completeness"] = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(),'Completeness')]/following::div[1]")
            )
        ).text.strip()

        summary["dependency_violations"] = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(),'Dependency Violations')]/following::div[1]")
            )
        ).text.strip()

        summary["transportation_ready"] = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(),'Transportation Ready')]/following::span[1]")
            )
        ).text.strip()

        return summary

    def get_required_parts_table(self):
        """
        SAFE: Required Parts may or may not exist
        """

        time.sleep(2)

        headers = self.driver.find_elements(
            By.XPATH, "//h3[contains(text(),'Required Parts')]"
        )

        # Section not present → valid business state
        if not headers:
            print("ℹ️ Required Parts section not present")
            return []

        header = headers[0]
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", header
        )

        time.sleep(2)

        rows = self.driver.find_elements(
            By.XPATH,
            "//h3[contains(text(),'Required Parts')]/following::tbody/tr"
        )

        data = []
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 4:
                data.append({
                    "part_id": cols[1].text.strip(),
                    "qty_required": cols[2].text.strip(),
                    "arrival": cols[3].text.strip(),
                    "category": cols[4].text.strip() if len(cols) > 4 else ""
                })

        print(f"ℹ️ Required Parts rows: {len(data)}")
        return data

    def get_dependency_status_table(self):
        """
        SAFE: Dependency Status table may or may not exist
        """

        time.sleep(2)

        headers = self.driver.find_elements(
            By.XPATH, "//h3[contains(text(),'Dependency Status')]"
        )

        #  Table not present = valid business case
        if not headers:
            print("Dependency Status section not present")
            return []

        rows = self.driver.find_elements(
            By.XPATH,
            "//h3[contains(text(),'Dependency Status')]/following::tbody/tr"
        )

        data = []
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 4:
                data.append({
                    "dependency": cols[1].text.strip(),
                    "prereq_arrival": cols[2].text.strip(),
                    "dep_arrival": cols[3].text.strip(),
                    "status": cols[4].text.strip() if len(cols) > 4 else ""
                })

        print(f" Dependency Status rows: {len(data)}")
        return data

    def get_transportation_facility(self):
        """
        Read selected Facility value
        """
        select_el = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[normalize-space()='Facility:']/following-sibling::select")
            )
        )
        return Select(select_el).first_selected_option.text.strip()

    def get_transportation_phase(self):
        """
        Read selected Phase value
        """
        select_el = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[normalize-space()='Phase:']/following-sibling::select")
            )
        )
        return Select(select_el).first_selected_option.text.strip()

    def get_transportation_part_categories(self):
        """
        Read selected Part Category chips
        """

        container = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[normalize-space()='Part Category:']/following-sibling::div"
                )
            )
        )

        chips = container.find_elements(By.XPATH, ".//div[contains(@class,'rounded')]")

        return [chip.text.strip() for chip in chips if chip.text.strip()]
    #operational insights Tab
    # Script_ID:30
    def go_to_operational_insights(self):
        tab = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Operational Insights']")
            )
        )
        tab.click()

        # Wait for Operational Insights header
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[contains(text(),'Part Demand And Allocation Status')]")
            )
        )

        time.sleep(1.5)
        return True

    # Script_ID:31
    def get_operational_filters(self):
        return {
            "status": Select(
                self.wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//label[normalize-space()='Status:']/following-sibling::select")
                    )
                )
            ).first_selected_option.text.strip(),

            "part": Select(
                self.wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//label[normalize-space()='Part ID:']/following-sibling::select")
                    )
                )
            ).first_selected_option.text.strip(),

            "facility": Select(
                self.wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//label[normalize-space()='Facility ID:']/following-sibling::select")
                    )
                )
            ).first_selected_option.text.strip()
        }

    # Script_ID:32
    def get_operational_allocation_table(self):
        rows = self.driver.find_elements(
            By.XPATH, "//table//tbody/tr"
        )

        data = []
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 5:
                data.append({
                    "part": cols[0].text.strip(),
                    "facility": cols[1].text.strip(),
                    "qty": cols[2].text.strip(),
                    "time": cols[3].text.strip(),
                    "status": cols[4].text.strip()
                })

        print(f"ℹ️ Allocation rows: {len(data)}")
        return data

    # Script_ID:33
    def get_part_inventory_details(self):
        labels = self.driver.find_elements(
            By.XPATH, "//div[contains(text(),'Part Inventory Details')]"
        )

        if not labels:
            print("ℹ️ Inventory details not present")
            return {}

        container = labels[0].find_element(
            By.XPATH, "./ancestor::div[contains(@class,'rounded')]"
        )

        texts = container.text.splitlines()
        return {t.split(":")[0]: t.split(":")[1].strip() for t in texts if ":" in t}

    def select_operational_status(self, value):
        """
        value = delayed | pending | fulfilled
        """
        select_el = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[normalize-space()='Status:']/following-sibling::select")
            )
        )

        self.driver.execute_script(
            """
            const select = arguments[0];
            select.value = arguments[1];
            select.dispatchEvent(new Event('change', { bubbles: true }));
            """,
            select_el,
            value
        )

        time.sleep(2.5)  # 👀 human visible
        print(f"✅ Status changed to {value}")

    def select_operational_part(self, value):
        """
        value = CRAH Stands | Floor Tiles - 32%
        """
        select_el = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[normalize-space()='Part ID:']/following-sibling::select")
            )
        )

        self.driver.execute_script(
            """
            const select = arguments[0];
            select.value = arguments[1];
            select.dispatchEvent(new Event('change', { bubbles: true }));
            """,
            select_el,
            value
        )

        time.sleep(2.5)  # 👀 human visible
        print(f"✅ Part selected: {value}")
    #tab location navigation in the operational insights
    # Script_ID:34
    def open_part_dependency_graph_tab(self):
        """
        Click Part Dependency Graph arrow (Operational Insights)
        and switch to new tab
        """

        parent = self.driver.current_window_handle

        # 🔥 Locate arrow RELATIVE to heading text
        arrow = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//h2[normalize-space()='Part Dependency Graph']"
                    "/ancestor::div[contains(@class,'flex')]"
                    "//*[name()='svg']"
                )
            )
        )

        # Scroll into view
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", arrow
        )
        time.sleep(0.5)

        # 🔥 JS click (React-safe)
        self.driver.execute_script(
            "arguments[0].dispatchEvent(new MouseEvent('click',{bubbles:true}));",
            arrow
        )

        # 🔑 wait for new tab
        self.wait.until(lambda d: len(d.window_handles) > 1)

        # 🔑 switch to new tab
        for handle in self.driver.window_handles:
            if handle != parent:
                self.driver.switch_to.window(handle)
                break

        print("✅ Part Dependency Graph opened in new tab")
        return parent

    # Script_ID:35
    def select_first_three_dependency_options(self):
        """
        Select only the required 3 options in Part Dependency Graph dropdown
        (Operational Insights → new tab)
        """

        dropdown = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//h1[normalize-space()='Part Dependency Graph']/following::select[1]"
                )
            )
        )
        time.sleep(1)
        select = Select(dropdown)

        values_to_select = [
            "Big Box LV Switchgear",
            "Generator w/ Enclosure",
            "UPS Cabinets & Batteries - 1500kW"
        ]

        for value in values_to_select:
            select.select_by_visible_text(value)
            time.sleep(2)  # human-visible delay

        print("✅ Selected required dependency options")


    # ================= PART DEPENDENCY GRAPH =================

    def close_child_and_return(self, parent_window):
        current = self.driver.current_window_handle

        if current != parent_window:
            self.driver.close()

        self.driver.switch_to.window(parent_window)
        time.sleep(1.5)

        print("✅ Part Dependency Graph tab closed and returned to parent")

        # Navigate to Impact Analysis tab
