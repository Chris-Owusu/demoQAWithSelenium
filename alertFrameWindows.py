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

class browserWindowClass:
    def __init__(self):
        pass

    # browserWindows = browser.find_element(By.XPATH, '//li[span[text()="Browser Windows"]]').click()

    def newTabElement(): 

    # newTable = browser.find_element(By.CSS_SELECTOR, "#tabButton").click()
        waited = wait(browser, 10)
    # Store the ID of the original window
        original_window = browser.current_window_handle

        # Check we don't have other windows open already
        assert len(browser.window_handles) == 1

        # Click the link which opens in a new window
        browser.find_element(By.CSS_SELECTOR, "#tabButton").click()

        # wait.until(EC.number_of_windows_to_be(2))

    

    # Loop through until we find a new window handle
        for window_handle in browser.window_handles:
            if window_handle != original_window:
                browser.switch_to.window(window_handle)
                break
        
        # wait.until(EC.title_is("This is a sample page"))
            
        assert browser.current_url=='https://demoqa.com/sample'
        print(browser.current_url)
        browser.switch_to.window(original_window)
        browser.implicitly_wait(5)
        assert 'https://demoqa.com/' in browser.current_url
        print(browser.current_url)


    def newWindowElement():
            newWindow = browser.find_element(By.CSS_SELECTOR, '#windowButton').click()
                # Access each dimension individually
            x = browser.get_window_position().get('x')
            y = browser.get_window_position().get('y')

            print(x)
            print(y)

            assert 'https://demoqa.com/browser-windows' in browser.current_url

    def newWindowMessageElement():
        newWindowMessage = browser.find_element(By.CSS_SELECTOR, '#messageWindowButton').click()
        assert browser.current_url == "https://demoqa.com/browser-windows"
        print(browser.current_url)

    # newTabElement()
    # newWindowElement()
    # newWindowMessageElement()

class alertClass:
    def __init__(self, browser):
        self.browser = browser

    # browser.find_element(By.XPATH, "(//li[@id='item-1'])[2]").click()
     
    def alert():
        browser.find_element(By.CSS_SELECTOR, '#alertButton').click()

        alert = wait(browser, 10).until(EC.alert_is_present())
        text = alert.text
        assert text == "You clicked a button"
        alert.accept()

    def timerAlert():
        browser.find_element(By.CSS_SELECTOR, '#timerAlertButton').click()
        browser.implicitly_wait(5000)
        alert = wait(browser, 10).until(EC.alert_is_present())
        text = alert.text
        assert text == "This alert appeared after 5 seconds"
        alert.accept()

    def confirmBoxClickCancel():
        browser.find_element(By.CSS_SELECTOR, '#confirmButton').click()

        wait(browser, 10).until(EC.alert_is_present())

        alert = browser.switch_to.alert
        text = alert.text
        assert text == "Do you confirm action?"
        alert.dismiss()

        confirmResult = browser.find_element(By.CSS_SELECTOR, "#confirmResult").text
        # confirmResult.is_displayed()
        print(confirmResult)
        assert confirmResult == "You selected Cancel"

    def confirmBoxClickOk():
        browser.find_element(By.CSS_SELECTOR, '#confirmButton').click()

        wait(browser, 10).until(EC.alert_is_present())

        alert = browser.switch_to.alert
        text = alert.text
        assert text == "Do you confirm action?"
        alert.accept()

        confirmResultOk = browser.find_element(By.CSS_SELECTOR, "#confirmResult").text
        # confirmResult.is_displayed()
        print(confirmResultOk)
        assert confirmResultOk == "You selected Ok"

    def promtButton():
        browser.find_element(By.CSS_SELECTOR, '#promtButton').click()
        wait(browser, 10).until(EC.alert_is_present())

        alert = browser.switch_to.alert
        alert.send_keys("Selenium")
        alert.accept()

        promptResult = browser.find_element(By.CSS_SELECTOR, "#promptResult").is_displayed()
        assert promptResult == True

    # alert()
    # timerAlert()
    # confirmBoxClickCancel()
    # confirmBoxClickOk()
    # promtButton()

class frameClass:
    def __init__(self):
        pass

    browser.find_element(By.CSS_SELECTOR, "#item-2").click()
    
    def bigFrame():
        browser.find_element(By.CSS_SELECTOR, "#frame1").is_displayed()



    def smallFrame():
        browser.find_element(By.CSS_SELECTOR, "#frame2").is_displayed()
    

    bigFrame()
    smallFrame()

    
        






browser.quit()