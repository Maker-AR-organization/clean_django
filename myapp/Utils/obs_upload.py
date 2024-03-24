# 图像上传到华为云OBS桶返回URL
import os
import traceback
import uuid

from obs import ObsClient


def obs_upload_file(files_name, image):
    ak = "0QOEBQ4Y9GQ4YRFKH8QF"
    sk = "FUgLdQyiLwmtQgDYjjeecfuu2HUHEx4DB2tto5h1"
    # server填写Bucket对应的Endpoint, 这里以中国-华北四为例，其他地区请按实际情况填写。
    server = "https://obs.cn-north-4.myhuaweicloud.com"
    # 创建obsClient实例
    # 如果使用临时AKSK和SecurityToken访问OBS，需要在创建实例时通过security_token参数指定securityToken值
    obsClient = ObsClient(access_key_id=ak, secret_access_key=sk, server=server)
    try:
        bucketName = "saodi"
        # 利用uuid生成不会重复的名称
        objectKey = files_name + "/" + str(uuid.uuid4()) + os.path.splitext(image)[1]
        # 设置带上传的文本内容
        file_path = image
        # 上传文本对象
        resp = obsClient.uploadFile(bucketName, objectKey, file_path)
        url = "https://" + bucketName + "." + "obs.cn-north-4.myhuaweicloud.com" + "/" + objectKey
        return url

    except:
        print('Put Content Failed')
        print(traceback.format_exc())
