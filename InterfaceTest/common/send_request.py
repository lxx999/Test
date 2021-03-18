import time
import json
import base64
import requests
import config
from hashlib import sha1
from faker import Faker
from common.generated_data import md5_encryption



class SendRequests(object):
    """ 接口请求工具类 """

    __slots__ = ["method", "uri", "param", "is_sign", "token", "app_key", "url", "time_stamp"]

    def __init__(self, method: str, uri: str, param: dict = "", is_sign: bool = True, token: str = "",
                 app_key: str = "6177a0a730442a91"):
        """
        初始化
        :param method: 请求方法
        :param uri: 接口地址
        :param param: 接口请求业务参数
        :param is_sign: 是否需要签名，默认为需要  True为需要  False为不需要
        :param token: token
        :param app_key: 本地 app_key
        """

        self.method = method
        self.uri = uri
        self.param = param
        self.is_sign = is_sign
        self.token = token
        self.app_key = app_key
        self.url = f'{config.env["protocol"]}://{config.env["host"]}'

        # 获取13位时间戳
        self.time_stamp = str(int(round(time.time() * 1000)))

    def base64_coding(self):
        """
        将请求参数进行base64编码，并进行指定格式拼接。
        :return: 拼接后的编码数据
        """

        # 部分接口不需要无业务参数不需要data
        join_data = ""

        if self.param:
            # base64转码
            __base64_data = base64.b64encode(json.dumps(self.param).encode()).decode()

            # 将编码后的最前面两位拼接到最末尾
            join_data = __base64_data[2:] + __base64_data[:2]

        return join_data

    def sign(self):
        """
        通过Sha1加密生成签名
        :return: 签名
        """

        # 拼接待加密的数据
        __sign_data = f'token={self.token}&appkey={self.app_key}&data={self.base64_coding()}&timeStamp={self.time_stamp}'

        return sha1(__sign_data.encode("utf-8")).hexdigest()

    def send_request(self):
        """
        方法请求
        :return:请求结果
        """

        # 请求方法转换为大写
        method = self.method.upper()

        # 需要签名的参数
        if self.is_sign:
            params = {
                # "token": self.token,
                "data": self.base64_coding(),
                "sign": self.sign(),
                "timeStamp": self.time_stamp,

            }
        else:
            params = self.param
            # params["token"] = self.token

        if "pv1" in self.uri:
            headers = {
                "pctoken": self.token
            }
        else:
            headers = {
                "token": self.token
            }
        print("------------------------------------------------业务参数-------------------------------------------------------")
        print(self.param)
        print(" ")

        print("------------------------------------------------实际请求参数-------------------------------------------------------")
        print(params)
        print(" ")

        if method == "POST":
            result = requests.post(url=self.url + self.uri, data=params, headers=headers, verify=False)
        elif method == "GET":
            result = requests.get(url=self.url + self.uri, params=params, headers=headers, verify=False)  # verify=False
        else:
            raise ValueError("请求方法目前只支持POST和GET!")

        data = {}
        code = result.status_code
        try:
            response = result.json()
            base_data = response["data"]

            # data存在数据，base64解码后返回数据
            if base_data:
                base_data = base_data[-2:] + base_data[:-2]
                # 解决unicode编码
                data = base64.b64decode(base_data).decode("unicode-escape")
        except:
            response = result.text
        print(
            "------------------------------------------------响应结果-------------------------------------------------------")
        print(response)
        print(" ")
        print(
            "---------------------------------------------data解密后数据-----------------------------------------------------")
        print(data)
        return response, code, data


if __name__ == '__main__':
    faker = Faker("zh_CN")
    params = {
        "email": "B20201024@qb.com",
        "password": md5_encryption("a123456789"),
    }

    for i in range(1):
        time.sleep(0.1)
        t = SendRequests(method="post", uri="/pv1/user/register", param=params,
                         token="", is_sign=True)

        response, code, data = t.send_request()

        print("http响应状态：", code)
        print("接口响应结果：", response)
        print("解密后data数据：", data)

