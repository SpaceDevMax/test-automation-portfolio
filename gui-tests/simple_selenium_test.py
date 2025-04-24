from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

def test_login():

    #Initialize WebDriver with WebDriver Manager
    edgeBrowser = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    try:

        # open browser and navigate to saucedemo login page 
        edgeBrowser.get('https://www.saucedemo.com/')

        time.sleep(5)

    except KeyboardInterrupt:
        # Close browser with Ctrl + C
        edgeBrowser.quit()

    finally:
        # Close browser even if there is a mistake
        edgeBrowser.quit()

if __name__ == '__main__':
    test_login()