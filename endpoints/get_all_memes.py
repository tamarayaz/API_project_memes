import requests
import allure

from endpoints.endpoint import Endpoint


class GetAllMemes(Endpoint):
    @allure.step("Get all memes by GET /meme)")
    def get_all_memes(self, token):
        self.response = requests.get(
            url=f'{self.url}/meme',
            headers={"Authorization": token}
        )
        return self.response
