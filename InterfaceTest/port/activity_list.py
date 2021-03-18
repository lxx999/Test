from common.send_request import SendRequests


params = {
    "uid": 163946,
    "start": "20100101",
    "end": "20201111",
}

# 获取活动数据列表
t = SendRequests(method="post", uri="/v1/healthy/activity-list", param=params,
                 token="usLYmfk0dwWzI_VOvqptusfrCgSfdZXy", is_sign=True)

t.send_request()
