from faker import Faker
from common.send_request import SendRequests
from common import md5_encryption, create_uuid

faker = Faker("zh_CN")

for i in range(1):
    params = {
        "email": "z01@qa.test", #f"t{i}@test.com",  # faker.pystr().lower() + faker.email(),
        "uuid": create_uuid(),
        "birthday": "١٩٥٤-٠٣-٢٧",  # "2000-10-18",
        "password": md5_encryption("a123456789"),
        "height": 50.1,
        "weight": 50.1,
        "gender": 0,
        "language": "de",
        "source": "app"
    }

    # 用户注册 ps:邮箱是不区分大小写的
    t = SendRequests(method="post", uri="/v1/user/register", param=params,
                     token="", is_sign=True)

    t.send_request()
