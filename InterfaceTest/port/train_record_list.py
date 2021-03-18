from common.send_request import SendRequests


params = {
    "uid": "163946",
    "pageSize": 10,
    "pageIndex": 1,
}

# 获取体能训练数据详情
t = SendRequests(method="post", uri="/v1/healthy/train-record-list", param=params,
                 token="cHg3J16GhZNLGwVa2f8J80Jrmf4qd3hO", is_sign=True)

t.send_request()
