import pytest
from data import valid_meme_body_post, meme_body_missing_field


@pytest.mark.critical
def test_create_meme_with_valid_data(auth_token, post_meme_endpoint):
    body = valid_meme_body_post()
    post_meme_endpoint.create_new_meme(body, auth_token)
    post_meme_endpoint.check_that_status_is_200()


@pytest.mark.high
@pytest.mark.parametrize("missing_field", ["text", "url", "tags", "info"])
def test_create_meme_without_required_field(auth_token, post_meme_endpoint, missing_field):
    body = meme_body_missing_field(missing_field)
    post_meme_endpoint.create_new_meme(body, auth_token)
    post_meme_endpoint.check_bad_request_is_400()


@pytest.mark.skip(reason="API currently accepts any string as URL")
def test_create_meme_with_invalid_url(auth_token, post_meme_endpoint):
    body = valid_meme_body_post()
    body["url"] = "not_a_url"
    post_meme_endpoint.create_new_meme(body, auth_token)
    post_meme_endpoint.check_bad_request_is_400()


@pytest.mark.medium
@pytest.mark.parametrize("invalid_text", [123, True, None, ["memes", "funny"], {"object": "one"}])
def test_create_meme_with_invalid_text_type(auth_token, post_meme_endpoint, invalid_text):
    body = valid_meme_body_post()
    body["text"] = invalid_text
    post_meme_endpoint.create_new_meme(body, auth_token)
    post_meme_endpoint.check_bad_request_is_400()


@pytest.mark.high
def test_create_meme_without_token(post_meme_endpoint):
    body = valid_meme_body_post()
    post_meme_endpoint.create_new_meme(body, token=None)
    post_meme_endpoint.check_response_is_unauthorized()


@pytest.mark.medium
@pytest.mark.parametrize("invalid_info", ["string", ["memes", "funny"], 123, True, ""])
def test_create_meme_with_invalid_info_type(auth_token, post_meme_endpoint, invalid_info):
    body = valid_meme_body_post()
    body["info"] = invalid_info
    post_meme_endpoint.create_new_meme(body, auth_token)
    post_meme_endpoint.check_bad_request_is_400()


@pytest.mark.medium
@pytest.mark.parametrize("invalid_tags", ["string", {"object1": "one", "object2": "two"}, 123, None, ""])
def test_create_meme_with_invalid_tags_type(auth_token, post_meme_endpoint, invalid_tags):
    body = valid_meme_body_post()
    body["tags"] = invalid_tags
    post_meme_endpoint.create_new_meme(body, auth_token)
    post_meme_endpoint.check_bad_request_is_400()
