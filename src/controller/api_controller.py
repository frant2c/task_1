import requests


class ApiController:
    def __init__(self):
        pass

    def send_get_request(self, request_url):
        response = requests.get(request_url)
        return self._handle_response(response)

    @staticmethod
    def _handle_response(response):
        try:
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise http_err
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err}")
            raise err
