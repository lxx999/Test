from common.send_request import SendRequests

params = {
    "id": 165153,
    # "token": "",
    # "pctoken": "",
    # "email": "fangxing@honbow.com",
}

# 获取用户信息
t = SendRequests(method="post", uri="/pv1/user/user-info-list", param=params,
                 token="", is_sign=True)

t.send_request()
