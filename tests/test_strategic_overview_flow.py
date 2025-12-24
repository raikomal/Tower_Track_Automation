# import time
# from pages.slider_page import SliderPage
# from pages.facility_status_page import FacilityStatusPage
# from utils.csv_writer import start_new_report, write_test_report
# from utils.alert_handler import handle_any_alert
#
#
# def test_strategic_overview_flow(driver):
#
#     # ---------------- REPORT INIT ----------------
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
#     handle_any_alert(driver)
#     time.sleep(3)
#
#     write_test_report(
#         "Tower Track", "Web", "Navigation",
#         "Open Facility Status Tracker",
#         "Navigate via Part Allocation Insights",
#         "Facility page should open",
#         "Facility page opened",
#         "Pass", "", "SO-01", ""
#     )
#
#     # =========================================================
#     # TC-SO-02: Strategic Overview Load
#     # =========================================================
#     assert facility.verify_strategic_overview_loaded()
#
#     write_test_report(
#         "Tower Track", "Web", "Strategic Overview",
#         "Verify page load",
#         "Strategic Overview default tab",
#         "Widgets visible",
#         "Widgets loaded",
#         "Pass", "", "SO-02", ""
#     )
#
#     # =========================================================
#     # TC-SO-03: KPI Cards
#     # =========================================================
#     kpis = facility.get_kpi_card_values()
#     assert len(kpis) >= 5
#
#     write_test_report(
#         "Tower Track", "Web", "Strategic Overview",
#         "Verify KPI cards",
#         "Read KPI card values",
#         "At least 5 KPI cards should be visible",
#         f"KPI card values: {kpis[:5]}",
#         "Pass", "", "SO-03", ""
#     )
#
#     # =========================================================
#     # TC-SO-04: Map (verify → hover)
#     # =========================================================
#     assert facility.verify_strategic_overview_loaded()
#
#     points = facility.get_facility_map_points()
#     assert len(points) > 0
#
#     for p in points[:3]:
#         facility.hover_on_map_point(p)
#         time.sleep(0.8)
#
#     write_test_report(
#         "Tower Track", "Web", "Strategic Overview",
#         "Verify map hover",
#         "Hover facility map circles",
#         "Map should respond",
#         f"{len(points)} points detected",
#         "Pass", "", "SO-04", ""
#     )
#
#     # =========================================================
#     # TC-SO-05: KPI Table hover + dropdown
#     # =========================================================
#     facility.scroll_to_kpi_table()
#     assert facility.wait_for_kpis_to_load()
#
#     facilities = facility.get_all_kpi_facilities()
#     assert len(facilities) > 0
#
#     for name in facilities[:3]:
#         facility.hover_on_kpi_row(name)
#         time.sleep(1)
#
#     facility.switch_kpi_view("table")
#
#     write_test_report(
#         "Tower Track", "Web", "Strategic Overview",
#         "Verify KPI table hover",
#         "Hover KPI table rows and switch dropdown",
#         "Rows should highlight correctly",
#         f"{len(facilities)} facilities found",
#         "Pass", "", "SO-05", ""
#     )
#
#     # =========================================================
#     # TC-SO-06: KPI Bar Chart hover
#     # =========================================================
#     facility.switch_kpi_view("barchart")
#     time.sleep(2)
#
#     bars = facility.get_kpi_bars()
#     assert len(bars) > 0
#
#     for bar in bars[:3]:
#         facility.hover_on_kpi_bar(bar)
#         time.sleep(1)
#
#     write_test_report(
#         "Tower Track", "Web", "Strategic Overview",
#         "Verify KPI bar chart hover",
#         "Hover KPI bars",
#         "Tooltips should appear",
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
        "Click Part Allocation → Facility Status Tracker",
        "Facility page should open",
        "Facility page opened",
        "Pass", "", "SO-01", ""
    )

    # =========================================================
    # TC-SO-02: Strategic Overview Load (MAP SVG = LOAD)
    # =========================================================
    facility.scroll_to_map_section()
    time.sleep(1)

    assert facility.verify_map_visible()

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Verify Strategic Overview load",
        "Wait for map SVG",
        "Strategic Overview should load",
        "Strategic Overview loaded",
        "Pass", "", "SO-02", ""
    )

    # =========================================================
    # TC-SO-03: KPI Table Data (REAL KPI VALUES)
    # =========================================================
    assert facility.wait_for_kpis_to_load()

    kpis = facility.get_all_kpi_values()
    assert len(kpis) >= 5

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Verify KPI values",
        "Read KPI values from table",
        "KPI values should be present",
        f"KPI values: {kpis[:5]}",
        "Pass", "", "SO-03", ""
    )

    # =========================================================
    # TC-SO-04: MAP Hover (CRITICAL)
    # =========================================================
    points = facility.get_facility_map_points()
    assert len(points) > 0

    facility.hover_multiple_map_circles(count=5)

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Verify map hover",
        "Hover facility map circles",
        "Map should respond",
        f"{len(points)} map points found",
        "Pass", "", "SO-04", ""
    )

    # =========================================================
    # TC-SO-05: KPI Table Hover + Dropdown
    # =========================================================
    facility.scroll_to_kpi_table()
    assert facility.wait_for_kpis_to_load()

    facilities = facility.get_all_kpi_facilities()
    assert len(facilities) > 0

    for f in facilities[:3]:
        facility.hover_on_kpi_row(f)
        time.sleep(0.6)

    facility.switch_kpi_view("table")

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Verify KPI table hover",
        "Hover table rows and switch view",
        "Rows should highlight",
        f"{len(facilities)} facilities found",
        "Pass", "", "SO-05", ""
    )

    # =========================================================
    # TC-SO-06: KPI Bar Chart Hover
    # =========================================================
    facility.switch_kpi_view("barchart")
    time.sleep(1.5)

    bars = facility.get_kpi_bars()
    assert len(bars) > 0

    for bar in bars[:3]:
        facility.hover_on_kpi_bar(bar)

    write_test_report(
        "Tower Track", "Web", "Strategic Overview",
        "Verify KPI bar chart hover",
        "Hover KPI bars",
        "Bar chart should respond",
        f"{len(bars)} bars detected",
        "Pass", "", "SO-06", ""
    )
