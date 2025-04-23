import pytest


@pytest.mark.critical
def test_delete_meme_with_valid_id(auth_token, delete_meme_endpoint, created_meme, get_one_meme_endpoint):
    meme_id = created_meme
    delete_meme_endpoint.delete_meme(meme_id, auth_token)
    delete_meme_endpoint.check_that_status_is_200()
    get_one_meme_endpoint.get_one_meme(auth_token, meme_id)
    get_one_meme_endpoint.check_response_not_found()


@pytest.mark.high
def test_delete_meme_with_invalid_id(auth_token, delete_meme_endpoint):
    invalid_id = 9999
    delete_meme_endpoint.delete_meme(invalid_id, auth_token)
    delete_meme_endpoint.check_response_not_found()


@pytest.mark.high
def test_delete_meme_twice(auth_token, delete_meme_endpoint, created_meme):
    meme_id = created_meme
    delete_meme_endpoint.delete_meme(meme_id, auth_token)
    delete_meme_endpoint.check_that_status_is_200()
    delete_meme_endpoint.delete_meme(meme_id, auth_token)
    delete_meme_endpoint.check_response_not_found()


@pytest.mark.high
def test_delete_meme_without_token(delete_meme_endpoint, created_meme):
    meme_id = created_meme
    delete_meme_endpoint.delete_meme(meme_id, token=None)
    delete_meme_endpoint.check_response_is_unauthorized()


@pytest.mark.medium
@pytest.mark.parametrize("invalid_token", ["fake_token_12345", "None", "6757444"])
def test_delete_meme_with_invalid_token(invalid_token, delete_meme_endpoint, created_meme):
    meme_id = created_meme
    delete_meme_endpoint.delete_meme(meme_id, invalid_token)
    delete_meme_endpoint.check_response_is_unauthorized()


@pytest.mark.medium
def test_delete_meme_with_empty_token_string(delete_meme_endpoint, created_meme):
    meme_id = created_meme
    delete_meme_endpoint.delete_meme(meme_id, token="")
    delete_meme_endpoint.check_server_error()


@pytest.mark.high
def test_delete_meme_by_non_owner(authorize_token_endpoint, created_meme, delete_meme_endpoint):
    authorize_token_endpoint.get_authorize_token({"name": "not_owner_of_meme"})
    not_owner_token = authorize_token_endpoint.response.json().get("token")

    meme_id = created_meme
    delete_meme_endpoint.delete_meme(meme_id, token=not_owner_token)
    delete_meme_endpoint.check_response_is_forbidden()
