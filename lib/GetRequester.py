import requests
import json


class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        url_data = []
        data = json.loads(self.get_response_body())
        for item in data:
            new_item = {
                "name": item["name"],
                "occupation": item["occupation"]
            }
            url_data.append(new_item)
        return url_data
