# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from fixture.common import wait_for, wait_for_elements
from model.project_model import Project
from fixture.common import random_string

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        wait_for(wd, By.CSS_SELECTOR, 'a[class="manage-menu-link"]').click()
        wait_for_elements(wd, By.CSS_SELECTOR, 'div#manage-menu a')[1].click()

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        # init project creation
        wait_for(wd, By.CSS_SELECTOR, 'input.button-small[value="Create New Project"]').click()
        self.fill_project_form(project)
        # submit project creation
        wd.find_element_by_css_selector('input.button[value="Add Project"]').click()
        self.open_projects_page()
        self.project_cache = None

    def select_project_by_name(self, name):
        wd = self.app.wd
        self.open_projects_page()
        project_table = wait_for(wd, By.CSS_SELECTOR, 'tbody')
        project = None
        for element in project_table.find_elements_by_css_selector('a'):
            if element.text == name:
                project = element
        if project is not None:
            project.click()
        else:
            raise RuntimeError(f'no project with name "{name}"')

    def delete_by_name(self, name):
        wd = self.app.wd
        self.select_project_by_name(name)
        wait_for(wd, By.CSS_SELECTOR, 'input[value="Delete Project"]').click()
        wait_for(wd, By.CSS_SELECTOR, 'input[value="Delete Project"]').click()
        self.project_cache = None

    def fill_project_form(self, project):
        self.change_field_value('input#project-name', project.name)
        self.change_field_value('textarea#project-description', project.description)

    def change_field_value(self, field, text):
        wd = self.app.wd
        if text is not None:
            element = wd.find_element_by_css_selector(field)
            element.click()
            element.clear()
            element.send_keys(text)

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_projects_page()
            self.project_cache = list()
            project_table = wait_for(wd, By.CSS_SELECTOR, 'tbody')
            for element in project_table.find_elements_by_css_selector('tr'):
                name = element.find_element_by_css_selector('a').text
                description = element.find_elements_by_css_selector('td')[4].text
                self.project_cache.append(Project(name=name, description=description))
        return list(self.project_cache)

    def generate_new_name(self):
        names = [p.name for p in self.get_project_list()]
        new_name = random_string('name', 12).strip()
        while new_name in names:
            new_name = random_string('name', 12)
        return new_name
        # random_string
