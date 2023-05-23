import requests
import json


class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        data_list = []
        data = json.loads(self.get_response_body())
        for d in data:
            data_list.append(d)

        return data_list
