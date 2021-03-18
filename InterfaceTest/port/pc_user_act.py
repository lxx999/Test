from common.send_request import SendRequests


# 获取activename字段不为空的接口
t = SendRequests(method="post", uri="/pv1/user/user-act",
                 token="", is_sign=True)

t.send_request()
