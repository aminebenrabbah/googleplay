






def click_week():
    web.refresh()
    time.sleep(2)
    links = web.find_elements(by = By.TAG_NAME,value ='a')
    time.sleep(2)
    links[26].click()
    time.sleep(2)
    links = web.find_elements(by = By.TAG_NAME,value ='a')
    time.sleep(2)
    links[29].click()
    
