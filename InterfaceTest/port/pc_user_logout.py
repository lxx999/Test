from common.send_request import SendRequests

# 用户登出
t = SendRequests(method="post", uri="/pv1/user/logout",
                 token="Zn1eXITnmwJ11iRSTMOE0iC_qTaTGRUu", is_sign=True)

t.send_request()
