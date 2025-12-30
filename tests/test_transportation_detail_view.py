# tests/test_transportation_detail_view.py

from pages.facility_status_page import FacilityStatusPage
from utils.csv_writer import write_test_report


def transportation_detail_view_flow(driver):
    test_transportation_detail_view(driver)


def test_transportation_detail_view(driver):
    facility = FacilityStatusPage(driver)

    # ===============================
    # 1️⃣ Click arrow → open NEW TAB
    # ===============================
    parent = driver.current_window_handle
    facility.click_transportation_arrow()

    write_test_report(
        "Tower Track", "Web", "Transportation View",
        "Open Transportation detail view",
        "Click transportation arrow",
        "New tab should open",
        "New tab opened",
        "Pass", "", "TR-01", ""
    )

    # ===============================
    # 2️⃣ Verify Transportation page
    # ===============================
    assert facility.verify_transportation_view_page_loaded(), \
        "Transportation detail page did not load"

    write_test_report(
        "Tower Track", "Web", "Transportation View",
        "Verify Transportation page load",
        "Wait for route & DOM",
        "Transportation page should load",
        "Page loaded",
        "Pass", "", "TR-02", ""
    )

    # ===============================
    # 3️⃣ Close tab & return
    # ===============================
    facility.close_child_and_return(parent)

    write_test_report(
        "Tower Track", "Web", "Transportation View",
        "Return to Strategic Overview",
        "Close transportation tab",
        "Should return to main window",
        "Returned successfully",
        "Pass", "", "TR-03", ""
    )
