from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage
from utils.csv_writer import write_test_report
from selenium.webdriver.support.ui import Select
import time


def test_facility_sankey_chart_interaction(driver):
    slider = SliderPage(driver)
    facility = FacilityStatusPage(driver)

    # =========================================================
    # TC-SO-07: Sankey Chart Visibility
    # =========================================================
    slider.click_slider("Part Allocation Insights")
    slider.hover_and_click_facility_status_tracker()

    assert facility.verify_sankey_chart_visible(), "Sankey chart not visible"

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Verify Sankey chart visible",
        "Navigate to Distributor → Facility Flow",
        "Sankey chart should render",
        "Sankey chart rendered",
        "Pass", "", "SO-07", ""
    )

    # =========================================================
    # TC-SO-08: Sankey Hover Interaction (SAFE)
    # =========================================================
    facility.hover_flow_links(count=3)

    links = facility.get_flow_links()
    assert len(links) > 0, "Sankey links not found after hover"

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Verify Sankey hover interaction",
        "Hover Sankey flow links",
        "Flows should be interactive",
        f"{len(links)} Sankey links detected",
        "Pass", "", "SO-08", ""
    )

    # =========================================================
    # TC-SO-09: Sankey Dropdown Interaction (TOP 2 ONLY)
    # =========================================================
    dropdown = facility.get_sankey_dropdown()
    select = Select(dropdown)

    options = select.options
    assert len(options) >= 2, "Not enough Sankey dropdown options"

    for opt in options[:2]:
        select.select_by_visible_text(opt.text)
        time.sleep(1)  # Highcharts redraw

        assert facility.verify_sankey_chart_visible(), \
            f"Sankey not rendered for option: {opt.text}"

        facility.hover_flow_links(count=2)

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Verify Sankey dropdown interaction",
        "Change facility dropdown & hover flows",
        "Sankey should redraw and remain interactive",
        f"{len(options)} dropdown options detected",
        "Pass", "", "SO-09", ""
    )
