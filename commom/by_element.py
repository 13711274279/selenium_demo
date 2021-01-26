import enum
from selenium.webdriver.common.by import By


class By_Element(enum.Enum):
    xpath = By.XPATH
    id = By.ID
    class_name = By.CLASS_NAME
    link_text = By.LINK_TEXT
    css_selector = By.CSS_SELECTOR
    tag_name = By.TAG_NAME
    name = By.NAME
    partial_link_text = By.PARTIAL_LINK_TEXT


class Location:

    @property
    def location(self):
        my_list = dict(map(lambda n: (n.name, n.value), By_Element))
        return my_list

# test = Browser()
# test.open_windows("http://hrmtestt.bndxqc.com/login")
# test.click_element(Location().location['class_name'], "ivu-btn-primary")
