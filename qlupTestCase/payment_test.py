import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def browser():
    # Setup: Create a WebDriver instance
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver
    # Teardown: Quit the WebDriver instance
    driver.quit()


def test_payment(browser):
    # Navigate to the payment page
    browser.get("https://newapp-staging.qlub.cloud/qr/ae/dummy-checkout/90/_/_/1827c10c80?lang=en")

    # Click on 'View menu'
    browser.find_element(By.XPATH, "//a[normalize-space()='View menu']").click()

    # Click on 'Pay the bill'
    browser.find_element(By.XPATH, "//a[normalize-space()='Pay the bill']").click()

    # Click on 'Split bill'
    browser.find_element(By.XPATH, "//span[normalize-space()='Split bill']").click()

    # Click on Pay a custom amount
    browser.find_element(By.CSS_SELECTOR, "button[id='select-custom'] span[class='wrapper']").click()

    # Set amount 10 AED
    browser.find_element(By.ID, "fullWidth").send_keys("10")

    # Click confirm
    browser.find_element(By.XPATH, "//span[normalize-space()='Confirm']").click()

    # Click on Tip option and choose one
    time.sleep(3)
    browser.find_element(By.XPATH, "(//div[@class='MuiBox-root css-1tpu0u3'])[3]").click()

    # Enter information card
    card_number = browser.find_element(By.ID, "checkout-frames-card-number")
    card_number.send_keys("4242 4242 4242 4242")

    browser.find_element(By.ID, "checkout-frames-expiry-date").send_keys("02/26")
    browser.find_element(By.ID, "checkout-frames-cvv").send_keys("100")

    # Click on pay
    browser.find_element(By.XPATH, "//span[normalize-space()='Pay Now']").click()

    #verify redirect to successful payment page
    element= browser.find_element(By.XPATH,"(//p[@class='MuiTypography-root MuiTypography-body1 css-1dbb4wf'])[1]")
    element_text = element.text
    assert element_text == "Payment was successful!"
