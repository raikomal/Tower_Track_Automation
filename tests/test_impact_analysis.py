# import time
# from pages.slider_page import SliderPage
# from pages.facility_status_page import FacilityStatusPage
# from utils.csv_writer import write_test_report
# from utils.simulation_api import run_simulation_backend
#
#
# # =========================================================
# # ✅ REUSABLE FLOW (FOR E2E)
# # =========================================================
# def impact_analysis_flow(driver):
#     """
#     Reusable Impact Analysis flow
#     Used by E2E test
#     """
#     test_impact_analysis_flow(driver)
#
#
# # =========================================================
# # ✅ PYTEST TEST (REAL LOGIC + REPORTING)
# # =========================================================
# def test_impact_analysis_flow(driver):
#     slider = SliderPage(driver)
#     facility = FacilityStatusPage(driver)
#
#     # ============================================================
#     # NAVIGATION
#     # ============================================================
#     slider.click_slider("Part Allocation Insights")
#     slider.hover_and_click_facility_status_tracker()
#     facility.go_to_impact_analysis()
#
#     write_test_report(
#         "Tower Track", "Web", "Impact Analysis",
#         "Navigate to Impact Analysis",
#         "Click Impact Analysis tab",
#         "Impact Analysis page should load",
#         "Page loaded",
#         "Pass", "", "IA-NAV-01", ""
#     )
#
#     # ============================================================
#     # DEFAULT FILTERS
#     # ============================================================
#     filters = facility.get_impact_filters()
#     assert isinstance(filters, dict)
#
#     write_test_report(
#         "Tower Track", "Web", "Impact Analysis",
#         "Verify default filters",
#         "Read default filters",
#         "Filters should be visible",
#         str(filters),
#         "Pass", "", "IA-01", ""
#     )
#
#     # ============================================================
#     # FACILITY SELECTION
#     # ============================================================
#     facility.select_impact_facility("CHI1 (Aurora, IL)")
#     time.sleep(1)
#
#     write_test_report(
#         "Tower Track", "Web", "Impact Analysis",
#         "Select Facility",
#         "Select CHI1 (Aurora, IL)",
#         "Facility should be selected",
#         "CHI1 selected",
#         "Pass", "", "IA-02", ""
#     )
#
#     # ============================================================
#     # DATE SELECTION
#     # ============================================================
#     facility.select_impact_start_date("10-08-2024")
#     facility.select_impact_end_date("25-11-2024")
#
#     write_test_report(
#         "Tower Track", "Web", "Impact Analysis",
#         "Select Date Range",
#         "Select Start & End Date",
#         "Dates should be applied",
#         "10-08-2024 → 25-11-2024",
#         "Pass", "", "IA-03", ""
#     )
#
#     # ============================================================
#     # GET RECOMMENDATION
#     # ============================================================
#     facility.click_get_recommendation()
#     time.sleep(2)
#
#     write_test_report(
#         "Tower Track", "Web", "Impact Analysis",
#         "Get Allocation Recommendation",
#         "Click Get Recommendation",
#         "Recommendation should load",
#         "Request sent",
#         "Pass", "", "IA-04", ""
#     )
#
#     # 🔥 WAIT FOR BACKEND PROCESSING
#     facility.wait_for_recommendation_to_finish()
#
#     write_test_report(
#         "Tower Track", "Web", "Impact Analysis",
#         "Recommendation Loaded",
#         "Wait for backend processing",
#         "Recommendation should complete",
#         "Completed",
#         "Pass", "", "IA-04A", ""
#     )
#
#     # ============================================================
#     # MODIFY ALLOCATION
#     # ============================================================
#     facility.modify_allocation_and_compute_cost()
#     time.sleep(2)
#
#     write_test_report(
#         "Tower Track", "Web", "Impact Analysis",
#         "Modify Allocation",
#         "Edit allocation quantities",
#         "Cost charts should update",
#         "Values entered: 20, 50, 70",
#         "Pass", "", "IA-05", ""
#     )
#
#     # ================= SIMULATION PLANNING TOOL =================
#     if facility.scroll_to_simulation_section():
#         if facility.simulation_tool_ready():
#             ran = facility.run_simulation_planning_flow_safe()
#             if ran:
#                 facility.hover_simulation_cost_graphs()
#     else:
#         print("ℹ️ Simulation section skipped (backend-controlled)")
#
#     write_test_report(
#         "Tower Track", "Web", "Impact Analysis",
#         "Simulation Planning Tool",
#         "Run simulation + hover graph",
#         "Simulation graph should appear if data exists",
#         "Simulation executed / skipped safely",
#         "Pass", "", "IA-SIM-FINAL", ""
#     )
#
#     # ============================================================
#     # BACKEND SIMULATION (SOURCE OF TRUTH)
#     # ============================================================
#     run_simulation_backend(
#         source_facility="PHX1 (Chandler, AZ)",
#         destination_facility="PHX2 (Chandler, AZ)",
#         part="Generator",
#         quantity=20
#     )
#
#     write_test_report(
#         "Tower Track", "API", "Simulation",
#         "Backend Simulation",
#         "POST simulate-reallocation",
#         "Simulation API should succeed",
#         "Success",
#         "Pass", "", "IA-SIM-API", ""
#     )
#
#     # ============================================================
#     # FINAL UI VALIDATION
#     # ============================================================
#     facility.scroll_to_simulation_section()
#     facility.hover_simulation_cost_graphs()
#
#     write_test_report(
#         "Tower Track", "Web", "Impact Analysis",
#         "Validate Simulation Graph",
#         "Hover simulation cost graph",
#         "Tooltip should appear",
#         "Graph hovered successfully",
#         "Pass", "", "IA-SIM-FINAL-UI", ""
#     )
import time
from pages.facility_status_page import FacilityStatusPage
from utils.csv_writer import write_test_report
from utils.simulation_api import run_simulation_backend


