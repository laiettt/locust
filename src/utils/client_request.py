from locust.contrib.fasthttp import FastHttpSession


class Client(object):

    def __init__(self, client: FastHttpSession) -> None:
        self.client = client

    def post(self, api_url: str, header: dict = None, body: dict = None):
        return self.request(api_url=api_url, method="POST", header=header, body=body)
        # return self.client.post(url=api_url, method="POST", header=header, body=body)

    def get(self, api_url: str, header: dict = None, body: dict = None):
        return self.client.request(url=api_url, method="GET", header=header, body=body)

    def request(self, api_url: str, method: str, header: dict, body: dict = None):
        try:
            # url = f"{self.domain}{api_url}"
            if method == "POST":
                # request_log(api_url=api_url, url=url, method="POST", header=header, body=body)
                response = self.client.post(url=api_url, headers=header, json=body, timeout=3)
            else:
                # request_log(url=url, method="GET", header=header, body=body)
                response = self.client.get(url=api_url, headers=header, json=body, timeout=3)
            # logger.info(f'Response: {response}')
            return response

        except Exception as e:
            # logger.error(f'{e}')
            raise Exception
#
#
# def request_log(**kwargs):
#     logger.info(json.dumps(kwargs, indent=4))