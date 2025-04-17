import pytest


@pytest.mark.critical
def test_authorization_with_valid_name(authorize_token_endpoint):
    authorize_token_endpoint.get_authorize_token({"name": "tamara"})
    authorize_token_endpoint.check_token_was_returned()


@pytest.mark.critical
def test_token_liveness_with_valid_token(auth_token, check_token_endpoint):
    check_token_endpoint.check_token(auth_token)
    check_token_endpoint.check_token_is_alive()


@pytest.mark.high
def test_authorization_with_empty_name(authorize_token_endpoint):
    authorize_token_endpoint.get_authorize_token({})
    authorize_token_endpoint.check_bad_request_is_400()


@pytest.mark.medium
@pytest.mark.parametrize("invalid_token", ["", "fake_token_12345", None, 12345])
def test_token_liveness_check_with_invalid_token(check_token_endpoint, invalid_token):
    check_token_endpoint.check_token(invalid_token)
    check_token_endpoint.check_response_not_found()


@pytest.mark.high
def test_request_without_token(get_all_memes_endpoint):
    get_all_memes_endpoint.get_all_memes(token=None)
    get_all_memes_endpoint.check_response_is_unauthorized()
