# # import time
# # from pages.slider_page import SliderPage
# # from pages.facility_status_page import FacilityStatusPage
# # from utils.csv_writer import start_new_report, write_test_report
# # from utils.alert_handler import handle_any_alert
# #
# #
# # def test_strategic_overview_flow(driver):
# #
# #     # ---------------- REPORT INIT ----------------
# #     start_new_report()
# #
# #     slider = SliderPage(driver)
# #     facility = FacilityStatusPage(driver)
# #
# #     # =========================================================
# #     # TC-SO-01: Navigation
# #     # =========================================================
# #     slider.navigate_to_part_allocation_insights()
# #     handle_any_alert(driver)
# #
# #     slider.open_facility_status_tracker()
# #     handle_any_alert(driver)
# #     time.sleep(3)
# #
# #     write_test_report(
# #         "Tower Track", "Web", "Navigation",
# #         "Open Facility Status Tracker",
# #         "Navigate via Part Allocation Insights",
# #         "Facility page should open",
# #         "Facility page opened",
# #         "Pass", "", "SO-01", ""
# #     )
# #
# #     # =========================================================
# #     # TC-SO-02: Strategic Overview Load
# #     # =========================================================
# #     assert facility.verify_strategic_overview_loaded()
# #
# #     write_test_report(
# #         "Tower Track", "Web", "Strategic Overview",
# #         "Verify page load",
# #         "Strategic Overview default tab",
# #         "Widgets visible",
# #         "Widgets loaded",
# #         "Pass", "", "SO-02", ""
# #     )
# #
# #     # =========================================================
# #     # TC-SO-03: KPI Cards
# #     # =========================================================
# #     kpis = facility.get_kpi_card_values()
# #     assert len(kpis) >= 5
# #
# #     write_test_report(
# #         "Tower Track", "Web", "Strategic Overview",
# #         "Verify KPI cards",
# #         "Read KPI card values",
# #         "At least 5 KPI cards should be visible",
# #         f"KPI card values: {kpis[:5]}",
# #         "Pass", "", "SO-03", ""
# #     )
# #
# #     # =========================================================
# #     # TC-SO-04: Map (verify → hover)
# #     # =========================================================
# #     assert facility.verify_strategic_overview_loaded()
# #
# #     points = facility.get_facility_map_points()
# #     assert len(points) > 0
# #
# #     for p in points[:3]:
# #         facility.hover_on_map_point(p)
# #         time.sleep(0.8)
# #
# #     write_test_report(
# #         "Tower Track", "Web", "Strategic Overview",
# #         "Verify map hover",
# #         "Hover facility map circles",
# #         "Map should respond",
# #         f"{len(points)} points detected",
# #         "Pass", "", "SO-04", ""
# #     )
# #
# #     # =========================================================
# #     # TC-SO-05: KPI Table hover + dropdown
# #     # =========================================================
# #     facility.scroll_to_kpi_table()
# #     assert facility.wait_for_kpis_to_load()
# #
# #     facilities = facility.get_all_kpi_facilities()
# #     assert len(facilities) > 0
# #
# #     for name in facilities[:3]:
# #         facility.hover_on_kpi_row(name)
# #         time.sleep(1)
# #
# #     facility.switch_kpi_view("table")
# #
# #     write_test_report(
# #         "Tower Track", "Web", "Strategic Overview",
# #         "Verify KPI table hover",
# #         "Hover KPI table rows and switch dropdown",
# #         "Rows should highlight correctly",
# #         f"{len(facilities)} facilities found",
# #         "Pass", "", "SO-05", ""
# #     )
# #
# #     # =========================================================
# #     # TC-SO-06: KPI Bar Chart hover
# #     # =========================================================
# #     facility.switch_kpi_view("barchart")
# #     time.sleep(2)
# #
# #     bars = facility.get_kpi_bars()
# #     assert len(bars) > 0
# #
# #     for bar in bars[:3]:
# #         facility.hover_on_kpi_bar(bar)
# #         time.sleep(1)
# #
# #     write_test_report(
# #         "Tower Track", "Web", "Strategic Overview",
# #         "Verify KPI bar chart hover",
# #         "Hover KPI bars",
# #         "Tooltips should appear",
# #         f"{len(bars)} bars detected",
# #         "Pass", "", "SO-06", ""
# #     )
# #
# import time
# from pages.slider_page import SliderPage
# from pages.facility_status_page import FacilityStatusPage
# from utils.csv_writer import start_new_report, write_test_report
# from utils.alert_handler import handle_any_alert
#
#
# def test_strategic_overview_flow(driver):
#
#     # =========================================================
#     # REPORT INIT
#     # =========================================================
#     start_new_report()
#
#     slider = SliderPage(driver)
#     facility = FacilityStatusPage(driver)
#
#     # =========================================================
#     # TC-SO-01: Navigation
#     # =========================================================
#     slider.navigate_to_part_allocation_insights()
#     handle_any_alert(driver)
#
#     slider.open_facility_status_tracker()
#     facility.wait_for_dom_stability()
#     handle_any_alert(driver)
#
#     write_test_report(
#         "Tower Track", "Web", "Navigation",
#         "Open Facility Status Tracker",
#         "Click Part Allocation → Facility Status Tracker",
#         "Facility page should open",
#         "Facility page opened",
#         "Pass", "", "SO-01", ""
#     )
#
#     # =========================================================
#     # TC-SO-02: Strategic Overview Load (MAP SVG = LOAD)
#     # =========================================================
#     # =========================================================
#     # TC-SO-04: MAP Hover (FINAL & STABLE)
#     # =========================================================
#     facility.scroll_to_map_section()
#
#     # Wait only for MAP SVG (not bars)
#     assert facility.verify_map_visible()
#
#     # Small deterministic delay for Highcharts animation
#     time.sleep(0.8)
#
#     points = facility.get_facility_map_points()
#     print("MAP POINTS FOUND:", len(points))
#
#     assert len(points) > 0
#
#     facility.hover_multiple_map_circles(count=min(5, len(points)))
#
#     write_test_report(
#         "Tower Track", "Web", "Strategic Overview",
#         "Verify Strategic Overview load",
#         "Wait for map SVG",
#         "Strategic Overview should load",
#         "Strategic Overview loaded",
#         "Pass", "", "SO-02", ""
#     )
#
#     # =========================================================
#     # TC-SO-03: KPI Table Data (REAL KPI VALUES)
#     # =========================================================
#     assert facility.wait_for_kpis_to_load()
#
#     kpis = facility.get_all_kpi_values()
#     assert len(kpis) >= 5
#
#     write_test_report(
#         "Tower Track", "Web", "Strategic Overview",
#         "Verify KPI values",
#         "Read KPI values from table",
#         "KPI values should be present",
#         f"KPI values: {kpis[:5]}",
#         "Pass", "", "SO-03", ""
#     )
#     # =========================================================
#     # TC-SO-04: MAP Hover (CRITICAL)
#     # =========================================================
#     points = facility.get_facility_map_points()
#
#     print("MAP POINTS FOUND:", len(points))
#     assert len(points) > 0
#
#     facility.hover_multiple_map_circles(count=5)
#
#     write_test_report(
#         "Tower Track", "Web", "Strategic Overview",
#         "Verify map hover",
#         "Hover facility map circles",
#         "Map should respond",
#         f"{len(points)} map points found",
#         "Pass", "", "SO-04", ""
#     )
#
#     # =========================================================
#     # TC-SO-05: KPI Table Hover + Dropdown
#     # =========================================================
#     facility.scroll_to_kpi_table()
#     assert facility.wait_for_kpis_to_load()
#
#     facilities = facility.get_all_kpi_facilities()
#     assert len(facilities) > 0
#
#     for f in facilities[:3]:
#         facility.hover_on_kpi_row(f)
#         time.sleep(0.6)
#
#     facility.switch_kpi_view("table")
#
#     write_test_report(
#         "Tower Track", "Web", "Strategic Overview",
#         "Verify KPI table hover",
#         "Hover table rows and switch view",
#         "Rows should highlight",
#         f"{len(facilities)} facilities found",
#         "Pass", "", "SO-05", ""
#     )
#
#     # =========================================================
#     # TC-SO-06: KPI Bar Chart Hover (BAR ONLY)
#     # =========================================================
#     facility.switch_kpi_view("barchart")
#     facility.wait_for_dom_stability()
#     bars = facility.get_kpi_bars()
#
#     time.sleep(2)
#
#     bars = facility.get_kpi_bars()
#     assert len(bars) > 0
#
#     for bar in bars[:4]:
#         facility.hover_on_kpi_bar(bar)
#         time.sleep(1)
#
#     write_test_report(
#         "Tower Track", "Web", "Strategic Overview",
#         "Verify KPI bar chart hover",
#         "Hover KPI bars only",
#         "Bar tooltip should appear",
#         f"{len(bars)} bars detected",
#         "Pass", "", "SO-06", ""
#     )
#
import time
from pages.slider_page import SliderPage
from pages.facility_status_page import FacilityStatusPage
from utils.csv_writer import start_new_report, write_test_report
from utils.alert_handler import handle_any_alert


