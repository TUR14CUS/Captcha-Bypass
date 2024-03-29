import undetected_chromedriver as uc
from twocaptcha import TwoCaptcha
import time

def solve_captcha(web):
    driver = uc.Chrome()
    driver.get(web)

    # Get site key
    sitekey = driver.find_element(by='id', value='recaptcha-demo').get_attribute('data-sitekey')
    print(f"Site Key: {sitekey}")

    api_key = "YOUR_API"
    solver = TwoCaptcha(api_key)
    print("Solving captcha...")
    response = solver.recaptcha(sitekey=sitekey, url=web)

    print(f'Captcha Key: {response["code"]}')

    # Send Captcha Key to form
    driver.execute_script("document.getElementById('g-recaptcha-response').value = '{}';".format(response["code"]))

    # Click Submit
    driver.find_element(by='xpath', value='//*[@id="recaptcha-demo-submit"]').click()

    time.sleep(5)

# Usage example
web = input("Enter URL: ")
solve_captcha(web)
