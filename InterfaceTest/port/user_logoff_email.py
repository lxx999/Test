from common.send_request import SendRequests
from common import md5_encryption


params = {
    "language": "sds",
    # "token": "t7dsNJG22DpQ_RJhwPvpyGugJFJMRBIx"

}

# 用户注销发送邮件 ps:邮箱是不区分大小写的
t = SendRequests(method="post", uri="/v1/user/logoff-email", param=params,
                 token="t7dsNJG22DpQ_RJhwPvpyGugJFJMRBIx", is_sign=True)

t.send_request()
