from locust.contrib.fasthttp import FastHttpSession, FastResponse


class Client(object):

    def __init__(self) -> None:
        self.client = None
        self.account = None

    def set_client(self, client: FastHttpSession, account: str):
        self.client = client
        self.account = account

    def post(self, api_url: str, header: dict = None, body: dict = None):
        return self.request(api_url=api_url, method="POST", header=header, body=body)

    def get(self, api_url: str, header: dict = None, body: dict = None):
        return self.request(api_url=api_url, method="GET", header=header, body=body)

    def request(self, api_url: str, method: str, header: dict, body: dict = None):
        try:
            response: FastResponse
            if method == "POST":
                response = self.client.post(url=api_url, headers=header, json=body, timeout=3)
            else:
                response = self.client.get(url=api_url, headers=header, json=body, timeout=3)
            return response
        except Exception as e:
            raise e
