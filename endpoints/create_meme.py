import requests
import allure
from endpoints.endpoint import Endpoint


class PostMeme(Endpoint):
    @allure.step("Create a new meme with POST")
    def create_new_meme(self, body, token):
        self.response = requests.post(
            url=f'{self.url}/meme',
            headers={"Authorization": token},
            json=body
        )
        return self.response