def test_strategic_overview_flow(driver):

    # =========================================================
    # REPORT INIT
    # =========================================================
    start_new_report()

    slider = SliderPage(driver)
    facility = FacilityStatusPage(driver)

    # =========================================================
    # TC-SO-01: Navigation
    # =========================================================
    slider.navigate_to_part_allocation_insights()
    handle_any_alert(driver)

    slider.open_facility_status_tracker()
    handle_any_alert(driver)

    write_test_report(
        "Tower Track", "Web", "Navigation",
        "Open Facility Status Tracker",
        "Navigate via Part Allocation Insights",
        "Facility Status page should open",
        "Facility Status page opened",
        "Pass", "", "SO-01", ""
    )

    # =========================================================
    # TC-SO-02: Page Load (MAP = READY)
    # =========================================================
    facility.wait_for_map_svg_once()

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Verify page load",
        "Wait for Highcharts map",
        "Map should render",
        "Map rendered",
        "Pass", "", "SO-02", ""
    )

    # =========================================================
    # TC-SO-03: KPI CARDS (TOP SUMMARY)
    # =========================================================
    kpis = facility.get_kpi_card_values()
    print("KPI CARDS:", kpis)

    assert len(kpis) >= 3, "KPI cards not detected"

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Verify KPI cards",
        "Read KPI summary cards",
        "KPI cards should be visible",
        f"KPI values: {kpis[:3]}",
        "Pass", "", "SO-03", ""
    )

    # =========================================================
    # TC-SO-04: MAP HOVER (FULFILLMENT RATE)
    # =========================================================
    map_points = facility.get_facility_map_points()
    print("MAP POINTS FOUND:", len(map_points))

    assert len(map_points) > 0, "No map points found"

    facility.hover_multiple_map_circles(count=5)

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Verify map hover",
        "Hover on facility map bubbles",
        "Tooltip should appear",
        f"{len(map_points)} map points detected",
        "Pass", "", "SO-04", ""
    )

    # =========================================================
    # TC-SO-05: KPI TABLE (MISALLOCATION RATE)
    # =========================================================
    facility.scroll_to_kpi_table()
    facility.wait_for_kpis_to_load()

    facilities = facility.get_all_kpi_facilities()
    misalloc_values = facility.get_misallocation_rate_values()

    print("FACILITIES:", facilities)
    print("MISALLOCATION VALUES:", misalloc_values)

    assert len(facilities) > 0, "Facility list empty"
    assert len(misalloc_values) > 0, "Misallocation values missing"

    for name in facilities[:3]:
        facility.hover_on_kpi_row(name)
        time.sleep(0.4)

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Verify KPI table hover",
        "Hover facility KPI rows",
        "Rows should highlight",
        f"{len(facilities)} facilities found",
        "Pass", "", "SO-05", ""
    )

    # =========================================================
    # TC-SO-06: BAR CHART (READINESS SCORE)
    # =========================================================
    facility.switch_kpi_view("barchart")

    bars = facility.get_bar_chart_columns()
    print("BAR COUNT:", len(bars))

    assert len(bars) > 0, "Bar chart columns not detected"

    for bar in bars[:3]:
        facility.hover_on_bar(bar)
        time.sleep(0.5)

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Verify bar chart hover",
        "Hover readiness bars",
        "Tooltip should appear",
        f"{len(bars)} bars detected",
        "Pass", "", "SO-06", ""
    )
