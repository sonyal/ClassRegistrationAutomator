import mechanize

try:
    br = mechanize.Browser()
    br.set_handle_robots(False)

    print("1")
    check = br.open("https://app.testudo.umd.edu/#/main/dropAdd?termId=202008")  # login url
    check = check.read().decode("utf-8")

    print ("5")
    if ("Central Authentication Service (CAS)" in check):
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