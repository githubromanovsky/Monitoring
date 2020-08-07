#!/usr/bin/python3
import os
import sys
import requests


def send_message():
    """Function for send message in Telegram"""
    requests.get("https://api.telegram.org/bot{}/sendMessage?".format(api_token),
                 params=dict(chat_id="@Your Chanel Telegram",
                             text="Warning! Server {} not "
                                  "available".format(hostname)))
    return ()


# Your ip or hostname
hostname = "Your ip-address server"
hostname1 = "Your ip-address server"
# Your api_token telegram bot
api_token = "Your API-key"
response = os.system("ping -c 10 " + hostname)
if response == 0:
    pass
else:
    send_message()
response = os.system("ping -c 10 " + hostname1)
if response == 0:
    pass
else:
    send_message()
sys.exit()
