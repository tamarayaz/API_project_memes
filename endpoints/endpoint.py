import allure


class Endpoint:
    url = 'http://167.172.172.115:52355'
    response = None
    json = None

    @allure.step("Check that response is 200")
    def check_that_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step("Check that the token is in response")
    def check_token_was_returned(self):
        self.json = self.response.json()
        assert "token" in self.json

    @allure.step("Check if the token is alive")
    def check_token_is_alive(self):
        assert "Token is alive" in self.response.text

    @allure.step("Check that the request is not authorized")
    def check_response_is_unauthorized(self):
        assert self.response.status_code == 401  #or self.response.status_code == 403

    @allure.step("Check that the response is not found")
    def check_response_not_found(self):
        assert self.response.status_code == 404

    @allure.step("Check that the request is invalid")
    def check_bad_request_is_400(self):
        assert self.response.status_code == 400

    @allure.step("Check if the server returned an error")
    def check_server_error(self):
        assert self.response.status_code == 500

    @allure.step("Check if the method is not allowed")
    def check_method_not_allowed(self):
        assert self.response.status_code == 405

    @allure.step("Check that meme has all required fields")
    def check_meme_contains_required_fields(self):
        self.json = self.response.json()
        required_fields = ["id", "text", "url", "tags", "info"]
        for field in required_fields:
            assert field in self.json
