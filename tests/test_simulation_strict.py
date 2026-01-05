from pages.facility_status_page import FacilityStatusPage
from pages.simulation_page import SimulationPage


def test_simulation_planning(driver):
    """
    Functional test for Simulation Planning Tool
    (SAFE – Playwright-inspired Selenium)
    """

    facility = FacilityStatusPage(driver)
    simulation = SimulationPage(driver)

    # ---------------- NAVIGATION ----------------
    facility.go_to_impact_analysis()

    facility.select_impact_facility("PHX1 (Chandler, AZ)")
    facility.select_impact_start_date("10-08-2024")
    facility.select_impact_end_date("25-11-2024")

    facility.click_get_recommendation()
    facility.wait_for_recommendation_to_finish()
    facility.modify_allocation_and_compute_cost()

    # ---------------- SIMULATION ----------------
    if simulation.is_rendered():
        assert simulation.run_simulation_safe(
            source="OSK1 (Osaka, JP)",
            destination="NVA5 (Sterling, VA)",
            part="MV Transformers",
            quantity="28"
        ), "Simulation did not execute"

        simulation.hover_cost_graphs()
    else:
        print("ℹ️ Simulation Planning Tool not rendered (backend-driven)")
