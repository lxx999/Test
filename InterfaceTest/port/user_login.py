from common.send_request import SendRequests
from common import md5_encryption, create_uuid


params = {
    "email": "fangxing@honbow.com",
    "uuid": create_uuid(),  # 登录接口未校验uuid是否与邮箱匹配
    "password": md5_encryption("b123456789"),

}

# 用户登录
t = SendRequests(method="post", uri="/v1/user/login", param=params,
                 token="", is_sign=True)

t.send_request()
