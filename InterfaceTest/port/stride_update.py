from faker import Faker
from common.send_request import SendRequests
from common import md5_encryption, create_uuid

faker = Faker("zh_CN")

params = {
    "strideWalk": "91",
    "strideRun": "71",
    "strideRunAction": 1,  # 测试校准 1  手动输入 2  系统默认 3  自动校准 4
    "strideWalkAction": 1,
}

# 用户步长信息更新
t = SendRequests(method="post", uri="/v1/user/stride-update", param=params,
                 token="_2Auh8iHcHVhyQ_9pHaXPPAQc5e4LBKF", is_sign=True)

t.send_request()
