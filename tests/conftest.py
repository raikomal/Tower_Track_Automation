# import sys
# import os
# import pytest
#
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
#
# from tests.login_helper import login_and_reach_dashboard
#
#
# @pytest.fixture(scope="function")
# def driver():
#     driver = login_and_reach_dashboard()
#     yield driver
#     driver.quit()
import pytest
from tests.login_helper import login_and_reach_dashboard

@pytest.fixture(scope="function")
def driver():
    driver = login_and_reach_dashboard()
    yield driver
    driver.quit()

