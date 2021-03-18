import os
import time
import json
import base64
import random
import config
from hashlib import sha1
from faker import Faker
from common import create_uuid, md5_encryption


class PerformanceData(object):
    __slots__ = ["uri", "table_name", "number", "app_key"]

    # 初始化
    def __init__(self, uri: str, table_name: str, number: int = 1000, app_key: str = "6177a0a730442a91"):
        """
        生成性能压测需要的加密参数
        :param uri: 接口uri
        :param table_name: 数据库查询表名   格式：库.表名  eg：lf_app.hb_user
        :param number: 生成数据的条数
        :param app_key: 本地appkey
        """

        self.uri = uri
        self.number = number
        self.app_key = app_key
        self.table_name = table_name

    def encrypt_data(self, params: dict, token: str = ""):
        """
        生成接口参数
        :param params:业务数据
        :param token:token
        :return:时间戳，编码后数据，签名
        """

        time_stamp = str(int(round(time.time() * 1000)))

        # base64转码
        base64_data = base64.b64encode(json.dumps(params).encode()).decode()

        # 将编码后的最前面两位拼接到最末尾
        join_data = base64_data[2:] + base64_data[:2]

        # 拼接待加密的数据
        sign_data = f'token={token}&appkey={self.app_key}&data={join_data}&timeStamp={time_stamp}'

        sign = sha1(sign_data.encode("utf-8")).hexdigest()

        return f"{token},{join_data},{sign},{time_stamp}"

    def generated_data(self):
        """
        生成接口参数至txt文件保存
        :return:
        """
        user_data = []
        email_list = []
        sql_data = []

        faker = Faker("zh_CN")
        sql_key = ("uid", "email", "uuid", "password", "token")

        # 活动/体能相关接口需要用户处于激活状态
        if self.uri in ["/healthy/activity-add", "/healthy/activity-list", "/healthy/train-record-add",
                        "/healthy/train-record-list", "/healthy/train-record-del", "/healthy/train-record-info"]:
            # 查询非注销状态且token处于有效期的用户且激活
            sql = f'select id,email,uuid,password,token from {self.table_name} where state != 2 and expirtime > now() and status = 1'
        else:
            # 查询非注销状态且token处于有效期的用户
            sql = f'select id,email,uuid,password,token from {self.table_name} where state != 2 and expirtime > now()'
        # 将所有符合规则的数据以字典的形式生成
        data = db.find_all(sql)
        for i in data:
            i = list(i)
            i[0] = str(i[0])
            sql_data.append(dict(zip(sql_key, tuple(i))))

        try:
            filename = self.uri.split("/")[-1].replace("-", "_") + ".txt"
            # 处理文件名称
            # if self.uri == "/user/is-registered":
            #     filename = "user_is_register.txt"
            # elif self.uri == "/user/register":
            #     filename = "user_register.txt"
            # elif self.uri == "/user/login":
            #     filename = "user_login.txt"
            # elif self.uri == "/user/send-act-user-email":
            #     filename = "send_act_user_email.txt"
            # elif self.uri == "/user/password-reset-email":
            #     filename = "password_reset_email.txt"
            # elif self.uri == "/user/verify-email":
            #     filename = "verify_email.txt"
            # elif self.uri == "/user/change-password":
            #     filename = "change_password.txt"
            # elif self.uri == "/user/forget-password":
            #     filename = "forget_password.txt"
            # elif self.uri == "/user/userinfo":
            #     filename = "user_info.txt"
            # elif self.uri == "/user/logout":
            #     filename = "user_logout.txt"
            # elif self.uri == "/user/logoff-email":
            #     filename = "user_logoff_email.txt"
            # elif self.uri == "/user/logoff":
            #     filename = "user_logoff.txt"
            # elif self.uri == "/user/logoff-cancel":
            #     filename = "logoff_cancel.txt"
            # elif self.uri == "/healthy/activity-add":
            #     filename = "activity_add.txt"
            # elif self.uri == "/healthy/activity-list":
            #     filename = "activity_list.txt"
            # elif self.uri == "/healthy/train-record-add":
            #     filename = "train_record_add.txt"
            # elif self.uri == "/healthy/train-record-list":
            #     filename = "train_record_list.txt"
            # elif self.uri == "/healthy/train-record-del":
            #     filename = "train_record_del.txt"
            # elif self.uri == "/healthy/train-record-info":
            #     filename = "train_record_info.txt"
            # elif self.uri == "/user/up-device":
            #     filename = "up_device.txt"
            # elif self.uri == "/user/stride-update":
            #     filename = "stride_update.txt"

            if self.uri in ("/user/is-registered", "/user/register"):
                while len(user_data) != self.number:
                    email = faker.pystr(5) + faker.email()
                    if self.uri == "/user/is-registered":
                        params = {
                            "email": email
                        }
                        data = self.encrypt_data(params=params)
                    else:
                        # 判断数据库不存在且不加入重复email
                        sql = f'select * from {self.table_name} where email = "{email}"'
                        res = db.find_all(sql)
                        if not res and email not in email_list:
                            params = {
                                "email": email,
                                "password": md5_encryption("a123456789"),
                                "uuid": create_uuid(),
                                "gender": random.randint(0, 2),
                                "birthday": faker.date(),
                                "height": "180",
                                "weight": "65",
                                "language": "zh"
                            }
                            email_list.append(email)
                            data = self.encrypt_data(params=params)
                        else:
                            continue
                    print(f"正在生成第{len(user_data)}条数据，原业务数据：{params}")
                    user_data.append(data)
            elif self.uri in ("/user/login", "/user/send-act-user-email", "/user/password-reset-email"):
                print(f"数据库只存在{len(data)}条可生成数据,已全部生成！")
                for i in sql_data:
                    params = False
                    if self.uri == "/user/login":
                        params = {
                            "email": i["email"],
                            "uuid": i["uuid"],
                            "password": i["password"]
                        }
                    elif self.uri == "/user/send-act-user-email":
                        params = {
                            "uid": i["uid"]
                        }
                    elif self.uri == "/user/password-reset-email":
                        params = {
                            "email": i["email"]
                        }
                    user_data.append(self.encrypt_data(params))
                    print(f"已生成第{len(user_data)}条数据，原业务数据：{params}")
            elif self.uri in ("/user/verify-email", "/user/forget-password", "/user/logoff"):
                print(f"接口：{self.uri}，无需加密和签名！")
                print(f"数据库只存在{len(data)}条可生成数据,开始生成数据！")
                for i in sql_data:
                    params = False
                    if self.uri == "/user/verify-email":
                        params = i["token"]
                    elif self.uri == "/user/forget-password":
                        params = f'{i["token"]},{i["password"]},{i["password"]}'
                    elif self.uri == "/user/logoff":
                        params = i["token"]
                    user_data.append(params)
                    print(f"已生成第{len(user_data)}条数据，业务数据：{params}")
            else:
                print(f"数据库只存在{len(data)}条可生成数据,开始生成数据！")
                for i in sql_data:
                    params = False
                    if self.uri == "/user/change-password":
                        params = {
                            "uid": i["uid"],
                            "oldPassword": i["password"],
                            "newPassword": i["password"]
                        }
                    elif self.uri == "/user/userinfo":
                        params = {
                            "uid": i["uid"],
                            "name": "压测数据",
                            "birthday": "1999-09-09",
                            "gender": 0,
                            "height": "180",
                            "weight": "65",
                        }
                    elif self.uri == "/user/logout":
                        params = {
                            "uid": i["uid"]
                        }
                    elif self.uri == "/user/logoff-email":
                        params = {
                            "uid": i["uid"]
                        }
                    elif self.uri == "/user/logoff-cancel":
                        params = {
                            "uid": i["uid"]
                        }
                    elif self.uri == "/healthy/activity-add":
                        params = {
                            "uid": i["uid"],
                            "data": [
                                # 新接口加密数据要可以正常解密，否则会报错
                                {"date": "20200901",
                                 "data": "eJzNlztvgzAQgP/LzQw+v7A9Nl0iZetYRcgCBqQ8UOJUiqL892JamsSkXSrEMeEz5/t8+gbuAr4M\nzUcTzuAuUPlQgwNUFhGFZvGBDI7B76ri1Bbl/rQL4HgGodnWb60vu89Rdct98JtiOKqIu+DYEC/9\nZn/oCiDXQ6hq4qF9uuH5ED1u6rpNs4+hvlVWTGZQFVtfdpyL3EnjULuXhePMychaFTsf02H5ypla\n9ZFwbmOkX1+znxsvQ71ddRzg3i8wZh+ou9f7vlgth77cLsFik26Y7L+Mf/HwhIebMY/ARyAppiSy\n6hHJWD5GQqGSLqGRdtJG2QRL6TGWlPqRSiOfEiqxyXx1aj6bEp7czGx3yiOf2D0nDz5Re0YenT9x\nek4eSctnzWj5rDQtn5Wg5bO0tHyWmpbPktPyWRhaPgtFy2eBtHz+/lmkwyNp+cwZLZ8xp+Xz3VQ4\nGc/615L9fHg3tq2vnybPNR8=\n"},
                                {"date": "20200902",
                                 "data": "eJzNlztvgzAQgP/LzQw+v7A9Nl0iZetYRcgCBqQ8UOJUiqL892JamsSkXSrEMeEz5/t8+gbuAr4M\nzUcTzuAuUPlQgwNUFhGFZvGBDI7B76ri1Bbl/rQL4HgGodnWb60vu89Rdct98JtiOKqIu+DYEC/9\nZn/oCiDXQ6hq4qF9uuH5ED1u6rpNs4+hvlVWTGZQFVtfdpyL3EnjULuXhePMychaFTsf02H5ypla\n9ZFwbmOkX1+znxsvQ71ddRzg3i8wZh+ou9f7vlgth77cLsFik26Y7L+Mf/HwhIebMY/ARyAppiSy\n6hHJWD5GQqGSLqGRdtJG2QRL6TGWlPqRSiOfEiqxyXx1aj6bEp7czGx3yiOf2D0nDz5Re0YenT9x\nek4eSctnzWj5rDQtn5Wg5bO0tHyWmpbPktPyWRhaPgtFy2eBtHz+/lmkwyNp+cwZLZ8xp+Xz3VQ4\nGc/615L9fHg3tq2vnybPNR8=\n"},
                            ]
                        }
                    elif self.uri == "/healthy/activity-list":
                        params = {
                            "uid": i["uid"]
                        }
                    elif self.uri == "/healthy/train-record-add":
                        params = {
                            "uid": i["uid"],
                            "data": [
                                # 新接口加密数据要可以正常解密，否则会报错
                                {"date": "20200901",
                                 "data": "eJxNj71uwzAMhN+FswfZiVqZW1B58Ng0u0FYqiPElg39BAmCvHtpd0i2w33k8fiAnJ0BhG+Tm+zaCxSQbEytZo91T+McnI2A5UcBE926c+iuNGYLWNcFDEtsfbKBLUDB87P/dcPpvjAvCzCdp4kltLoS8mcN35AUDM+WQjpSsuYVIXmHHd4oZb2vlFT7nRAC1qiJevZ1hYcGlcKDwuYLtd7Yf+zrTEx22QrRdXirrBQPu5jI93bDJgdKbvbrg+rz+QfpHlFy",
                                 "tid": str(i["uid"]) + "001",
                                 "detail": "eJyVkkFrhDAQhf9LznOIWZNNcluqB6GX0mNZJKgsodUVjYVF/O+diFvElK0LQ8i8JMP3no7k0vaZq2qixwlIZ1y1dL/7nuiPIwURgcKioJhfpfItrjIGGc3rEaSci4Hk87XDLHIv4t4XigKUmgvvxNiegZR5Y+qKaJIljPJ34hV3azdKbQoUEqZPqZZSn6ROX3SS4JmzJZ68lUM62OyToBHXGdvY5uINvNreoYfxmRFACvN17W5EcyCmcPa7yp31jILu5MX4sI+4ipnkMj5QSlHuXdXmxXVoEMlPQjbTFHiTTjAGpw+AVy//AgqZ1zyCsoUn8B06uScxE94bsXWoxP6JAVzgO8x3VxKecBPME5/8X4rHoXJFlwhW/87W/HSefgD4qfgE"},
                                {"date": "20200902",
                                 "data": "eJxNj71uwzAMhN+FswfZiVqZW1B58Ng0u0FYqiPElg39BAmCvHtpd0i2w33k8fiAnJ0BhG+Tm+zaCxSQbEytZo91T+McnI2A5UcBE926c+iuNGYLWNcFDEtsfbKBLUDB87P/dcPpvjAvCzCdp4kltLoS8mcN35AUDM+WQjpSsuYVIXmHHd4oZb2vlFT7nRAC1qiJevZ1hYcGlcKDwuYLtd7Yf+zrTEx22QrRdXirrBQPu5jI93bDJgdKbvbrg+rz+QfpHlFy",
                                 "tid": str(i["uid"]) + "002",
                                 "detail": "eJyVkkFrhDAQhf9LznOIWZNNcluqB6GX0mNZJKgsodUVjYVF/O+diFvElK0LQ8i8JMP3no7k0vaZq2qixwlIZ1y1dL/7nuiPIwURgcKioJhfpfItrjIGGc3rEaSci4Hk87XDLHIv4t4XigKUmgvvxNiegZR5Y+qKaJIljPJ34hV3azdKbQoUEqZPqZZSn6ROX3SS4JmzJZ68lUM62OyToBHXGdvY5uINvNreoYfxmRFACvN17W5EcyCmcPa7yp31jILu5MX4sI+4ipnkMj5QSlHuXdXmxXVoEMlPQjbTFHiTTjAGpw+AVy//AgqZ1zyCsoUn8B06uScxE94bsXWoxP6JAVzgO8x3VxKecBPME5/8X4rHoXJFlwhW/87W/HSefgD4qfgE"},
                                {"date": "20200903",
                                 "data": "eJxNj71uwzAMhN+FswfZiVqZW1B58Ng0u0FYqiPElg39BAmCvHtpd0i2w33k8fiAnJ0BhG+Tm+zaCxSQbEytZo91T+McnI2A5UcBE926c+iuNGYLWNcFDEtsfbKBLUDB87P/dcPpvjAvCzCdp4kltLoS8mcN35AUDM+WQjpSsuYVIXmHHd4oZb2vlFT7nRAC1qiJevZ1hYcGlcKDwuYLtd7Yf+zrTEx22QrRdXirrBQPu5jI93bDJgdKbvbrg+rz+QfpHlFy",
                                 "tid": str(i["uid"]) + "003",
                                 "detail": "eJyVkkFrhDAQhf9LznOIWZNNcluqB6GX0mNZJKgsodUVjYVF/O+diFvElK0LQ8i8JMP3no7k0vaZq2qixwlIZ1y1dL/7nuiPIwURgcKioJhfpfItrjIGGc3rEaSci4Hk87XDLHIv4t4XigKUmgvvxNiegZR5Y+qKaJIljPJ34hV3azdKbQoUEqZPqZZSn6ROX3SS4JmzJZ68lUM62OyToBHXGdvY5uINvNreoYfxmRFACvN17W5EcyCmcPa7yp31jILu5MX4sI+4ipnkMj5QSlHuXdXmxXVoEMlPQjbTFHiTTjAGpw+AVy//AgqZ1zyCsoUn8B06uScxE94bsXWoxP6JAVzgO8x3VxKecBPME5/8X4rHoXJFlwhW/87W/HSefgD4qfgE"},
                            ]
                        }
                    elif self.uri == "/healthy/train-record-list":
                        params = {
                            "uid": i["uid"]
                        }
                    elif self.uri == "/healthy/train-record-del":
                        params = {
                            "uid": i["uid"],
                            "tids": f'{i["uid"] + "001"},{i["uid"] + "002"}'
                        }
                    elif self.uri == "/healthy/train-record-info":
                        params = {
                            "uid": i["uid"],
                            "tid": i["uid"] + "003"
                        }
                    elif self.uri == "/user/up-device":
                        params = {
                            "uid": i["uid"],
                            "deviceType": "ID205S",
                            "mac": "FB:05:63:DE:31:8E",
                            "deviceInfo": json.dumps(
                                {"deviceAddress": "FB:05:63:DE:31:8E", "deviceId": 344, "deviceName": "ID205S",
                                 "deviceType": "ID205S", "iconId": 2131558401, "id": 0, "is": 0,
                                 "isInDfuMode": False, "len": 0, "rssi": -33}),
                        }
                    elif self.uri == "/user/stride-update":
                        params = {
                            "strideWalk": "65",
                            "strideRun": "100"
                        }
                    user_data.append(self.encrypt_data(params=params, token=i["token"]))
                    print(f"已生成第{len(user_data)}条数据，业务数据：{params}")

            with open(os.path.join(config.performance_path, filename), 'w') as f:
                if self.uri in ("/user/verify-email", "/user/logoff"):
                    f.write("token\n")
                elif self.uri == "/user/forget-password":
                    f.write("token,password,repassword\n")
                else:
                    f.write("token,data,sign,time_stamp\n")
                for i in user_data:
                    f.write(f"{i}\n")

            # 处理最后一行空行
            with open(os.path.join(config.performance_path, filename), "rb") as f:
                content = f.read()

            with open(os.path.join(config.performance_path, filename), "wb") as f:
                f.write(content[:-2])
        except UnboundLocalError:
            print("你输入的self.uri不存在，请确认后重新输入！")


# PD = PerformanceData(uri="/healthy/activity-add", table_name="hbdatacenter.hb_user")
# res = PD.generated_data()
