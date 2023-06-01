import pytest
from fixture.application import Application
import json
import os.path

fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),file)
        with open(config_file_path) as config_file:
            target = json.load(config_file)
    return target

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web = load_config(request.config.getoption("--target"))['web']
    web_admin = load_config(request.config.getoption("--target"))['webadmin']
    testdata = load_config(request.config.getoption("--target"))['testdata']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser,testdata=testdata)
    fixture.session.ensure_login(username=web_admin["username"], password=web_admin["password"], base_url=web["baseurl"])
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")



