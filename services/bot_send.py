import requests
from datetime import datetime


def send_msg(**kwargs):
    token = "7705285656:AAGl0Sst4-qkB-onTA-U58VEpDmZBHxXzNo"  # bot token

    user_id = "885826488"  # user id
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + user_id + "&text=" + f"{datetime.now().strftime(f'<b>%d/%m/%y  %H : %M : %S {kwargs}</b>')}&parse_mode=HTML"
    response = requests.get(url_req)
    print(response.json())