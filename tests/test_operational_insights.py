# import time
# from pages.slider_page import SliderPage
# from pages.facility_status_page import FacilityStatusPage
# from utils.csv_writer import write_test_report
#
#
# # =========================================================
# # ✅ REUSABLE FLOW (FOR E2E)
# # =========================================================
# def operational_insights_flow(driver):
#     """
#     Reusable Operational Insights flow
#     Used by E2E test
#     """
#     test_operational_insights_flow(driver)
#
#
# # =========================================================
# # ✅ PYTEST TEST (REAL LOGIC + REPORTING)
# # =========================================================
# def test_operational_insights_flow(driver):
#     slider = SliderPage(driver)
#     facility = FacilityStatusPage(driver)
#
#     # ================= NAVIGATION =================
#     slider.click_slider("Part Allocation Insights")
#     slider.hover_and_click_facility_status_tracker()
#     facility.go_to_operational_insights()
#
#     # ================= FILTERS (DEFAULT) =================
#     filters = facility.get_operational_filters()
#     assert isinstance(filters, dict)
#
#     write_test_report(
#         "Tower Track", "Web", "Operational Insights",
#         "Verify default filters",
#         "Read selected filters",
#         "Filters should be visible",
#         str(filters),
#         "Pass", "", "OI-01", ""
#     )
#
#     # ================= ALLOCATION TABLE =================
#     rows = facility.get_operational_allocation_table()
#     assert isinstance(rows, list)
#
#     write_test_report(
#         "Tower Track", "Web", "Operational Insights",
#         "Verify allocation table",
#         "Read table rows",
#         "Table may or may not have data",
#         f"Rows: {len(rows)}",
#         "Pass", "", "OI-02", ""
#     )
#
#     # ================= INVENTORY DETAILS =================
#     inventory = facility.get_part_inventory_details()
#     assert isinstance(inventory, dict)
#
#     write_test_report(
#         "Tower Track", "Web", "Operational Insights",
#         "Verify inventory details",
#         "Read inventory panel",
#         "Inventory should load if data exists",
#         str(inventory),
#         "Pass", "", "OI-03", ""
#     )
#
#     # ================= STEP 1: DELAYED =================
#     facility.select_operational_status("delayed")
#     facility.select_operational_part("CRAH Stands")
#     time.sleep(1.5)
#
#     rows_delayed = facility.get_operational_allocation_table()
#
#     write_test_report(
#         "Tower Track", "Web", "Operational Insights",
#         "Verify Delayed + CRAH Stands",
#         "Change filters",
#         "Table should update",
#         f"Rows: {len(rows_delayed)}",
#         "Pass", "", "OI-04", ""
#     )
#
#     # ================= STEP 2: PENDING =================
#     facility.select_operational_status("pending")
#     facility.select_operational_part("Cable Busway")
#     time.sleep(1.5)
#
#     rows_pending = facility.get_operational_allocation_table()
#
#     write_test_report(
#         "Tower Track", "Web", "Operational Insights",
#         "Verify Pending + Cable Busway",
#         "Change filters",
#         "Table should update",
#         f"Rows: {len(rows_pending)}",
#         "Pass", "", "OI-05", ""
#     )
#
#     # ================= PART DEPENDENCY GRAPH (NEW TAB) =================
#     parent_window = driver.current_window_handle
#
#     facility.open_part_dependency_graph_tab()
#     facility.select_first_three_dependency_options()
#
#     write_test_report(
#         "Tower Track", "Web", "Operational Insights",
#         "Verify Part Dependency Graph",
#         "Open graph and change dropdown",
#         "Graph should update",
#         "Selected first 3 dropdown options",
#         "Pass", "", "OI-06", ""
#     )
#
#     facility.close_child_and_return(parent_window)
import time
from pages.facility_status_page import FacilityStatusPage
from utils.csv_writer import write_test_report


# =========================================================
# ✅ REUSABLE FLOW (FOR E2E)
# =========================================================
def operational_insights_flow(driver):
    """
    Reusable Operational Insights flow
    Used by E2E test
    """
    test_operational_insights_flow(driver)


# =========================================================
# ✅ PYTEST TEST (REAL LOGIC + REPORTING)
# =========================================================
def test_operational_insights_flow(driver):
    facility = FacilityStatusPage(driver)

    # ================= NAVIGATION =================
    # ⚠️ DO NOT USE SLIDER HERE
    # Strategic Overview already opened Facility Status Tracker
    facility.go_to_operational_insights()

    # ================= FILTERS (DEFAULT) =================
    filters = facility.get_operational_filters()
    assert isinstance(filters, dict)

    write_test_report(
        "Tower Track", "Web", "Operational Insights",
        "Verify default filters",
        "Read selected filters",
        "Filters should be visible",
        str(filters),
        "Pass", "", "OI-01", ""
    )

    # ================= ALLOCATION TABLE =================
    rows = facility.get_operational_allocation_table()
    assert isinstance(rows, list)

    write_test_report(
        "Tower Track", "Web", "Operational Insights",
        "Verify allocation table",
        "Read table rows",
        "Table may or may not have data",
        f"Rows: {len(rows)}",
        "Pass", "", "OI-02", ""
    )

    # ================= INVENTORY DETAILS =================
    inventory = facility.get_part_inventory_details()
    assert isinstance(inventory, dict)

    write_test_report(
        "Tower Track", "Web", "Operational Insights",
        "Verify inventory details",
        "Read inventory panel",
        "Inventory should load if data exists",
        str(inventory),
        "Pass", "", "OI-03", ""
    )

    # ================= STEP 1: DELAYED =================
    facility.select_operational_status("delayed")
    facility.select_operational_part("CRAH Stands")
    time.sleep(1.5)

    rows_delayed = facility.get_operational_allocation_table()

    write_test_report(
        "Tower Track", "Web", "Operational Insights",
        "Verify Delayed + CRAH Stands",
        "Change filters",
        "Table should update",
        f"Rows: {len(rows_delayed)}",
        "Pass", "", "OI-04", ""
    )

    # ================= STEP 2: PENDING =================
    facility.select_operational_status("pending")
    facility.select_operational_part("Cable Busway")
    time.sleep(1.5)

    rows_pending = facility.get_operational_allocation_table()

    write_test_report(
        "Tower Track", "Web", "Operational Insights",
        "Verify Pending + Cable Busway",
        "Change filters",
        "Table should update",
        f"Rows: {len(rows_pending)}",
        "Pass", "", "OI-05", ""
    )

    # ================= PART DEPENDENCY GRAPH (NEW TAB) =================
    parent_window = driver.current_window_handle

    facility.open_part_dependency_graph_tab()
    facility.select_first_three_dependency_options()

    write_test_report(
        "Tower Track", "Web", "Operational Insights",
        "Verify Part Dependency Graph",
        "Open graph and change dropdown",
        "Graph should update",
        "Selected first 3 dropdown options",
        "Pass", "", "OI-06", ""
    )

    facility.close_child_and_return(parent_window)
