class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, login, password, base_url):
        wd = self.app.wd
        self.app.open_home_page(base_url)
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(login)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def is_project_exists(self, project_name):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath(f"//td//a[text()='{project_name}']"))>0

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//td[@class='login-info-left' and text()='Logged in as: ']")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("td.login-info-left span").text

    def menu_link_by_name(self, item):
        wd = self.app.wd
        wd.find_element_by_link_text(item).click()

    project_cache = None

    def add_project(self, project_name):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project_name)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.project_cache = None

    def delete_project(self, project_name):
        wd = self.app.wd
        wd.find_element_by_link_text(project_name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            self.project_cache=[]
            wd = self.app.wd
            for row in wd.find_elements_by_xpath("//a[contains(@href,'manage_proj_edit')]"):
                self.project_cache.append(row.text)
        return list(self.project_cache)

    def manage_menu_link(self, item):
        wd = self.app.wd
        wd.find_element_by_link_text(item).click()

    def ensure_login(self, username, password,base_url):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username,password,base_url)