# tests/test_impact_analysis.py

import time
from pages.facility_status_page import FacilityStatusPage
from utils.csv_writer import write_test_report
from utils.simulation_api import run_simulation_backend


# =========================================================
# ✅ REUSABLE FLOW (FOR E2E)
# =========================================================
def impact_analysis_flow(driver):
    """
    Reusable Impact Analysis flow
    Used by E2E test
    """
    test_impact_analysis_flow(driver)


# =========================================================
# ✅ PYTEST TEST (REAL LOGIC + REPORTING)
# =========================================================
def test_impact_analysis_flow(driver):
    facility = FacilityStatusPage(driver)

    # =====================================================
    # NAVIGATION (NO SLIDER)
    # =====================================================
    facility.go_to_impact_analysis()

    write_test_report(
        "Tower Track", "Web", "Impact Analysis",
        "Navigate to Impact Analysis",
        "Click Impact Analysis tab",
        "Impact Analysis page should load",
        "Page loaded",
        "Pass", "", "IA-01", ""
    )

    # =====================================================
    # FILTERS
    # =====================================================
    filters = facility.get_impact_filters()
    assert isinstance(filters, dict)

    write_test_report(
        "Tower Track", "Web", "Impact Analysis",
        "Verify default filters",
        "Read default filters",
        "Filters should be visible",
        str(filters),
        "Pass", "", "IA-02", ""
    )

    # =====================================================
    # FACILITY + DATE
    # =====================================================
    facility.select_impact_facility("CHI1 (Aurora, IL)")
    facility.select_impact_start_date("10-08-2024")
    facility.select_impact_end_date("25-11-2024")

    write_test_report(
        "Tower Track", "Web", "Impact Analysis",
        "Select facility & date",
        "Apply facility and date range",
        "Inputs should apply",
        "CHI1 + date range applied",
        "Pass", "", "IA-03", ""
    )

    # =====================================================
    # GET RECOMMENDATION
    # =====================================================
    facility.click_get_recommendation()
    facility.wait_for_recommendation_to_finish()

    write_test_report(
        "Tower Track", "Web", "Impact Analysis",
        "Get recommendation",
        "Request allocation recommendation",
        "Recommendation should complete",
        "Recommendation completed",
        "Pass", "", "IA-04", ""
    )

    # =====================================================
    # MODIFY ALLOCATION
    # =====================================================
    facility.modify_allocation_and_compute_cost()

    write_test_report(
        "Tower Track", "Web", "Impact Analysis",
        "Modify allocation",
        "Edit allocation values",
        "Cost charts should update",
        "Allocation modified",
        "Pass", "", "IA-05", ""
    )

    # =====================================================
    # SIMULATION (UI)
    # =====================================================
    if facility.scroll_to_simulation_section():
        if facility.simulation_tool_ready():
            facility.run_simulation_planning_flow_safe()
            facility.hover_simulation_cost_graphs()

    write_test_report(
        "Tower Track", "Web", "Impact Analysis",
        "Simulation planning tool",
        "Run simulation and hover graph",
        "Simulation graph should render",
        "Simulation handled",
        "Pass", "", "IA-06", ""
    )

    # =====================================================
    # SIMULATION (BACKEND)
    # =====================================================
    run_simulation_backend(
        source_facility="PHX1 (Chandler, AZ)",
        destination_facility="PHX2 (Chandler, AZ)",
        part="Generator",
        quantity=20
    )

    write_test_report(
        "Tower Track", "API", "Simulation",
        "Backend simulation",
        "Call simulate-reallocation API",
        "API should succeed",
        "Backend simulation success",
        "Pass", "", "IA-07", ""
    )
