import pytest
import random


@pytest.mark.critical
def test_get_all_memes_returns_list_with_valid_token(auth_token, get_all_memes_endpoint):
    get_all_memes_endpoint.get_all_memes(auth_token)
    get_all_memes_endpoint.check_that_status_is_200()
    get_all_memes_endpoint.check_that_get_all_memes_returns_list()


@pytest.mark.critical
def test_get_one_meme_with_valid_id(auth_token, get_one_meme_endpoint, created_meme):
    meme_id = created_meme
    get_one_meme_endpoint.get_one_meme(auth_token, meme_id)
    get_one_meme_endpoint.check_that_status_is_200()
    get_one_meme_endpoint.check_that_returned_meme_equals_sent_id(meme_id)


@pytest.mark.critical
def test_get_one_meme_contains_required_fields(auth_token, get_one_meme_endpoint, created_meme):
    meme_id = created_meme
    get_one_meme_endpoint.get_one_meme(auth_token, meme_id)
    get_one_meme_endpoint.check_that_status_is_200()
    get_one_meme_endpoint.check_meme_contains_required_fields()


@pytest.mark.high
def test_get_one_meme_with_invalid_id(auth_token, get_one_meme_endpoint):
    invalid_id = random.randint(900, 999)
    get_one_meme_endpoint.get_one_meme(auth_token, invalid_id)
    get_one_meme_endpoint.check_response_not_found()


@pytest.mark.high
def test_get_all_memes_without_token(get_all_memes_endpoint):
    get_all_memes_endpoint.get_all_memes(token=None)
    get_all_memes_endpoint.check_response_is_unauthorized()


@pytest.mark.high
def test_get_one_meme_with_invalid_token(get_one_meme_endpoint, created_meme):
    meme_id = created_meme
    invalid_token = "fake_token_123"
    get_one_meme_endpoint.get_one_meme(invalid_token, meme_id)
    get_one_meme_endpoint.check_response_is_unauthorized()
