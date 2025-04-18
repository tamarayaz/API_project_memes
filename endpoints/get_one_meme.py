import requests
import allure

from endpoints.endpoint import Endpoint


class GetOneMeme(Endpoint):
    @allure.step("Get one meme by GET /meme/id)")
    def get_one_meme(self, token, meme_id):
        self.response = requests.get(
            url=f'{self.url}/meme/{meme_id}',
            headers={"Authorization": token}
        )
        return self.response
    