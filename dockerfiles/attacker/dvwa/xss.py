import sys
from typing import NoReturn

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


def attack(site: str, payload: str, username: str, password: str):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)

    driver.get(site)

    # check for a login page
    if driver.current_url.endswith("/login.php"):
        username_element = driver.find_element(By.NAME, "username")
        password_element = driver.find_element(By.NAME, "password")

        username_element.send_keys(username)
        password_element.send_keys(password)

        button = driver.find_element(By.NAME, "Login")
        button.click()

    driver.get(site + payload)

    # a simple check if JS has been injected
    out = "console.log(\"PWNED\")" in driver.page_source

    driver.quit()
    return out

def main(site, payload, username, password):
    print(attack(site, payload, username, password))