import requests
import json

class WittyFlowSms:

    def __init__(self, app_id, app_secret):
        self.app_id     = app_id
        self.app_secret = app_secret

    def app_id():
        return self.app_id

    def app_secret():
        return self.app_secret


    def send_sms(from, to, message):
        body_to_send = json.dumps({
            "from":       f"{from}",
            "to":         f"233{to[1:]}",
            "type" :      1,
            "app_id":     f"{self.app_id}",
            "app_secret": f"{self.app_secret}",
        })
        response = requests.post('https://api.wittyflow.com/v1/messages/send', data=body_to_send)
        return response.json()
