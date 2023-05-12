import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def browser():
    # Setup: Create a WebDriver instance
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver
    # Teardown: Quit the WebDriver instance
    driver.quit()


def test_payment(browser):
    # Navigate to the payment page
    driver.get("https://newapp-staging.qlub.cloud/qr/ae/dummy-checkout/90/_/_/1827c10c80?lang=en")

    # Click on 'View menu'
    driver.find_element(By.XPATH, "//a[normalize-space()='View menu']").click()

    # Click on 'Pay the bill'
    driver.find_element(By.XPATH, "//a[normalize-space()='Pay the bill']").click()

    # Click on 'Split bill'
    driver.find_element(By.XPATH, "//span[normalize-space()='Split bill']").click()

    # Click on Pay a custom amount
    driver.find_element(By.CSS_SELECTOR, "button[id='select-custom'] span[class='wrapper']").click()

    # Set amount 10 AED
    driver.find_element(By.ID, "fullWidth").send_keys("10")

    # Click confirm
    driver.find_element(By.XPATH, "//span[normalize-space()='Confirm']").click()

    # Click on Tip option and choose one
    time.sleep(3)
    driver.find_element(By.XPATH, "(//div[@class='TipInputs_tipScrollable__C3Zsu']/div)[3]").click()

    # Enter information card
    # EnterCardNumber
    driver.switch_to.frame("cardNumber")  # ıd
    card_number = driver.find_element(By.ID, "checkout-frames-card-number")
    card_number.send_keys("4242424242424242")
    driver.switch_to.default_content()
    time.sleep(2)
    # EnterExpiryDate
    driver.switch_to.frame("expiryDate")  # ıd
    expiry_date = driver.find_element(By.ID, "checkout-frames-expiry-date")
    expiry_date.send_keys("02/26")
    driver.switch_to.default_content()
    time.sleep(2)
    # EnterCvv
    driver.switch_to.frame("cvv")  # ıd
    cvv = driver.find_element(By.ID, "checkout-frames-cvv")
    cvv.send_keys("100")
    driver.switch_to.default_content()
    time.sleep(2)

    # Click on pay button
    driver.find_element(By.XPATH, "//button[@id='checkout-action-btn']").click()
    time.sleep(10)

    # verify redirect to successful payment page
    element = browser.find_element(By.XPATH, "//p[contains(text(),'Payment was successful!')]")
    element_text = element.text
    assert element_text == "Payment was successful!"
