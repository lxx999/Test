from common.send_request import SendRequests
from common import md5_encryption


params = {
    "password": md5_encryption("a123456789"),

}

# 校验密码是否pctoken对应的用户
t = SendRequests(method="post", uri="/pv1/user/password-verify", param=params,
                 token="Zn1eXITnmwJ11iRSTMOE0iC_qTaTGRUu", is_sign=True)

t.send_request()
