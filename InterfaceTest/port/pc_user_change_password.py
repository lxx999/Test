from common.send_request import SendRequests
from common import md5_encryption


params = {
    "oldPassword": md5_encryption("a123456789"),
    "newPassword": md5_encryption("a123456789")
}

# 用户修改密码
t = SendRequests(method="post", uri="/pv1/user/change-password", param=params,
                 token="gYLIN0bRz4VodNzpVjgUCXMmXo7K4wHA", is_sign=True)

t.send_request()
