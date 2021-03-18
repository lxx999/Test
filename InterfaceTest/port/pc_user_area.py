from common.send_request import SendRequests


# 获取area字段接口
t = SendRequests(method="post", uri="/pv1/user/user-area",
                 token="", is_sign=True)

t.send_request()
