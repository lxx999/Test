from common.send_request import SendRequests

# 用户登出
t = SendRequests(method="post", uri="/v1/user/logout",
                 token="yjT-koCW3moRSCy0wEMocSgGsVLMCynV", is_sign=True)

t.send_request()
