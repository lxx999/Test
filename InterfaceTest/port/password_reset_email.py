from faker import Faker
from common.send_request import SendRequests
from common import md5_encryption, create_uuid

faker = Faker("zh_CN")

params = {
    "email": "fangxing@honbow.com".lower(),
    "language": "it",
}

# 忘记密码发送邮件
t = SendRequests(method="post", uri="/v1/user/password-reset-email", param=params,
                 token="", is_sign=True)

t.send_request()
