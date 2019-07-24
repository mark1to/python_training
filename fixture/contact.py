from model.contact import Contanct

class ContactHelper:

    def __init__(self,app):
        self.app=app


    def change_field_value(self,field_name,text):
        driver=self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    contact_cache=None

    def get_contact_list(self):
        if self.contact_cache is None:
            driver=self.app.driver
            self.app.open_home_page()
            self.contact_cache=[]
            for row in driver.find_elements_by_name("entry"):
                cells=row.find_elements_by_tag_name("td")
                firstname=cells[1].text
                lastname=cells[2].text
                id=cells[0].find_element_by_tag_name("input").get_attribute("value")
                self.contact_cache.append(Contanct(firstname=firstname,lastname=lastname,id=id))
        return  list(self.contact_cache)


    def open_contact_to_edit_by_index(self,index):
        driver=self.app.driver
        self.app.open_home_page()
        row=driver.find_elements_by_name("entry")[index]
        cell=row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()


    def open_contact_view_by_index(self,index):
        driver=self.app.driver
        self.app.open_home_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()