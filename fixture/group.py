from model.group import Group


class GroupHelper:


    def __init__(self,app):
        self.app=app


    def open_groups_page(self):
        driver=self.app.driver
        if not(driver.current_url.endswith("/group.php") and len(driver.find_elements_by_name("new"))>0):
            driver.find_element_by_link_text("groups").click()


    def create(self, group):
        driver=self.app.driver
        self.open_groups_page()
        #init group creating
        driver.find_element_by_name("new").click()
        #fill group form
        self.fill_group_form(group)
        #submit group creation
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        driver = self.app.driver
        self.change_filed_value("group_name", group.name)
        self.change_filed_value("group_header", group.header)
        self.change_filed_value("group_footer", group.footer)


    def change_filed_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group()
        #submit deletion
        driver.find_element_by_name("delete").click()
        self.return_to_groups_page()


    def select_first_group(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()


    def modify_first_group(self,new_group_data):
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group()
        #open modification form
        driver.find_element_by_name("edit").click()
        #fill group form
        self.fill_group_form(new_group_data)
        #submit notification
        driver.find_element_by_name("update").click()
        self.return_to_groups_page()


    def return_to_groups_page(self):
        driver=self.app.driver
        driver.find_element_by_link_text("group page").click()


    def count(self):
        driver=self.app.driver
        self.open_groups_page()
        return len(driver.find_elements_by_name("selected[]"))

    def get_group_list(self):
        driver=self.app.driver
        self.open_groups_page()
        groups=[]
        for i in driver.find_elements_by_css_selector("span.group"):
            text = i.text
            id = i.find_element_by_name("selected[]").get_attribute("value")
            groups.append(Group(name=text,id=id))
        return groups