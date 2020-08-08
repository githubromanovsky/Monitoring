#!/usr/bin/python3
import os
import requests


def send_message():
    """Function for send message in Telegram"""
    requests.get("https://api.telegram.org/bot{}/sendMessage?".format(api_token),
                 params=dict(chat_id="@Your Chanel Telegram",
                             text="Warning! Server {} not "
                                  "available".format(ip)))
    return ()


# Your ip or hostname servers
hostname = ["Your ip-address server1", "Your ip-address server1"]
# Your api_token telegram bot
api_token = "Your API-key"
for ip in hostname:
    response = os.system("ping -c 10 " + ip)
    if response == 0:
        pass
    else:
        send_message()
