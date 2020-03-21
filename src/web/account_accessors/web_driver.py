from selenium import webdriver


class WebDriver:
    def move_to_element(self, element, driver):
        webdriver.ActionChains(driver).move_to_element(element)\
            .click(element).perform()

    def move_to_and_click_element(self, element, driver):
        webdriver.ActionChains(driver).move_to_element(element)\
            .perform()