from common.send_request import SendRequests


params = {
    "language": "zh",
}

# 发送用户激活邮件
t = SendRequests(method="post", uri="/v1/user/send-act-user-email", param=params,
                 token="peDBy1fmkSGG-94UrSpCxirSlEJ-8iLD", is_sign=True)

t.send_request()
