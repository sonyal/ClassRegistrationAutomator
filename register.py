from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time 

user = "USERNAME"
pswd = "PASSWORD"
soc = "link to UMD schedule of classes site with course info"


options = FirefoxOptions()
options.add_argument("--headless")
profile_path = 'C:\\Users\\Sonya\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\3z5offf7.default-release'
profile = webdriver.FirefoxProfile(profile_path)
driver = webdriver.Firefox(profile, options=options)
driver.get(soc)

if not driver.find_element_by_class_name("open-seats-count").text == 0:
    driver.get('https://voice.google.com/u/4/calls')

    time.sleep(3)
    
    driver.execute_script("window.open('https://app.testudo.umd.edu/#/main/dropAdd?termId=202008');")
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    
    driver.implicitly_wait(15) 

    username = driver.find_element_by_id("username")
    username.clear()
    username.send_keys(user)

    password = driver.find_element_by_id("password")
    password.clear()
    password.send_keys(pswd)

    driver.find_element_by_name("_eventId_proceed").click()

    driver.implicitly_wait(10)
    
    windows = driver.window_handles
    driver.switch_to.window(windows[0])

    driver.implicitly_wait(35)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/div/div/gv-call-response/div/div/button').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/div/div/div[1]/div[2]/gv-in-call-button-panel/div/div/gv-in-call-button-ng2[4]/div/button').click()
    time.sleep(7)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/div/div/div[2]/gv-dtmf-input/div[2]/gv-dialpad/div/div[1]/div[1]/div').click()

    windows = driver.window_handles
    driver.switch_to.window(windows[1])



    driver.get('https://app.testudo.umd.edu/#/main/dropAdd?termId=202008')
    driver.find_element_by_link_text("Fall 2020").click()
    driver.find_element_by_class_name("drop-add-table-course-input ng-pristine ng-valid ng-valid-maxlength drop-add-table-course-input-margin common-uppercase ng-touched").send_keys("PSYC123")
    driver.find_element_by_class_name("drop-add-table-section-input ng-pristine ng-valid ng-valid-maxlength common-uppercase ng-touched").send_keys("0201")
    driver.find_element_by_id("submit_changes").click()
    driver.quit()
