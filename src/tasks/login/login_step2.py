from locust import task, FastHttpUser, constant
from src.utils.client_request import TaskSets
from src.tasks.login.login_step1 import LoginStep1


class EchoTaskSet(TaskSets):
    @task
    def hihihi(self):
        print("hihihi")

    @task
    def call_step1(self):
        LoginStep1.login_step_1(self)
# class LoginStep2(TaskSets):
#     @task
#     def login_step_2(self):
#         print("login_step_2")


def test2(self):
    print(66666)


class EchoLocust(FastHttpUser):
    tasks = [EchoTaskSet]
    # tasks = EchoTaskSet
    host = "settings.platform_url"
    wait_time = constant(0.5)


if __name__ == "__main__":
    from locust import run_single_user
    run_single_user(EchoLocust)