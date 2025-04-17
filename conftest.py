import pytest


from endpoints.check_token_ import CheckToken
from endpoints.create_meme import PostMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.get_all_memes import GetAllMemes
from endpoints.get_authorize_token import AuthorizeToken
from endpoints.get_one_meme import GetOneMeme
from endpoints.update_meme import UpdateMeme

url = 'http://167.172.172.115:52355/'

@pytest.fixture(scope="session")
def auth_token(authorize_token_endpoint, check_token_endpoint):
    token_cache = {}

    def get_token():
        if "token" in token_cache:
            verify_token = check_token_endpoint.check_token(token_cache["token"])
            if verify_token .status_code == 200:
                return token_cache["token"]

        new_token = authorize_token_endpoint.get_authorize_token({"name": "tamara"}).json()["token"]
        token_cache["token"] = new_token
        return new_token

    return get_token()

@pytest.fixture(scope="session")
def authorize_token_endpoint():
    return AuthorizeToken()

@pytest.fixture(scope="session")
def check_token_endpoint():
    return CheckToken()

@pytest.fixture()
def get_all_memes_endpoint():
    return GetAllMemes()

@pytest.fixture()
def get_one_meme_endpoint():
    return GetOneMeme()

@pytest.fixture()
def post_meme_endpoint():
    return PostMeme()


@pytest.fixture()
def update_meme_endpoint():
    return UpdateMeme()


@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()

@pytest.fixture()
def created_meme(auth_token, post_meme_endpoint, delete_meme_endpoint):
    token = auth_token

    meme_data = {
        "text": "Programmer",
        "url": "https://timeweb.com/media/articles/0001/18/thumb_17628_articles_standart.png",
        "tags": ["cat", "funny", "old_mem"],
        "info": {"author": "tester"}
    }

    create_response = post_meme_endpoint.create_new_meme(meme_data, token)
    meme_id = create_response.json().get("id")

    yield meme_id
    delete_meme_endpoint.delete_meme(meme_id, token)

#pytest tests/test_authorization.py -v
# pytest tests/test_delete_memes.py
# pytest tests/test_create_memes.py
# pytest tests/test_update_memes.py
# pytest tests/test_get_memes.py -v