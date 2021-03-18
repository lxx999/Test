from faker import Faker
from common.send_request import SendRequests

faker = Faker("zh_CN")

params = {
    "id": 165153,
    "name": faker.name(),  # 非必填
    "birthday": "2000-10-18",  # 必填  限制不得小于13岁
    "gender": 0,  # 非必填  ps：0：保密  1：男  2：女
    "height": 50.1,  # 必填
    "weight": 50.1,  # 必填

}

# 修改用户信息
t = SendRequests(method="post", uri="/pv1/user/userinfo", param=params,
                 token="-yGYazHpT4UvUJ0eLV6GSIHQ7YYdD1CZ", is_sign=True)

t.send_request()
