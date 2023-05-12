import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://newapp-staging.qlub.cloud/qr/ae/dummy-checkout/90/_/_/1827c10c80/invoice?lang=en&source=menuPage")
driver.implicitly_wait(15)
driver.maximize_window()
driver.find_element(By.ID ,"checkout-frames-card-number").send_keys("424242424242")


