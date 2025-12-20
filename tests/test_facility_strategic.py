from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage
from tests.test_login import login_and_reach_dashboard
from utils.csv_writer import write_test_report, start_new_report
import time


def test_strategic_overview_map_hover():
    start_new_report()

    driver = login_and_reach_dashboard()

    try:
        slider = SliderPage(driver)
        facility_page = FacilityStatusPage(driver)

        # 🔒 EXISTING WORKING FLOW (DO NOT MODIFY)
        slider.click_slider("Part Allocation Insights")
        time.sleep(2)

        slider.hover_and_click_facility_status_tracker()
        time.sleep(2)

        # 🟢 STRATEGIC OVERVIEW
        facility_page.click_strategic_overview()
        facility_page.verify_strategic_overview_loaded()

        # 🗺 MAP HOVER TEST
        facility_page.hover_on_first_facility()

        assert facility_page.is_tooltip_visible()

        write_test_report(
            "Tower Track",
            "Web",
            "Facility Status Tracker",
            "Strategic Overview map hover",
            "Hover on one facility circle",
            "Facility data tooltip should appear",
            "Tooltip appeared successfully",
            "Pass",
            "",
            "SO-MAP-01",
            ""
        )

    finally:
        driver.quit()
