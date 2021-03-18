from common.send_request import SendRequests
from common import md5_encryption


params = {
    "oldPassword": md5_encryption("b123456789"),
    "newPassword": md5_encryption("a123456789")
}

# 用户修改密码
t = SendRequests(method="post", uri="/v1/user/change-password", param=params,
                 token="OVKDObTNeQhwr3vdKF1c9R8qp6s_vKn3", is_sign=True)

t.send_request()
