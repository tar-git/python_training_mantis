from selenium import webdriver

from fixture.james import JamesHelper
from fixture.session import SessionHelper
from fixture.project_helper import ProjectHelper
from fixture.mail import MailHelper
from fixture.signup import SignupHelper
from fixture.soap import SoapHelper


class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized %s" % browser)
        self.session = SessionHelper(self)
        self.james = JamesHelper(self)
        self.project = ProjectHelper(self)
        self.config = config
        self.base_url = config["web"]["baseUrl"]
        self.mail = MailHelper(self)
        self.signup = SignupHelper(self)
        self.soap = SoapHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url == self.base_url
           and len(wd.find_elements_by_link_text("Last name")) > 0):
            wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
