import functools
from selenious import WebDriverMixin
from selenium.common.exceptions import NoSuchElementException


def mock_fe(self, name, *args, **kwargs):
    if self.returns:
        index = min(len(self.returns) - 1, len(self.calls))
        retval = self.returns[index]
    elif name.startswith("find_elements"):
        retval = [True]
    else:
        retval = True

    self.calls.append({"name": name, "args": args, "kwargs": kwargs, "retval": retval})

    if retval == NoSuchElementException:
        raise NoSuchElementException
    
    return retval
        
class MockWebDriver():
    def __init__(self, returns=None):
        self.returns = returns
        self.calls = []

    def find_element_by_id(self, *args, **kwargs):
        return mock_fe(self, "find_element_by_id", *args, **kwargs)
    
    def find_elements_by_id(self, *args, **kwargs):
        return mock_fe(self, "find_elements_by_id", *args, **kwargs)
    
    def find_element_by_xpath(self, *args, **kwargs):
        return mock_fe(self, "find_element_by_xpath", *args, **kwargs)
    
    def find_elements_by_xpath(self, *args, **kwargs):
        return mock_fe(self, "find_elements_by_xpath", *args, **kwargs)
    
    def find_element_by_link_text(self, *args, **kwargs):
        return mock_fe(self, "find_element_by_link_text", *args, **kwargs)
    
    def find_elements_by_link_text(self, *args, **kwargs):
        return mock_fe(self, "find_elements_by_link_text", *args, **kwargs)
    
    def find_element_by_partial_link_text(self, *args, **kwargs):
        return mock_fe(self, "find_element_by_partial_link_text", *args, **kwargs)
    
    def find_elements_by_partial_link_text(self, *args, **kwargs):
        return mock_fe(self, "find_elements_by_partial_link_text", *args, **kwargs)
    
    def find_element_by_name(self, *args, **kwargs):
        return mock_fe(self, "find_element_by_name", *args, **kwargs)
    
    def find_elements_by_name(self, *args, **kwargs):
        return mock_fe(self, "find_elements_by_name", *args, **kwargs)
    
    def find_element_by_tag_name(self, *args, **kwargs):
        return mock_fe(self, "find_element_by_tag_name", *args, **kwargs)
    
    def find_elements_by_tag_name(self, *args, **kwargs):
        return mock_fe(self, "find_elements_by_tag_name", *args, **kwargs)
    
    def find_element_by_class_name(self, *args, **kwargs):
        return mock_fe(self, "find_element_by_class_name", *args, **kwargs)
    
    def find_elements_by_class_name(self, *args, **kwargs):
        return mock_fe(self, "find_elements_by_class_name", *args, **kwargs)
    
    def find_element_by_css_selector(self, *args, **kwargs):
        return mock_fe(self, "find_element_by_css_selector", *args, **kwargs)
    
    def find_elements_by_css_selector(self, *args, **kwargs):
        return mock_fe(self, "find_elements_by_css_selector", *args, **kwargs)
    
    def find_element(self, *args, **kwargs):
        return mock_fe(self, "find_element", *args, **kwargs)
    
    def find_elements(self, *args, **kwargs):
        return mock_fe(self, "find_elements", *args, **kwargs)

class MockDriver(WebDriverMixin, MockWebDriver):
    pass
