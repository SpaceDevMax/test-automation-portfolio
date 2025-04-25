from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

def test_login():

    #Initialize WebDriver with WebDriver Manager
    edgeBrowser = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    try:

        # Ópen browser and navigate to saucedemo login page 
        edgeBrowser.get('https://www.saucedemo.com/')

        # Wait until browser loads
        time.sleep(2)

        # Find input fields and button
        username_field = edgeBrowser.find_element(By.ID, "user-name")
        password_field = edgeBrowser.find_element(By.ID, "password")
        login_button = edgeBrowser.find_element(By.ID, "login-button")

        # Type in username and password
        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")

        # Click login button
        login_button.click()

        # Was login succesful?
        assert "inventory" in edgeBrowser.current_url, "Login failed!"

    except KeyboardInterrupt:
        # Close browser with Ctrl + C
        edgeBrowser.quit()

    finally:
        # Close browser even if there is a mistake
        edgeBrowser.quit()

if __name__ == '__main__':
    test_login()