from common.send_request import SendRequests

params = {
    "name": "",
    "email": "fangxing@honbow.com",
    "isactive": "",  # 状态。1为激活，0为未激活
    "state": "",  # 状态:1正常，2:注销 0是默认正常
    "created": "",
    "area": "",
    "source": "",
    "subscribe": "",
    "activename": "",
    "perPage": "",
    "page": "",
}

# 获取用户列表
t = SendRequests(method="post", uri="/pv1/user/user-list", param=params,
                 token="", is_sign=True)

t.send_request()
