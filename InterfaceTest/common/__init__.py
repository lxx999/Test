import zlib
import base64
import hashlib
import random


def decode_data(enciphered_data: str):
    """
    解密活动记录和体能记录数据库加密数据
    :param enciphered_data:加密字符串
    :return:解密后的数据
    """

    # 指定替换
    replace_data = enciphered_data.replace("\\n", "\\\\n").replace('\\\\n', "\n").replace("\\\\r", "\r").replace(
        "\\\\t", "\t")

    # base64解码
    base_data = base64.b64decode(replace_data)

    # 解压
    decompress_data = zlib.decompress(base_data)

    return decompress_data


def md5_encryption(s: str):
    """
    md5加密字符串
    :param s: 待加密字符串
    :return: 加密完的字符串
    """
    md5_str = hashlib.md5(s.encode("utf-8")).hexdigest()

    return md5_str


def create_number_set():
    """
    生成数字+字母组合一起的集合
    :return:
    """
    number_set = [chr(i) for i in range(48, 58)]
    char_set = [chr(i) for i in range(97, 123)]
    total_set = number_set + char_set

    return total_set


def create_uuid():
    """
    生成36位数uuid
    :return:
    """
    data = ''
    for i in range(36):
        max_letter = chr(random.randint(65, 90))
        min_letter = chr(random.randint(97, 122))
        number = random.randint(0, 9)
        data_li = [number, min_letter, max_letter]
        random_index = random.randint(0, 2)
        s = str(data_li[random_index])
        if i in (8, 13, 18, 23):
            s = "-"
        data += s
    return data


def create_tid():
    """
    生成8位数tid
    :return:
    """
    data = ''
    for i in range(8):
        max_letter = chr(random.randint(65, 90))
        min_letter = chr(random.randint(97, 122))
        number = random.randint(0, 9)
        data_li = [number, min_letter, max_letter]
        random_index = random.randint(0, 2)
        s = str(data_li[random_index])
        data += s

    return data


def create_mac():
    """
    生成随机mac地址
    :return:mac
    """
    mac = ""
    for i in range(6):
        s = "".join(random.sample(create_number_set(), 2))
        mac = mac + s + ":"

    return mac[:-1].upper()


def base64_decode(data: str):
    """ 解密数据"""

    join_data = data[-2:] + data[:-2]

    de_data = base64.b64decode(join_data)

    return de_data
