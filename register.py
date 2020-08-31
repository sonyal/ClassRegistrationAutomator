import mechanize

try:
    br = mechanize.Browser()
    br.set_handle_robots(False)

    print("1")
    soc = br.open("https://app.testudo.umd.edu/soc/search?courseId=CMSC420&sectionId=0201&termId=202008&_openSectionsOnly=on&creditCompare=&credits=&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on")
    
    if not "<span class=\"open-seats-count\">0</span>" in soc.read().decode("utf-8"):
        check = br.open("https://app.testudo.umd.edu/#/main/dropAdd?termId=202008")  

        if ("Central Authentication Service (CAS)" in check.read().decode("utf-8")):
            br.select_form(nr=0)
            br["j_username"] = user
            br["j_password"] = pswd
            br.submit()
            print(test.read())
        else:
            print(check)
except:
    print("sdfs")
    # br.find_link(text="Change Password")
    # req = br.click_link(text="Change Password")
    # br.open(req)  # opens the link to change FXall password

    # br.select_form(id="aso_search_form_anchor")
    # br["gs_taif50"] = "from:noah@techjobsforgood.com"
    # br.submit()  # submit form to change password on FXall site

    # f =     
    # except:
    #     print("unable to use gmail")