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

# element = browser.find_element(By.CSS_SELECTOR, 'div.home-body > div > div:nth-child(1)').click()
formSection = browser.find_element(By.CSS_SELECTOR, 'div.home-body > div > div:nth-child(2)').click()

action = ActionChains(browser)

#Forms
practiceForm = browser.find_element(By.XPATH, "(//li[@id='item-0'])[2]").click()
first_name = browser.find_element(By.CSS_SELECTOR, '#firstName').send_keys('Christopher')
last_name = browser.find_element(By.CSS_SELECTOR, '#lastName').send_keys('Owusu')
email = browser.find_element(By.CSS_SELECTOR, '#userEmail').send_keys('co@gmail.com')
gender = browser.find_element(By.CSS_SELECTOR, '#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(3)').click()
number = browser.find_element(By.CSS_SELECTOR, '#userNumber').send_keys('0243111990')
dateOfBirthInpu = browser.find_element(By.CSS_SELECTOR, '#dateOfBirthInput').click()
month = browser.find_element(By.XPATH, '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select').send_keys('oct')
year = browser.find_element(By.XPATH, '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select').send_keys('2000')
day = browser.find_element(By.XPATH, '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/div[2]').click()
subject = browser.find_elements(By.XPATH, "(//div[@class='subjects-auto-complete__value-container subjects-auto-complete__value-container--is-multi css-1hwfws3'])[1]").send_keys('Com')
# subject
for elem in subject:
    print(elem)
# gender1 = browser.find_element(By.CSS_SELECTOR, '#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(1)').click()
# gender2 = browser.find_element(By.CSS_SELECTOR, '#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(3)').click()
# picture = browser.find_element(By.CSS_SELECTOR, "#uploadPicture").send_keys('C:\\Users\\ChristopherOwusuAhen\\Desktop\\catman.png')
# currAddress = browser.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys('23 newyork street')
# state = browser.find_element(By.XPATH, "//div[@id='state']").send_keys('har', Keys.ENTER)






browser.quit()