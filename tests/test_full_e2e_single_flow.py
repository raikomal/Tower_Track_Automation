from utils.csv_writer import start_new_report, write_test_report

from .test_strategic_overview_flow import strategic_overview_flow
from .test_transportation_detail_view import transportation_detail_view_flow
from .test_operational_insights import operational_insights_flow
from .test_impact_analysis import impact_analysis_flow


def test_full_single_flow(driver):
    """
    ONE LOGIN
    ONE BROWSER
    ONE CSV REPORT
    FULL END-TO-END FLOW
    """

    # =====================================================
    # 1️⃣ START CSV REPORT
    # =====================================================
    start_new_report()

    # =====================================================
    # 2️⃣ LOGIN REPORT (LOGIN ALREADY DONE IN FIXTURE)
    # =====================================================
    write_test_report(
        "Tower Track",
        "Web",
        "Authentication",
        "User Login",
        "Login with valid credentials",
        "Dashboard should load",
        "Dashboard loaded successfully",
        "Pass",
        "",
        "LOGIN-01",
        ""
    )

    # =====================================================
    # 3️⃣ STRATEGIC OVERVIEW
    # (Map, KPI Cards, Map Hover, KPI Table, Bar Chart,
    #  Sankey, Readiness)
    # =====================================================
    strategic_overview_flow(driver)

    # =====================================================
    # 4️⃣ TRANSPORTATION DETAIL VIEW (Arrow → New Tab)
    # =====================================================
    transportation_detail_view_flow(driver)

    # =====================================================
    # 5️⃣ OPERATIONAL INSIGHTS
    # =====================================================
    operational_insights_flow(driver)

    # =====================================================
    # 6️⃣ IMPACT ANALYSIS
    # =====================================================
    impact_analysis_flow(driver)

    # =====================================================
    # 7️⃣ FINAL SUMMARY ROW
    # =====================================================
    write_test_report(
        "Tower Track",
        "Web",
        "E2E Automation",
        "Full end-to-end flow",
        "Single login → complete automation",
        "All modules should execute",
        "Strategic + Transportation + Operational + Impact completed",
        "Pass",
        "",
        "E2E-01",
        ""
    )

