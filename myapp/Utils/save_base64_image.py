import base64
import io
from PIL import Image


# 解码Base64，并保存为图片
def save_base64(base64_data, file_path):
    # 解码base64字符串
    image_data = base64.b64decode(base64_data)

    # 将解码后的数据转换为字节流
    image_stream = io.BytesIO(image_data)

    # 打开图像
    image_open = Image.open(image_stream)

    # 保存图像文件
    image_open.save(file_path)
