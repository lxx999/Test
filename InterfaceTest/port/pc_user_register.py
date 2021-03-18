from faker import Faker
from common.send_request import SendRequests
from common import md5_encryption, create_uuid

faker = Faker("zh_CN")

for i in range(1):
    params = {
        "email": faker.pystr().lower() + faker.email(),
        "password": md5_encryption("a123456789"),
        "photo": "https://official-file.honbow.com/ava1593293280805.png",
        "loginip": "127.0.0.1",
        "area": "en",
        "source": "pc"
    }

    # 用户注册 ps:邮箱是不区分大小写的
    t = SendRequests(method="post", uri="/pv1/user/register", param=params,
                     token="", is_sign=True)

    t.send_request()
