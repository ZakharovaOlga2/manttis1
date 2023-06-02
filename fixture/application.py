from selenium import webdriver
from fixture.session import SessionHelper
from fixture.soap import SoapHelper

class Application:

    def __init__(self, browser="firefox", testdata=None, wsdl=None, username=None, password=None):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.testdata = testdata
        self.soap = SoapHelper(self, username=username, password=password, wsdl=wsdl)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self, base_url):
        wd = self.wd
        wd.get(base_url)

    def destroy(self):
        self.wd.quit()