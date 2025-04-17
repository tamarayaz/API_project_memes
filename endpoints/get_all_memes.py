import requests

from endpoints.endpoint import Endpoint


class GetAllMemes(Endpoint):
    def get_all_memes(self, token):
        self.response = requests.get(
            url=f'{self.url}/meme',
            headers={"Authorization": token}
        )
        return self.response
