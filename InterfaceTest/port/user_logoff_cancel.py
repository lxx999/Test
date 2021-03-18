from faker import Faker
from common.send_request import SendRequests
from common import md5_encryption, create_uuid

faker = Faker("zh_CN")

params = {
    "uid": 164845
}

# 取消用户注销
t = SendRequests(method="post", uri="/v1/user/logoff-cancel", param=params,
                 token="", is_sign=True)

t.send_request()
