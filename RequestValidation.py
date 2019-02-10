class RequestValidator:

    def api_token_validation(self, auth):
        self.auth = auth
        if self.auth == "a1s2d3f4":
            return True
        else:
            return False

