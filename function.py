def Token_Taker(passport_no, city, type):

    from selenium import webdriver

    url = "https://feims.dofe.gov.np/Individual-Login"

    driver = webdriver.Chrome()
    driver.get(url)

    #passport no
    driver.set_window_size(920, 680)
    driver.find_element_by_id("txtPassportNo").send_keys(passport_no)
    driver.find_element_by_id("btnPassportNext").click()

    #password
    driver.find_element_by_name("lytA$ctl05$Password").send_keys("100")
    driver.find_element_by_name("lytA$ctl05$LoginButton").click()
    
    #edit profile
    driver.find_element_by_class_name("home-menu-item").click()

    #submit
    driver.find_element_by_xpath("/html/body/form[1]/div[4]/div[2]/div/div/div/div/div/div/div/div/div/div[3]/div[2]/div/div[1]/a[7]").click()

    #now the real shit gets started

    #swoghasada
    driver.find_element_by_id("chkAggrement").click()

    #checking whether online or offline and selecting branch
    if type == "office":
        
        
        driver.find_element_by_id('bt_office').click()
        driver.find_element_by_id('ddlBranchList').send_keys("BB")
        
        condition = True

        while condition:
            check_value = driver.find_element_by_xpath("/html/body/form[1]/div[4]/div[2]/div/div/div/div/div/div/div/div/div/div[3]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/span").text
            if check_value.strip() == "No Token Available for selected branch":
                driver.find_element_by_id('ddlBranchList').send_keys("BB")
                print("done")
            else:
                driver.find_element_by_xpath("/html/body/form[1]/div[4]/div[2]/div/div/div/div/div/div/div/div/div/div[3]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/span").click()
                driver.find_element_by_id("btnSubmitRequest").click()
                condition = False

    elif type == "online":
        driver.find_element_by_id("bt_Online").click()
        check_value = driver.find_element_by_xpath("/html/body/form[1]/div[4]/div[2]/div/div/div/div/div/div/div/div/div/div[3]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/span").text
        
        condition = True
        while condition:
            if check_value.strip() == "No Token Available for selected branch":
                driver.find_element_by_id('bt_office').click()
                driver.find_element_by_id("bt_Online").click()
            else:
                driver.find_element_by_xpath("/html/body/form[1]/div[4]/div[2]/div/div/div/div/div/div/div/div/div/div[3]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/span").click()
                driver.find_element_by_id("btnSubmitRequest").click()
                condition = False


passport = "08027730"
city = 'Biratnagar'
type = "online"

Token_Taker(passport, city, type)
        

   

    






