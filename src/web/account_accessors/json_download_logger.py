from .logger import Logger
import time
from selenium import webdriver
import datetime
from datetime import timedelta
from selenium.webdriver.common.keys import Keys
from web.logger import HEADLESS
import os
import zipfile
import platform
import os.path
import shutil
from setup.load_global_configs import CONFIGS
from bs4 import BeautifulSoup


class JsonDownloadLogger(Logger):
    def __init__(self):
        None

    def download_weekly_message_data(self):
        # download message data between today and 7 days ago
        end_date = datetime.datetime.now()
        start_date = end_date - timedelta(7)

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
        self.sleep_up_to_5_secs()

        json_option = driver.find_elements_by_xpath("//*[@class='_54nh']")[1]
        json_option.click()

        self.sleep_up_to_5_secs()

        # deselect all
        elmnt = driver.find_element_by_xpath("//*[contains(text(), 'Deselect All')]")
        elmnt.send_keys(Keys.ENTER)

        # get messages checkbox
        elmnts = driver.find_elements_by_xpath("//*[@class='_3qn7 _61-3 _2fyi _3qng']")
        msg_elmnt = elmnts[7]
        msg_elmnt = msg_elmnt.find_element_by_class_name('_1gcq._29c-._1gco._5e9w')

        # click messages checkbox
        webdriver.ActionChains(driver).move_to_element(msg_elmnt).click(msg_elmnt).perform()

        self.sleep_up_to_5_secs()

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

        self.sleep_up_to_5_secs()

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

        self.sleep_up_to_5_secs()

        # select curr year
        year_dropdown_elmnt = driver.find_elements_by_xpath \
            ("//*[@class='_2-cs _p _55pi _2agf _4o_4 _4jy0 _4jy3 _517h _51sy _42ft']")[0]
        year_dropdown_elmnt.click()
        if end_year != start_year:
            curr_year_elmnt = driver.find_elements_by_xpath("//*[@class='_54ni __MenuItem']")[29+((curr_year-1)-end_year)]
            curr_year_elmnt.click()
        else:
            year_dropdown_elmnt.click()

        self.sleep_up_to_5_secs()

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

        self.sleep_up_to_5_secs()

        # click ok
        ok_button = driver.find_element_by_xpath("//*[@class='_4jy0 _4jy3 _4jy1 _51sy selected _42ft']")
        ok_button.click()

        self.sleep_up_to_5_secs()

        # click create file
        create_file_button = driver.find_element_by_xpath("//*[@data-testid='dyi/sections/create']")
        create_file_button.click()

        self.sleep_up_to_5_secs()

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

        self.sleep_up_to_5_secs()

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
        self.sleep_up_to_5_secs()

        driver.quit()

    def unzip_message_data(self):
        print('unzipping downloaded files...')
        downloads_directory = CONFIGS['downloads_directory']
        zipfile_name = CONFIGS['zipfile_name']
        path_to_zip_file = downloads_directory + zipfile_name

        destination_directory = os.getcwd()
        with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
            zip_ref.extractall(destination_directory)

        origato_media_directory_name = self.get_origato_media_directory_name()
        self.__convert_all_mp4_files_to_mp3(
            destination_directory + '/messages/inbox/' + origato_media_directory_name + '/audio'
        )

    def get_origato_directory_name_windows(self):
        origato_chat_name = ""
        for directory_name in os.listdir('messages/inbox'):
            if 'ORIGATO' in directory_name.upper() and 'ORIGATORESURRECTED' not in directory_name.upper():
                origato_chat_name = directory_name
        return origato_chat_name

    def get_origato_media_directory_name(self):
        # windows media/messages directory are the same
        if platform.system() == 'Windows':
            return self.get_origato_directory_name_windows()

        # linux (and Mac?) downloads store media in directory with uppercase chat name
        elif platform.system() == 'Linux' or platform.system() == 'Darwin':
            for directory_name in os.listdir('messages/inbox'):
                if 'ORIGATO' in directory_name and 'ORIGATORESURRECTED' not in directory_name:
                    return directory_name

        # default, should never reach
        return ''

    def get_origato_messages_directory_name(self):
        # windows media/messages directory are the same
        if platform.system() == 'Windows':
            return self.get_origato_directory_name_windows()

        # linux (and Mac?) downloads store messages in directory with lowercase chat name
        elif platform.system() == 'Linux' or platform.system() == 'Darwin':
            for directory_name in os.listdir('messages/inbox'):
                if 'origato' in directory_name and 'origatoresurrected' not in directory_name:
                    return directory_name

        # default, should never reach
        return ''

    def get_relative_path_to_messages_jsons(self):
        origato_messages_directory_name = self.get_origato_messages_directory_name()

        relative_path_to_messages_json = 'messages/inbox/' + origato_messages_directory_name + '/'
        return relative_path_to_messages_json

    def __convert_all_mp4_files_to_mp3(self, path):
        if not os.path.exists(path):
            return
        print('converting audio files from mp4 to mp3...')
        for filename in os.listdir(path):
            base_file, ext = os.path.splitext(filename)
            if ext == ".mp4":
                os.rename(path + '/' + filename, path + '/' + base_file + ".mp3")

    def downloads_cleanup(self):
        download_dir = CONFIGS['downloads_directory']
        zipfile_name = CONFIGS['zipfile_name']
        path_to_zip_file = download_dir + zipfile_name

        if os.path.exists(path_to_zip_file):
            os.remove(path_to_zip_file)

        path_to_messages_folder = os.getcwd() + '/messages'
        if os.path.exists(path_to_messages_folder):
            shutil.rmtree(path_to_messages_folder)

    # useful function for debugging, prints html of an element grabbed by selenium/other web scrapers
    def pretty_print_html_element(block):
        html_string = block.get_attribute('outerHTML')
        print(BeautifulSoup(html_string, 'html.parser').prettify())
