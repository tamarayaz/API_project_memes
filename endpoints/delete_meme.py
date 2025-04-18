import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):
    @allure.step("Delete meme by ID")
    def delete_meme(self, meme_id, token):
        self.response = requests.delete(
            url=f'{self.url}/meme/{meme_id}',
            headers={"Authorization": token}
        )
        return self.response
