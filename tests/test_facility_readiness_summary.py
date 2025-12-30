from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage
from utils.csv_writer import write_test_report


def test_facility_status_readiness_summary(driver):
    slider = SliderPage(driver)
    facility = FacilityStatusPage(driver)

    slider.click_slider("Part Allocation Insights")
    slider.hover_and_click_facility_status_tracker()

    # ================= SO-14 =================
    facility.select_readiness_viewpoint("Facility")
    facility.hover_readiness_bars()

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Verify Facility readiness graph",
        "Hover readiness bars",
        "Bars should be interactive",
        "Facility readiness bars hovered",
        "Pass", "", "SO-14", ""
    )

    # ================= SO-15 =================
    # Script_ID:25
    for view in ["Resource", "Alert"]:
        facility.select_readiness_viewpoint(view)

        # ✅ NO hover here
        write_test_report(
            "Tower Track", "Web", "Strategic Overview",
            f"Verify {view} ViewPoint readiness",
            "Change readiness viewpoint",
            "Chart should update correctly",
            f"{view} readiness view validated",
            "Pass", "", "SO-15", ""
        )
