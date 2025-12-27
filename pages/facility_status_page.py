from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.keys import Keys

import time




class FacilityStatusPage:
    """
    Page Object: Facility Status Tracker – Strategic Overview
    Highcharts-safe implementation (NO infinite waits)
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    # =========================================================
    # WINDOW / TAB HANDLING
    # =========================================================
    def wait_for_new_window(self, old_window, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > 1
            )

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
    # SCROLL HELPERS
    # =========================================================
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
    def get_sankey_dropdown(self):
        """
        Returns Sankey chart dropdown (Distributor selector)
        """
        return self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='flex items-center gap-2 mr-2']//select"
                )
            )
        )

    #
    # ================= FACILITY STATUS READINESS SUMMARY =================

    def verify_readiness_chart_visible(self):
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(),'Readiness')]")
            )
        )
        return True

    from selenium.webdriver.common.keys import Keys

    def select_readiness_viewpoint(self, view):
        """
        React-safe select change (forces onChange to fire)
        """

        value_map = {
            "Facility": "facility",
            "Resource": "resource",
            "Transportation": "transportation",
            "Alert": "alert",
        }

        select_el = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//select[contains(@class,'w-56')]")
            )
        )

        # 🔥 Force React onChange
        self.driver.execute_script(
            """
            const select = arguments[0];
            select.value = arguments[1];
            select.dispatchEvent(new Event('change', { bubbles: true }));
            """,
            select_el,
            value_map[view]
        )

        # ✅ Wait until Transportation panel renders
        if view == "Transportation":
            self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//h2[normalize-space()='Transportation Dependency Readiness Summary']"
                    )
                )
            )

        return True

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

    def select_transportation_facility(self, facility_name="PHX1"):
        select_el = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[normalize-space()='Facility:']/following-sibling::select")
            )
        )

        Select(select_el).select_by_visible_text(facility_name)
        time.sleep(2)

    def select_transportation_phase(self, phase_name="Phase B"):
        select_el = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[normalize-space()='Phase:']/following-sibling::select")
            )
        )

        Select(select_el).select_by_visible_text(phase_name)
        time.sleep(2)

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

    def close_child_and_return(self, parent_window):
        current = self.driver.current_window_handle

        if current != parent_window:
            self.driver.close()

        self.driver.switch_to.window(parent_window)
        time.sleep(1.5)

        print("✅ Part Dependency Graph tab closed and returned to parent")

    # ================= PART DEPENDENCY GRAPH =================

    def close_child_and_return(self, parent_window):
        current = self.driver.current_window_handle

        if current != parent_window:
            self.driver.close()

        self.driver.switch_to.window(parent_window)
        time.sleep(1.5)

        print("✅ Part Dependency Graph tab closed and returned to parent")

        # Navigate to Impact Analysis tab

    def go_to_impact_analysis(self):
        tab = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Impact Analysis']")
            )
        )
        tab.click()
        time.sleep(1.5)

        print("✅ Navigated to Impact Analysis")

    def get_impact_filters(self):
        filters = {}

        try:
            status = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//label[contains(text(),'Status')]/following::select[1]")
                )
            )
            filters["status"] = Select(status).first_selected_option.text.strip()
        except:
            filters["status"] = None

        try:
            part = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//label[contains(text(),'Part')]/following::select[1]")
                )
            )
            filters["part"] = Select(part).first_selected_option.text.strip()
        except:
            filters["part"] = None

        return filters

    def select_impact_status(self, value):
        dropdown = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[contains(text(),'Status')]/following::select[1]")
            )
        )
        Select(dropdown).select_by_value(value)
        time.sleep(1)
        print(f"✅ Impact Status selected: {value}")

    def select_impact_part(self, part_name):
        dropdown = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[contains(text(),'Part')]/following::select[1]")
            )
        )
        Select(dropdown).select_by_visible_text(part_name)
        time.sleep(1)
        print(f"✅ Impact Part selected: {part_name}")

    def get_impact_table_rows(self):
        time.sleep(1)

        rows = self.driver.find_elements(
            By.XPATH, "//h3[contains(text(),'Impact')]/following::tbody/tr"
        )

        print(f"ℹ️ Impact rows: {len(rows)}")
        return rows

    # ================= IMPACT ANALYSIS → ALLOCATION RECOMMENDATION =================

    def go_to_impact_analysis(self):
        """
        Explicitly switch to Impact Analysis tab (React-safe)
        """

        impact_tab = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Impact Analysis']")
            )
        )

        # React-safe click
        self.driver.execute_script(
            "arguments[0].click();", impact_tab
        )

        # ✅ Wait until Impact Analysis content appears
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h2[contains(text(),'Allocation Recommendation')]")
            )
        )

        print("✅ Switched to Impact Analysis tab")
        return True

    def select_impact_facility(self, facility_name):
        """
        Select Facility dropdown
        """
        dropdown = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[normalize-space()='Select Facility:']/following-sibling::select")
            )
        )
        Select(dropdown).select_by_visible_text(facility_name)
        time.sleep(1.5)
        print(f"✅ Impact Facility selected: {facility_name}")

    def select_impact_start_date(self, date_value):
        """
        date_value format: YYYY-MM-DD
        """
        start_date = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[normalize-space()='Start Date:']/following-sibling::input")
            )
        )
        start_date.clear()
        start_date.send_keys(date_value)
        time.sleep(1)
        print(f"✅ Start Date selected: {date_value}")

    def select_impact_end_date(self, date_value):
        """
        date_value format: YYYY-MM-DD
        """
        end_date = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[normalize-space()='End Date:']/following-sibling::input")
            )
        )
        end_date.clear()
        end_date.send_keys(date_value)
        time.sleep(1)
        print(f"✅ End Date selected: {date_value}")

    def click_get_recommendation(self):
        """
        Click Get Recommendation button
        """
        btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Get Recommendation']")
            )
        )
        btn.click()
        time.sleep(3)
        print("✅ Get Recommendation clicked")




