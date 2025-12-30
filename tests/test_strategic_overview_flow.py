# import time
# from pages.slider_page import SliderPage
# from pages.facility_status_page import FacilityStatusPage
# from utils.csv_writer import write_test_report
#
# from utils.simulation_api import run_simulation_backend
#
#
#
# def strategic_overview_flow(driver):
#     """
#     Reusable Strategic Overview flow
#     Used by E2E test
#     """
#     test_strategic_overview_flow(driver)
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
#     facility = FacilityStatusPage(driver)
#
#     # ============================================================
#     # NAVIGATION
#     # ============================================================
#     # ⚠️ DO NOT USE SLIDER HERE
#     # Strategic Overview already opened Facility Status Tracker
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
# tests/test_strategic_overview_flow.py

from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage
from utils.csv_writer import write_test_report


def strategic_overview_flow(driver):
    test_strategic_overview_flow(driver)


def test_strategic_overview_flow(driver):
    slider = SliderPage(driver)
    facility = FacilityStatusPage(driver)
    # Script_ID:8
    # ================= NAVIGATION =================
    slider.navigate_to_part_allocation_insights()
    slider.hover_and_click_facility_status_tracker()

    write_test_report("Tower Track","Web","Strategic Overview",
        "Open Facility Status Tracker","Navigate via slider",
        "Page should open","Opened","Pass","","SO-01","")

    # ================= MAP LOAD =================
    facility.verify_strategic_overview_loaded()

    write_test_report("Tower Track","Web","Strategic Overview",
        "Verify map load","Wait for map",
        "Map should render","Map rendered","Pass","","SO-02","")

    # ================= KPI CARDS =================
    kpis = facility.get_kpi_card_values()
    assert len(kpis) >= 3

    write_test_report("Tower Track","Web","Strategic Overview",
        "Verify KPI cards","Read KPIs",
        "KPIs should appear",str(kpis),"Pass","","SO-03","")

    # ================= MAP HOVER =================
    facility.hover_multiple_map_circles(5)

    write_test_report("Tower Track","Web","Strategic Overview",
        "Verify map hover","Hover bubbles",
        "Tooltip should show","Hover OK","Pass","","SO-04","")

    # ================= KPI TABLE =================
    facility.scroll_to_kpi_table()
    facility.wait_for_kpis_to_load()

    facilities = facility.get_all_kpi_facilities()
    for f in facilities[:3]:
        facility.hover_on_kpi_row(f)

    write_test_report("Tower Track","Web","Strategic Overview",
        "Verify KPI table","Hover rows",
        "Rows highlight","Rows hovered","Pass","","SO-05","")

    # ================= BAR CHART =================
    facility.switch_kpi_view("barchart")
    bars = facility.get_bar_chart_columns()

    for bar in bars[:3]:
        facility.hover_on_bar(bar)

    write_test_report("Tower Track","Web","Strategic Overview",
        "Verify bar chart","Hover bars",
        "Tooltip visible","Bars hovered","Pass","","SO-06","")

    # ================= SANKEY =================
    facility.verify_sankey_chart_visible()
    facility.change_sankey_flow_view()
    facility.hover_flow_links(3)

    write_test_report("Tower Track","Web","Strategic Overview",
        "Verify Sankey","Change dropdown",
        "Flow updates","Updated","Pass","","SO-07","")

    # ================= READINESS (LAST) =================
    for view, tc in [
        ("Facility","SO-08"),
        ("Resource","SO-09"),
        ("Alert","SO-10"),
        ("Transportation","SO-11")
    ]:
        facility.select_readiness_viewpoint(view)

        write_test_report("Tower Track","Web","Strategic Overview",
            f"Verify {view} readiness",
            f"Switch to {view}",
            "View should update",
            f"{view} loaded",
            "Pass","",tc,"")
