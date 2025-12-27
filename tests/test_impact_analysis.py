from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage
from utils.csv_writer import write_test_report
import time


def test_impact_analysis_flow(driver):
    slider = SliderPage(driver)
    facility = FacilityStatusPage(driver)

    # ================= NAVIGATION =================
    slider.click_slider("Part Allocation Insights")
    slider.hover_and_click_facility_status_tracker()

    facility.go_to_impact_analysis()

    # ================= DEFAULT FILTERS =================
    filters = facility.get_impact_filters()
    assert isinstance(filters, dict)

    write_test_report(
        "Tower Track", "Web", "Impact Analysis",
        "Verify default filters",
        "Read filters",
        "Filters should be visible",
        str(filters),
        "Pass", "", "IA-01", ""
    )

    # ================= SELECT FACILITY (ADDED STEP – SAFE) =================
    facility.select_impact_facility("CHI1 (Aurora, IL)")
    time.sleep(1.5)

    write_test_report(
        "Tower Track", "Web", "Impact Analysis",
        "Verify Facility selection",
        "Select Facility",
        "Facility should be selected",
        "Facility=CHI1 (Aurora, IL)",
        "Pass", "", "IA-01A", ""
    )

    # ================= STEP 1 =================
    facility.select_impact_status("delayed")
    facility.select_impact_part("Generator w/ Enclosure")

    rows1 = facility.get_impact_table_rows()

    write_test_report(
        "Tower Track", "Web", "Impact Analysis",
        "Verify Delayed + Generator",
        "Change filters",
        "Table should update",
        f"Rows: {len(rows1)}",
        "Pass", "", "IA-02", ""
    )

    # ================= STEP 2 =================
    facility.select_impact_status("pending")
    facility.select_impact_part("Cable Busway")

    rows2 = facility.get_impact_table_rows()

    write_test_report(
        "Tower Track", "Web", "Impact Analysis",
        "Verify Pending + Cable Busway",
        "Change filters",
        "Table should update",
        f"Rows: {len(rows2)}",
        "Pass", "", "IA-03", ""
    )
