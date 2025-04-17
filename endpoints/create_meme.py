import requests

from endpoints.endpoint import Endpoint


class PostMeme(Endpoint):
    def create_new_meme(self, body, token):
        self.response = requests.post(
            url=f'{self.url}/meme',
            headers={"Authorization": token},
            json=body
        )
        return self.response

