import requests
import allure
from endpoints.endpoint import Endpoint


class CheckToken(Endpoint):
    @allure.step("Check if the token is alive")
    def check_token(self, token):
        self.response = requests.get(url=f'{self.url}/authorize/{token}')
        return self.response.text
