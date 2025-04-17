import requests

from endpoints.endpoint import Endpoint


class AuthorizeToken(Endpoint):
    def get_authorize_token(self, body):
        self.response = requests.post(
            url=f'{self.url}/authorize',
            json=body
        )
        return self.response
