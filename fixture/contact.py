from model.contact import Contanct
import re

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
                all_phones=cells[5].text
                self.contact_cache.append(Contanct(firstname=firstname,lastname=lastname,id=id,all_phones_from_home_page=all_phones))
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


    def get_contact_info_from_edit_page(self,index):
        driver = self.app.driver
        self.open_contact_to_edit_by_index(index)
        firstname=driver.find_element_by_name("firstname").get_attribute("value")
        lastname=driver.find_element_by_name("lastname").get_attribute("value")
        id=driver.find_element_by_name("id").get_attribute("value")
        homephone=driver.find_element_by_name("home").get_attribute("value")
        workphone=driver.find_element_by_name("work").get_attribute("value")
        mobilephone=driver.find_element_by_name("mobile").get_attribute("value")
        secondaryphone=driver.find_element_by_name("phone2").get_attribute("value")

        return Contanct(firstname=firstname,lastname=lastname,homephone=homephone,mobilephone=mobilephone,workphone=workphone,secondaryphone=secondaryphone,id=id)


    def get_contact_from_view_page(self,index):
        driver = self.app.driver
        self.open_contact_view_by_index(index)
        text=driver.find_element_by_id("content").text
        homephone=re.search("H: (.*)",text).group(1)
        workphone=re.search("W: (.*)",text).group(1)
        mobilephone=re.search("M: (.*)",text).group(1)
        secondaryphone=re.search("P: (.*)",text).group(1)
        return Contanct(homephone=homephone, mobilephone=mobilephone,
                        workphone=workphone, secondaryphone=secondaryphone)
