from selenium import webdriver
import yaml


class ArgSet():
    ## 프로그램 상수
    CHROME_DRVIER_PATH = "../chromeDriver/chromedriver.exe"
    ## ------------------------------------------------------------------------------------------
    @classmethod
    def getSelenium(cls):
        chrome_option = webdriver.ChromeOptions()
        # ====================================================
        chrome_option.add_argument("headless")
        chrome_option.add_argument("window-size=1920x1080")
        chrome_option.add_argument("disable-gpu")
        # ====================================================

        chrome_driver = webdriver.Chrome(executable_path= ArgSet.CHROME_DRVIER_PATH, chrome_options =chrome_option)
        #chrome_driver = webdriver.Chrome(executable_path=ArgSet.CHROME_DRVIER_PATH)
        return chrome_driver