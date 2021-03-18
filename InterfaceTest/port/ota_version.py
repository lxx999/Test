from common.send_request import SendRequests

# params = {"age": 1, "appVersionCode": 165, "deviceName": "ID205L", "deviceType": "ID205L", "firmwareId": 314,
#           "fwMode": "1", "gender": 1, "mac": "D0:78:F3:71:D4:D4", "mobileBrand": "Android", "os": 1,
#           "phoneModel": "Android", "version": "16"}

params = {
    "fwId": 53,
    "deviceName": "IW2",
    "deviceType": "IW2",
    "fwVer": 123,
    "fwMode": 2,
    "mac": "58:4A:83:80:DC:93",
    "appLan": "fr",
}

# OTA升级检查
t = SendRequests(method="post", uri="/v1/ota/ota-version", param=params,
                 token="", is_sign=True)

t.send_request()
