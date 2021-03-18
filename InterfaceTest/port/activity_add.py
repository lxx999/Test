from common.send_request import SendRequests


params = {
    "uid": 165424,
    "data": [
        {
            "date": "20200909",
            "data": "eJxNj71uwzAMhN+FswfZiVqZW1B58Ng0u0FYqiPElg39BAmCvHtpd0i2w33k8fiAnJ0BhG+Tm+zaCxSQbEytZo91T+McnI2A5UcBE926c+iuNGYLWNcFDEtsfbKBLUDB87P/dcPpvjAvCzCdp4kltLoS8mcN35AUDM+WQjpSsuYVIXmHHd4oZb2vlFT7nRAC1qiJevZ1hYcGlcKDwuYLtd7Yf+zrTEx22QrRdXirrBQPu5jI93bDJgdKbvbrg+rz+QfpHlFy"
        }
    ],
}

# 上传活动数据  ps:用户必须是激活状态
t = SendRequests(method="post", uri="/v1/healthy/activity-add", param=params,
                 token="NvND-I_G2ykujqYmGW4zZwLSKp9icAo7", is_sign=True)

t.send_request()
