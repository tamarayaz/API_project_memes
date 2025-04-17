import requests

from endpoints.endpoint import Endpoint


class CheckToken(Endpoint):
    def check_token(self, token):
        self.response = requests.get(url=f'{self.url}/authorize/{token}')
        return self.response.text
