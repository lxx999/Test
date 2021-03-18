from common.send_request import SendRequests
from common import md5_encryption, create_uuid, create_mac


params = {
    "deviceType": "ID205S",
    "deviceInfo": " ",
    "uid": 164845,
    "mac": create_mac(),
}

# 用户绑定设备
t = SendRequests(method="post", uri="/v1/user/up-device", param=params,
                 token="dQBXU4jP89VkTqpEEu1ilBHVryx4k4io", is_sign=True)

t.send_request()
