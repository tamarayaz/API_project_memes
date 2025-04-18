import requests
import allure

from endpoints.endpoint import Endpoint


class AuthorizeToken(Endpoint):
    @allure.step("Get authorization token")
    def get_authorize_token(self, body):
        self.response = requests.post(
            url=f'{self.url}/authorize',
            json=body
        )
        return self.response
