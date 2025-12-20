from pages.slider_page import SliderPage
from tests.test_login import login_and_reach_dashboard

def test_facility_status_tracker_navigation():
    driver = login_and_reach_dashboard()

    try:
        slider = SliderPage(driver)

        slider.click_slider("Part Allocation Insights")
        slider.hover_and_click_facility_status_tracker()

        assert "facility" in driver.current_url.lower()
    finally:
        driver.quit()
