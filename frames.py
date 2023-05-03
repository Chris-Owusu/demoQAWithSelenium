from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)

browser.get('https://demoqa.com/')
browser.maximize_window()

alertsTab = browser.find_element(By.XPATH, "(//div[@class='card mt-4 top-card'])[3]").click()


action = ActionChains(browser)
browser.implicitly_wait(5000)
browser.find_element(By.CSS_SELECTOR, "//div[@class='element-list collapse show']//li[@id='item-2']").click()


def bigFrame():
    browser.find_element(By.CSS_SELECTOR, "#frame1").is_displayed()

def smallFrame():
    browser.find_element(By.CSS_SELECTOR, "#frame2").is_displayed()

# bigFrame()
# smallFrame()

    
        






# browser.quit()