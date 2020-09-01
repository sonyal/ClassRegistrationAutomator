from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
options.add_argument("--headless")
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
driver = webdriver.Firefox(options=options,firefox_binary=binary, executable_path=r'D:\\txtbk\\Personal\\geckodriver-v0.27.0-win64\\geckodriver.exe')
driver.get("https://app.testudo.umd.edu/soc/search?courseId=PSYC123&sectionId=0201&termId=202008&openSectionsOnly=true&_openSectionsOnly=on&creditCompare=&credits=&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on")

if not driver.find_element_by_class_name("open-seats-count").text == 0:
    driver.get("https://app.testudo.umd.edu/#/main/dropAdd?termId=202008")

    if "Central Authentication Service (CAS)" in driver.page_source:
        driver.find_element_by_id("username").send_keys(user)
        driver.find_element_by_id ("password").send_keys(pswd)
        driver.find_element_by_class_name("form-element form-button").click()
    
    driver.find_element_by_class_name("secondary-button ng-binding ng-scope").click()
