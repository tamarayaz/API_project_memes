import requests
import allure
from endpoints.endpoint import Endpoint


class UpdateMeme(Endpoint):
    @allure.step("Update meme with PUT")
    def update_meme_put(self, meme_id, body, token):
        self.response = requests.put(
            f'{self.url}/meme/{meme_id}',
            headers={"Authorization": token},
            json=body
        )
        return self.response

    @allure.step("Update meme with PATCH")
    def update_meme_patch(self, meme_id, body, token):
        self.response = requests.patch(
            f'{self.url}/meme/{meme_id}',
            headers={"Authorization": token},
            json=body
        )
        return self.response
