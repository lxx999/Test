from faker import Faker
from common.send_request import SendRequests

faker = Faker("zh_CN")

params = {
    "email": "swindell.anne@ymail.com",  # faker.pystr() + faker.email(),
}

# 判断邮箱是否注册
t = SendRequests(method="post", uri="/v1/user/is-registered", param=params,
                 token="", is_sign=True)

t.send_request()
