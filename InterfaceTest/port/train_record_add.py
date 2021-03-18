from common.send_request import SendRequests


params = {
    "uid": 163946,
    "data": [
        # 新接口加密数据要可以正常解密，否则会报错
        {"date": "20201002",
         "data": "eJxNj71uwzAMhN+FswfZiVqZW1B58Ng0u0FYqiPElg39BAmCvHtpd0i2w33k8fiAnJ0BhG+Tm+zaCxSQbEytZo91T+McnI2A5UcBE926c+iuNGYLWNcFDEtsfbKBLUDB87P/dcPpvjAvCzCdp4kltLoS8mcN35AUDM+WQjpSsuYVIXmHHd4oZb2vlFT7nRAC1qiJevZ1hYcGlcKDwuYLtd7Yf+zrTEx22QrRdXirrBQPu5jI93bDJgdKbvbrg+rz+QfpHlFy",
         "tid": "tid001",
         "detail": "eJyVkkFrhDAQhf9LznOIWZNNcluqB6GX0mNZJKgsodUVjYVF/O+diFvElK0LQ8i8JMP3no7k0vaZq2qixwlIZ1y1dL/7nuiPIwURgcKioJhfpfItrjIGGc3rEaSci4Hk87XDLHIv4t4XigKUmgvvxNiegZR5Y+qKaJIljPJ34hV3azdKbQoUEqZPqZZSn6ROX3SS4JmzJZ68lUM62OyToBHXGdvY5uINvNreoYfxmRFACvN17W5EcyCmcPa7yp31jILu5MX4sI+4ipnkMj5QSlHuXdXmxXVoEMlPQjbTFHiTTjAGpw+AVy//AgqZ1zyCsoUn8B06uScxE94bsXWoxP6JAVzgO8x3VxKecBPME5/8X4rHoXJFlwhW/87W/HSefgD4qfgE"},
        {"date": "20200902",
         "data": "eJxNj71uwzAMhN+FswfZiVqZW1B58Ng0u0FYqiPElg39BAmCvHtpd0i2w33k8fiAnJ0BhG+Tm+zaCxSQbEytZo91T+McnI2A5UcBE926c+iuNGYLWNcFDEtsfbKBLUDB87P/dcPpvjAvCzCdp4kltLoS8mcN35AUDM+WQjpSsuYVIXmHHd4oZb2vlFT7nRAC1qiJevZ1hYcGlcKDwuYLtd7Yf+zrTEx22QrRdXirrBQPu5jI93bDJgdKbvbrg+rz+QfpHlFy",
         "tid": "tid002",
         "detail": "eJyVkkFrhDAQhf9LznOIWZNNcluqB6GX0mNZJKgsodUVjYVF/O+diFvElK0LQ8i8JMP3no7k0vaZq2qixwlIZ1y1dL/7nuiPIwURgcKioJhfpfItrjIGGc3rEaSci4Hk87XDLHIv4t4XigKUmgvvxNiegZR5Y+qKaJIljPJ34hV3azdKbQoUEqZPqZZSn6ROX3SS4JmzJZ68lUM62OyToBHXGdvY5uINvNreoYfxmRFACvN17W5EcyCmcPa7yp31jILu5MX4sI+4ipnkMj5QSlHuXdXmxXVoEMlPQjbTFHiTTjAGpw+AVy//AgqZ1zyCsoUn8B06uScxE94bsXWoxP6JAVzgO8x3VxKecBPME5/8X4rHoXJFlwhW/87W/HSefgD4qfgE"},
        {"date": "20200903",
         "data": "eJxNj71uwzAMhN+FswfZiVqZW1B58Ng0u0FYqiPElg39BAmCvHtpd0i2w33k8fiAnJ0BhG+Tm+zaCxSQbEytZo91T+McnI2A5UcBE926c+iuNGYLWNcFDEtsfbKBLUDB87P/dcPpvjAvCzCdp4kltLoS8mcN35AUDM+WQjpSsuYVIXmHHd4oZb2vlFT7nRAC1qiJevZ1hYcGlcKDwuYLtd7Yf+zrTEx22QrRdXirrBQPu5jI93bDJgdKbvbrg+rz+QfpHlFy",
         "tid": "tid003",
         "detail": "eJyVkkFrhDAQhf9LznOIWZNNcluqB6GX0mNZJKgsodUVjYVF/O+diFvElK0LQ8i8JMP3no7k0vaZq2qixwlIZ1y1dL/7nuiPIwURgcKioJhfpfItrjIGGc3rEaSci4Hk87XDLHIv4t4XigKUmgvvxNiegZR5Y+qKaJIljPJ34hV3azdKbQoUEqZPqZZSn6ROX3SS4JmzJZ68lUM62OyToBHXGdvY5uINvNreoYfxmRFACvN17W5EcyCmcPa7yp31jILu5MX4sI+4ipnkMj5QSlHuXdXmxXVoEMlPQjbTFHiTTjAGpw+AVy//AgqZ1zyCsoUn8B06uScxE94bsXWoxP6JAVzgO8x3VxKecBPME5/8X4rHoXJFlwhW/87W/HSefgD4qfgE"},
    ],
}

# 体能训练数据上传
t = SendRequests(method="post", uri="/v1/healthy/train-record-add", param=params,
                 token="OZFEfyhRXeCwaieMaXEbAi_ttLDHwB8Y", is_sign=True)

t.send_request()
