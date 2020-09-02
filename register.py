from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time 

options = FirefoxOptions()
options.add_argument("--headless")
# options.set_preference("media.navigator.permission.disabled", True)
profile_path = 'C:\\Users\\Sonya\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\3z5offf7.default-release'
profile = webdriver.FirefoxProfile(profile_path)
# profile.set_preference ('media.navigator.permission.disabled', True)
# profile.update_preferences()
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
# driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary, executable_path=r'D:\\txtbk\\Personal\\geckodriver-v0.27.0-win64\\geckodriver.exe')
driver = webdriver.Firefox(profile)
driver.get("https://app.testudo.umd.edu/soc/search?courseId=PSYC123&sectionId=0201&termId=202008&openSectionsOnly=true&_openSectionsOnly=on&creditCompare=&credits=&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on")

if not driver.find_element_by_class_name("open-seats-count").text == 0:
    # # driver.get('https://app.testudo.umd.edu/#/main/dropAdd?termId=202008')
    # driver.get('https://accounts.google.com/o/oauth2/auth?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile+email&redirect_uri=https%3a%2f%2fstackauth.com%2fauth%2foauth2%2fgoogle&state=%7b%22sid%22%3a1%2c%22st%22%3a%2259%3a3%3abbc%2c16%3a1c7148b72535a42b%2c10%3a1598933217%2c16%3a6e7de9a258d53579%2c014514bb93b101c568ead01903051d2a7bcdeffac9580fa8da270fe1c9644ed8%22%2c%22cdl%22%3anull%2c%22cid%22%3a%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2c%22k%22%3a%22Google%22%2c%22ses%22%3a%22bff02d4fdcfa445582582435a398c3bf%22%7d&response_type=code')

    # username = driver.find_element_by_id("identifierId")
    # username.send_keys(v_user)
    # driver.find_element_by_id("identifierNext").click()

    # error occurs here
    # set password
    time.sleep(2)
    # password = driver.find_element_by_name("password")
    # password.send_keys(v_pswd)
    # driver.find_element_by_id("passwordNext").click()
  
    # driver.implicitly_wait(2) 

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

    driver.implicitly_wait(30)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/div/div/gv-call-response/div/div/button').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/div/div/div[1]/div[2]/gv-in-call-button-panel/div/div/gv-in-call-button-ng2[4]/div/button').click()
    time.sleep(6)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/div/div/div[2]/gv-dtmf-input/div[2]/gv-dialpad/div/div[1]/div[1]/div').click()
    
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    
    driver.get('https://app.testudo.umd.edu/#/main/dropAdd?termId=202008')
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[4]/div[2]/div[2]/div/div[1]/div/div[2]/button").click()
    driver.find_element_by_xpath("/html/body/div/div/div[4]/div[2]/div[2]/div/div[3]/form/table/tbody/tr[6]/td[2]/input").send_keys("PSYC123")
    driver.find_element_by_class_name("/html/body/div/div/div[4]/div[2]/div[2]/div/div[3]/form/table/tbody/tr[6]/td[3]/input").send_keys("0201")
    driver.find_element_by_xpath("//*[@id=\"submit_changes\"]").click()
    # driver.quit()

        # frame = driver.find_element_by_xpath('//*[@id="duo_iframe"]')
        # driver.switch_to.frame(frame)
        # driver.find_element_by_css_selector('.device-select-wrapper > select:nth-child(1) > option:nth-child(4)').click()
        # frame = driver.find_element_by_xpath('//*[@id="duo_iframe"]')
        # driver.switch_to.frame(frame)
        # driver.find_element_by_css_selector('#auth_methods > fieldset:nth-child(4) > div:nth-child(2) > button:nth-child(3)').click()

    
  
    # driver.find_element_by_class_name('grid--cell s-btn s-btn__icon s-btn__google bar-md ba bc-black-3').click()
    
    # driver.implicitly_wait(15) 
    # time.sleep(2)
    

    # driver.quit()
    # 
    #     driver.execute_script("window.open('https://accounts.google.com/signin/v2/identifier?service=grandcentral&passive=1209600&continue=https%3A%2F%2Fvoice.google.com%2Fsignup&followup=https%3A%2F%2Fvoice.google.com%2Fsignup&flowName=GlifWebSignIn&flowEntry=ServiceLogin');")
        
    #     windows = driver.window_handles

    #     time.sleep(3)
    #     driver.switch_to.window(windows[1])
    #     print(driver.page_source)
    #     driver.find_element_by_id("identifierId").send_keys(v_user)
    #     driver.find_element_by_


    # # print(driver.page_source)



    # driver.find_element_by_link_text("Fall 2020").click()
    # driver.find_element_by_class_name("drop-add-table-course-input ng-pristine ng-valid ng-valid-maxlength drop-add-table-course-input-margin common-uppercase ng-touched").send_keys("PSYC123")
    # driver.find_element_by_class_name("drop-add-table-section-input ng-pristine ng-valid ng-valid-maxlength common-uppercase ng-touched").send_keys("0201")
    # driver.find_element_by_id("submit_changes").click()
    # driver.quit()
