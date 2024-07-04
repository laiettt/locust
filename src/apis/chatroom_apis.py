from src.utils.client_request import Client


def chat_to_vips(client: Client, header: dict, body: dict):
    api_path = '/chat_to_vips'
    return client.post(api_url=api_path, header=header, body=body)


def profile(client: Client, header: dict, body: dict):
    api_path = '/profile'
    return client.get(api_url=api_path, body=body, header=header)
