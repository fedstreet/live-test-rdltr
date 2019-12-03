class AuthenticatedRequest:
    def __init__(self):
        self.headers = {}

    def set_auth(self, auth_token):
        self.headers["Authorization"] = auth_token
        return self
