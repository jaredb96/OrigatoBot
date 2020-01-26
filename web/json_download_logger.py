from .logger import Logger
import time
from selenium import webdriver
import datetime
from datetime import timedelta
from selenium.webdriver.common.keys import Keys
from web.logger import HEADLESS
from utils.config import CONFIGS
import os

class JsonDownloadLogger(Logger):
    def __init__(self):
        None

    def download_recent_message_data(self):
        # download message data between yesterday and today
        end_date = datetime.datetime.now()
        start_date = end_date - timedelta(1)

        self.download_message_data(start_date, end_date)

    def download_message_data(self, start_date, end_date):
        start_year = start_date.year
        start_month = start_date.month
        start_day = start_date.day

        end_year = end_date.year
        end_month = end_date.month
        end_day = end_date.day

        driver = Logger.login(self, "https://www.facebook.com/settings?tab=your_facebook_information")

        # maximize window
        driver.maximize_window()

        # wait for page to load
        time.sleep(10)

        # if not headless, popover obscures focus of screen
        if not HEADLESS:
            # click screen to focus
            screen_block = driver.find_element_by_xpath("//*[@class='_3ixn']")
            screen_block.click()

        # redirect via "download your information" option
        download_your_information = driver.find_elements_by_xpath("//*[@class='fbSettingsListLink clearfix pvm phs']")[1]
        download_your_information.click()

        # wait for page to load
        time.sleep(10)

        # select 'JSON/HTML' dropdown menu
        format_dropdown_menu = \
            driver.find_elements_by_xpath("//*[@class='_p _55pi _2agf _4o_4 _4jy0 _4jy5 _517h _51sy _42ft']")[0]
        format_dropdown_menu.click()
        json_option = driver.find_elements_by_xpath("//*[@class='_54nh']")[1]
        json_option.click()

        time.sleep(5)

        # deselect all
        elmnt = driver.find_element_by_xpath("//*[contains(text(), 'Deselect All')]")
        elmnt.send_keys(Keys.ENTER)

        # get messages checkbox
        elmnts = driver.find_elements_by_xpath("//*[@class='_3qn7 _61-3 _2fyi _3qng']")
        msg_elmnt = elmnts[7]
        msg_elmnt = msg_elmnt.find_element_by_class_name('_1gcq._29c-._1gco._5e9w')

        # click messages checkbox
        webdriver.ActionChains(driver).move_to_element(msg_elmnt).click(msg_elmnt).perform()

        time.sleep(3)

        # move to top of screen, use top header text as anchor point
        top_text = driver.find_element_by_xpath("//*[@class='_2pi0 _4-u2  _4-u8']")
        webdriver.ActionChains(driver).move_to_element(top_text).perform()

        # click date range block
        date_block = driver.find_element_by_xpath("//*[@class='_55pi _2agf _4o_4 _4jy0 _4jy5 _517h _51sy _42ft']")
        date_block.click()

        # select start year
        year_dropdown_elmnt = driver.find_elements_by_xpath \
            ("//*[@class='_2-cs _p _55pi _2agf _4o_4 _4jy0 _4jy3 _517h _51sy _42ft']")[0]
        year_dropdown_elmnt.click()

        # get today's date
        dt = datetime.datetime.today()
        curr_year = dt.year
        curr_month = dt.month
        curr_day = dt.day

        if start_year != curr_year-1:
            if start_year == curr_year:
                yesterday_year_elmnt = driver.find_elements_by_xpath("//*[@class='_54ni __MenuItem']")[1]
            else:
                yesterday_year_elmnt = driver.find_elements_by_xpath("//*[@class='_54ni __MenuItem']")[(curr_year-start_year)]
            yesterday_year_elmnt.click()
        else:
            year_dropdown_elmnt.click()

        # select start month
        month_dropdown_elmnt = driver.find_elements_by_xpath \
            ("//*[@class='_2-cp _p _55pi _2agf _4o_4 _4jy0 _4jy3 _517h _51sy _42ft']")[0]
        month_dropdown_elmnt.click()
        start_month_elmnt = driver.find_elements_by_xpath("//*[@class='_54nc']")[19+(start_month-1)]
        start_month_elmnt.click()

        # select start day
        start_xpath = "//*[@data-testid='day_option_" + str(start_day) + "']"
        num_block = driver.find_elements_by_xpath(start_xpath)[0]
        num_block.click()

        time.sleep(1)

        # select curr year
        year_dropdown_elmnt = driver.find_elements_by_xpath \
            ("//*[@class='_2-cs _p _55pi _2agf _4o_4 _4jy0 _4jy3 _517h _51sy _42ft']")[0]
        year_dropdown_elmnt.click()
        if end_year != start_year:
            curr_year_elmnt = driver.find_elements_by_xpath("//*[@class='_54ni __MenuItem']")[29+((curr_year-1)-end_year)]
            curr_year_elmnt.click()
        else:
            year_dropdown_elmnt.click()

        time.sleep(1)

        # select curr month
        month_dropdown_elmnt = driver.find_elements_by_xpath \
            ("//*[@class='_2-cp _p _55pi _2agf _4o_4 _4jy0 _4jy3 _517h _51sy _42ft']")[0]
        month_dropdown_elmnt.click()

        if start_month != end_month and start_month != curr_month:
            curr_month_elmnt = driver.find_elements_by_xpath("//*[@class='_54nc']")[48+end_month-1]
            curr_month_elmnt.click()
        else:
            month_dropdown_elmnt.click()

        # select current day
        end_xpath = "//*[@data-testid='day_option_" + str(end_day) + "']"
        num_block = driver.find_elements_by_xpath(end_xpath)[1]
        num_block.click()

        time.sleep(1)

        # click ok
        ok_button = driver.find_element_by_xpath("//*[@class='_4jy0 _4jy3 _4jy1 _51sy selected _42ft']")
        ok_button.click()

        time.sleep(2)

        # click create file
        create_file_button = driver.find_element_by_xpath("//*[@data-testid='dyi/sections/create']")
        create_file_button.click()

        time.sleep(1)

        # click 'available copies'
        available_copies_button = driver.find_element_by_xpath("//*[@data-testid='dyi/navigation/all_archives']")
        driver.execute_script("window.scrollTo(0, 0)")
        available_copies_button.click()

        print('waiting for files to be ready...')

        # wait for file to be ready for download
        files_ready = False
        while not files_ready:
            try:
                download_ready_notif = driver.find_element_by_xpath("//*[@class='_3soj clearfix']")

                expected_inner_text_value = 'Your Facebook information file is ready to download.\na few seconds ago'
                if download_ready_notif.get_attribute("innerText") == expected_inner_text_value:
                    files_ready = True
            except:
                continue

        time.sleep(2)

        # refresh page
        driver.refresh()

        # wait for refresh to complete
        time.sleep(5)

        # if not headless, popover obscures focus of screen
        if not HEADLESS:
            # click screen to focus
            screen_block = driver.find_element_by_xpath("//*[@class='_3ixn']")
            screen_block.click()

        # click download button
        download_button = driver.find_element_by_xpath("//*[@data-testid='dyi/archives/download/1']")
        download_button.click()

        print('waiting for download to complete...')

        # wait to allow download to complete
        path_to_zip_file = CONFIGS['downloads_directory'] + CONFIGS['zipfile_name']
        zip_file_ready = os.path.exists(path_to_zip_file)
        while not zip_file_ready:
            zip_file_ready = os.path.isfile(path_to_zip_file)

        print('download complete! closing...')
        time.sleep(3)

        driver.quit()
