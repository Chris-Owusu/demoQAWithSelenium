from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)

browser.get('https://demoqa.com/')
browser.maximize_window()

element = browser.find_element(By.CSS_SELECTOR, 'div.home-body > div > div:nth-child(1)').click()

action = ActionChains(browser)


# Elements
def textBoxPart():
    textBox = browser.find_element(By.CSS_SELECTOR, '#item-0').click()
    fullname = browser.find_element(By.CSS_SELECTOR, '#userName').send_keys('Christopher Owusu')
    email = browser.find_element(By.CSS_SELECTOR, '#userEmail').send_keys('chris@gmail.com')
    currAddress = browser.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys('23 newyork street')
    permAdress = browser.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys('24 manhattan street')
    submit = browser.find_element(By.CSS_SELECTOR, '#submit').click()

    info = browser.find_element(By.ID, 'output')
    print("Output displayed is: ", info.is_displayed())

def checkBoxPart():
    checkBox = browser.find_element(By.CSS_SELECTOR, '#item-1').click()
    home = browser.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > span > button').click()
    desktop = browser.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > ol > li:nth-child(1) > span > button').click()
    commads = browser.find_element(By.XPATH, "//label[@for='tree-node-commands']").click()
    document = browser.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > ol > li:nth-child(2) > span > button').click()
    workSpace = browser.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(1) > span > button').click()
    react = browser.find_element(By.XPATH, "//label[@for='tree-node-react']").click()
    veu = browser.find_element(By.XPATH, "//label[@for='tree-node-veu']").click()
    browser.implicitly_wait(5)
    office = browser.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(2) > span > button').click()
    private = browser.find_element(By.XPATH, "//label[@for='tree-node-private']").click()
    classified = browser.find_element(By.XPATH, "//label[@for='tree-node-classified']").click()
    download = browser.find_element(By.CSS_SELECTOR, '#tree-node > ol > li > ol > li:nth-child(3) > span > button').click()
    excel = browser.find_element(By.XPATH, "//label[@for='tree-node-excelFile']").click()

    result = browser.find_element(By.ID, '#result')
    assert result.text == "commands, react"
    print('CheckBox result exist?', result)

def radioBtnPart():
    radioBtn = browser.find_element(By.CSS_SELECTOR, '#item-2').click()
    impressive = browser.find_element(By.CSS_SELECTOR, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > div:nth-child(3)').click()

    output = browser.find_element(By.CSS_SELECTOR, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > p').is_displayed()
    print("Output of radio button is: ", output)

def webTablesPart():
    webTables = browser.find_element(By.CSS_SELECTOR, '#item-3').click()
    adddBtn = browser.find_element(By.CSS_SELECTOR, '#addNewRecordButton').click()
    fname = browser.find_element(By.CSS_SELECTOR, '#firstName').send_keys('Mark')
    lname = browser.find_element(By.CSS_SELECTOR, '#lastName').send_keys('Dan')
    email = browser.find_element(By.CSS_SELECTOR, '#userEmail').send_keys('markdan@gmail.com')
    age = browser.find_element(By.CSS_SELECTOR, '#age').send_keys('52')
    salary = browser.find_element(By.CSS_SELECTOR, '#salary').send_keys('5200')
    department = browser.find_element(By.CSS_SELECTOR, '#department').send_keys('Science')
    submit = browser.find_element(By.CSS_SELECTOR, '#submit').click()


    results = browser.find_element(By.XPATH, "(//div[@role='row'])[5]")
    assert results.text == 'Mark'
    
def buttonsPart():
    buttons = browser.find_element(By.CSS_SELECTOR, '#item-4').click()
    dbClick = browser.find_element(By.CSS_SELECTOR, '#doubleClickBtn')
    action.double_click(dbClick)
    rClick = browser.find_element(By.CSS_SELECTOR, '#rightClickBtn')
    action.context_click(rClick)
    action.perform()
    clickk = browser.find_element(By.XPATH, "(//button[normalize-space()='Click Me'])[1]").click()

    #assertions
    doubleClickMessage = browser.find_element(By.CSS_SELECTOR, '#doubleClickMessage')
    assert 'You have done a double click' == doubleClickMessage.text
    rightClickMessage = browser.find_element(By.CSS_SELECTOR, '#rightClickMessage')
    assert 'You have done a right click' == rightClickMessage.text
    dynamicClickMessage = browser.find_element(By.CSS_SELECTOR, '#dynamicClickMessage')
    assert 'You have done a dynamic click' == dynamicClickMessage.text

def linksPart():
    links = browser.find_element(By.ID, '#item-5').click()
    
    
def uploadandDownloadsPart():
    uploadandDownload = browser.find_element(By.XPATH, '//*[@id="item-7"]').click()
    assert "Upload and Download" == uploadandDownload.text

textBoxPart()
# checkBoxPart()
# radioBtnPart()
# webTablesPart()
# buttonsPart()
# linksPart()
# uploadandDownloadsPart()

#Forms
form = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[2]/span/div').click()

# browser.quit()