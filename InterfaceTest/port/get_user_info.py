from common.send_request import SendRequests


# 获取用户信息
t = SendRequests(method="post", uri="/v1/user/get-user-info",
                 token="gG_s2YrEFjQsN2SQzF2UxIRGKrMRPIwY", is_sign=True)

t.send_request()

