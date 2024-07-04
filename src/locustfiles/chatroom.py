import queue
from locust import task, FastHttpUser, constant, TaskSet, events
from src.utils.client_request import Client
from src.tasks.chatroom.chat import chat_to_vip
from src.tasks.chatroom.profile import get_profile
from src.utils.read_datas import read_csv


user_queue = queue.Queue()


@events.init_command_line_parser.add_listener
def _(parser):
    parser.add_argument("--testfile", type=str, default="qa01", help="It's working")


@events.init.add_listener
def _(environment, **kwargs):
    testfile = f'{environment.parsed_options.testfile}.csv'
    users_csv = read_csv(testfile)
    for data in users_csv:
        user_queue.put_nowait(data)


class EchoTaskSet(TaskSet):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clients = Client(self.client)
        self.account = None

    def on_start(self):
        self.account = user_queue.get()
        """get token"""
        pass

    @task
    def call_chat_to_vip(self):
        # print(self.account, id(self.clients))
        chat_to_vip(self.clients)

    @task
    def call_get_profile(self):
        # print(self.account, id(self.clients))
        get_profile(self.clients)


class EchoLocust(FastHttpUser):
    tasks = [EchoTaskSet]
    host = "https://google.com"
    wait_time = constant(1)


if __name__ == "__main__":
    from locust import run_single_user
    run_single_user(EchoLocust)
    # os.system("locust -f chatroom.py")
