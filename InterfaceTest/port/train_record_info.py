from common.send_request import SendRequests


params = {
    "uid": "163946",
    "tid": "vPbZGrXn",
}

# 获取体能训练数据详情
t = SendRequests(method="post", uri="/v1/healthy/train-record-info", param=params,
                 token="cHg3J16GhZNLGwVa2f8J80Jrmf4qd3hO", is_sign=True)

t.send_request()
