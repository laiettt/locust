from src.apis.chatroom_apis import profile
from src.utils.client_request import Client


def get_profile(client: Client):
    """
        do something
    """
    return profile(client=client, header={}, body={})
