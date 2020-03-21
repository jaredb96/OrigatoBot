from . import driver


class ElementClicker:
    def __init__(self):
        self.driver
        pass

    def find_and_click_elements(self, elements, method_flags):
        raise NotImplementedError

    def find_and_click_element(self, element):

        raise NotImplementedError

    def find_and_click_element_with_check(self, element):
        raise NotImplementedError