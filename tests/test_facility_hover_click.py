from pages.slider_page import SliderPage
from tests.test_login import login_and_reach_dashboard
import time


def test_hover_and_click_facility_status_tracker():
    driver = login_and_reach_dashboard()

    try:
        slider = SliderPage(driver)

        # Step 1: Click Part Allocation Insights (existing working behavior)
        slider.click_slider("Part Allocation Insights")
        time.sleep(2)

        # Step 2: Hover + visible pause + click Facility Status Tracker
        slider.hover_and_click_facility_status_tracker()
        time.sleep(3)   # 👀 let page open clearly

        # STOP HERE – NO ASSERTIONS
        print("✅ Facility Status Tracker hover and click executed")

    finally:
        driver.quit()
