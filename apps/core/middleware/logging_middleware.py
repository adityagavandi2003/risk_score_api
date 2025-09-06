import logging

request_logger = logging.getLogger("django")

class RequestResponseLoggingMiddleware:
    """
    Logs each request and response (without sensitive data).
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_logger.info(f"Request: {request.method} {request.get_full_path()}")
        if request.body:
            request_logger.debug(f"Request body: {request.body.decode('utf-8', errors='ignore')}")

        response = self.get_response(request)

        request_logger.info(f"Response status: {response.status_code}")
        try:
            request_logger.debug(f"Response body: {response.content.decode('utf-8')}")
        except Exception:
            request_logger.debug("Response body could not be decoded.")

        return response
