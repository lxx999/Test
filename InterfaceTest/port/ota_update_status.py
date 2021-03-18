from common.send_request import SendRequests


params = {
    "fwId": "437",
    "deviceName": "IW1",
    "deviceType": "IW1",
    "fwVer": 198,  # 要升级版本
    "fwMode": "2",
    "mac": "C7:48:16:BC:20:09",
    "status": "4",    # 1 升级成功,2下载失败，3校验失败，4升级失败 5其他失败情况，6下载成功
    "remark": "测试",
    "errorCode": "150",
    "phoneSys": "13.5",
    "phoneMode": "SM-M3070",
    "preVer": 110,  # 当前版本
    "failSche": "50",
}

# OTA升级结果上报
t = SendRequests(method="post", uri="/v1/ota/update-status", param=params,
                 token="", is_sign=True)

t.send_request()
