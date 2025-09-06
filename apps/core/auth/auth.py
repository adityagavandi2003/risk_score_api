from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class HeaderApiKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get("X-API-Key")
        if api_key == "secret123":  # your fixed key
            return (None, None)  # no user, no auth object
        raise AuthenticationFailed("Invalid or missing API Key")
