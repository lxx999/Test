from common.send_request import SendRequests


params = {
    "uid": "163946",
    "tids": "vPbZGrXn",  # 多个体能id用竖线拼接
}

# 体能训练数据删除
t = SendRequests(method="post", uri="/v1/healthy/train-record-del", param=params,
                 token="cHg3J16GhZNLGwVa2f8J80Jrmf4qd3hO", is_sign=True)

t.send_request()
