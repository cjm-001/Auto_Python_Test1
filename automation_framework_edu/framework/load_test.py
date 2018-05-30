from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        self.login()

    def login(self):
        self.client.post("http://linehome.51cto.com/index",{"username":"cjm0001","password":"qqqqqq"})
    @task(2)
    def baidu(self):
        self.client.get("/")
    @task(1)
    def profile(self):
        self.client.get("/courselist")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000