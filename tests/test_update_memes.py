import pytest
from data import valid_meme_body_put, meme_body_missing_field


@pytest.mark.critical
def test_update_meme_and_verify_response_data(
        auth_token,
        update_meme_endpoint,
        get_one_meme_endpoint,
        created_meme
):
    body = valid_meme_body_put(created_meme)

    update_meme_endpoint.update_meme_put(created_meme, body, auth_token)
    update_meme_endpoint.check_that_status_is_200()

    get_one_meme_endpoint.get_one_meme(auth_token, created_meme)
    get_one_meme_endpoint.check_that_status_is_200()
    get_one_meme_endpoint.check_data_of_meme_equals_expected(body, check_id=False)


@pytest.mark.high
@pytest.mark.parametrize("missing_field", ["text", "url", "tags", "info"])
def test_update_meme_with_missing_field(auth_token, update_meme_endpoint, created_meme, missing_field):
    body = meme_body_missing_field(missing_field)
    update_meme_endpoint.update_meme_put(created_meme, body, auth_token)
    update_meme_endpoint.check_bad_request_is_400()


@pytest.mark.medium
@pytest.mark.parametrize("invalid_text", [False, 456, {"object": "one"}])
def test_update_meme_with_invalid_text_type(auth_token, update_meme_endpoint, created_meme, invalid_text):
    body = valid_meme_body_put(created_meme)
    body["text"] = invalid_text
    update_meme_endpoint.update_meme_put(created_meme, body, auth_token)
    update_meme_endpoint.check_bad_request_is_400()


@pytest.mark.medium
@pytest.mark.parametrize("invalid_info", [[], "string", 0])
def test_update_meme_with_invalid_info_type(auth_token, update_meme_endpoint, created_meme, invalid_info):
    body = valid_meme_body_put(created_meme)
    body["info"] = invalid_info
    update_meme_endpoint.update_meme_put(created_meme, body, auth_token)
    update_meme_endpoint.check_bad_request_is_400()


@pytest.mark.medium
@pytest.mark.parametrize("invalid_tags", ["string", {"object1": "one", "object2": "two"}, 123, None])
def test_update_meme_with_invalid_tags_type(auth_token, update_meme_endpoint, created_meme, invalid_tags):
    body = valid_meme_body_put(created_meme)
    body["tags"] = invalid_tags
    update_meme_endpoint.update_meme_put(created_meme, body, auth_token)
    update_meme_endpoint.check_bad_request_is_400()


@pytest.mark.medium
@pytest.mark.parametrize("invalid_id", ["string_id", -1, 99999])
def test_update_meme_with_invalid_id(auth_token, update_meme_endpoint, invalid_id):
    body = valid_meme_body_put(invalid_id)
    update_meme_endpoint.update_meme_put(invalid_id, body, auth_token)
    update_meme_endpoint.check_response_not_found()


@pytest.mark.low
def test_update_with_non_existent_method(auth_token, update_meme_endpoint, created_meme):
    body = valid_meme_body_put(created_meme)
    update_meme_endpoint.update_meme_patch(created_meme, body, auth_token)
    update_meme_endpoint.check_method_not_allowed()

@pytest.mark.high
def test_update_meme_without_token(update_meme_endpoint, created_meme):
    body = valid_meme_body_put(created_meme)
    update_meme_endpoint.update_meme_put(created_meme, body, token=None)
    update_meme_endpoint.check_response_is_unauthorized()

@pytest.mark.high
def test_update_meme_with_invalid_token(update_meme_endpoint, created_meme):
    body = valid_meme_body_put(created_meme)
    invalid_token = "invalid_token123"
    update_meme_endpoint.update_meme_put(created_meme, body, invalid_token)
    update_meme_endpoint.check_response_is_unauthorized()


def test_update_meme_by_non_owner(authorize_token_endpoint, update_meme_endpoint, created_meme):
    authorize_token_endpoint.get_authorize_token({"name": "not_owner_of_meme"})
    not_owner_token = authorize_token_endpoint.response.json().get("token")

    body = valid_meme_body_put(created_meme)

    update_meme_endpoint.update_meme_put(created_meme, body, not_owner_token)
    update_meme_endpoint.check_response_is_forbidden()
