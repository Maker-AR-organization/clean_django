import json

from huaweicloudsdkiam.v3 import KeystoneCreateUserTokenByPasswordResponse


# 自定义编码器将response对象转换为JSON字符串
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, KeystoneCreateUserTokenByPasswordResponse):
            return obj.to_dict()
        return super().default(obj)
