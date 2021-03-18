from common.send_request import SendRequests
from common import md5_encryption


params = {
    "email": "fangxing@honbow.com",
    "password": md5_encryption("a123456789"),

}

# 用户登录
t = SendRequests(method="post", uri="/pv1/user/login", param=params,
                 token="", is_sign=True)

t.send_request()
