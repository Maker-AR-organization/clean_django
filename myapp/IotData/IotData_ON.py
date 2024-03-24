from rest_framework.views import APIView
from rest_framework.response import Response
# 华为云IotDA的SDK
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.auth.credentials import DerivedCredentials
from huaweicloudsdkiotda.v5.region.iotda_region import IoTDARegion
from huaweicloudsdkiotda.v5 import *
from huaweicloudsdkcore.exceptions import exceptions


# 开启摄像头
class IotData_ON(APIView):
    def post(self, request):

        ak = "0QOEBQ4Y9GQ4YRFKH8QF"

        sk = "FUgLdQyiLwmtQgDYjjeecfuu2HUHEx4DB2tto5h1"

        credentials = BasicCredentials(ak, sk).with_derived_predicate(
            DerivedCredentials.get_default_derived_predicate())
        client = IoTDAClient.new_builder() \
            .with_credentials(credentials) \
            .with_region(IoTDARegion.value_of("cn-north-4")) \
            .build()

        try:
            request = CreateCommandRequest()
            request.device_id = "65eab957fb8177243a4cdfc3_123456"
            request.body = DeviceCommandRequest(
                paras="{\"Control\":\"ON\"}",
                command_name="Image_Control",
                service_id="saodi"
            )
            response = client.create_command(request)
            return Response(response.to_dict())  # 返回JSON格式响应
        except exceptions.ClientRequestException as e:
            error_response = {
                'status_code': e.status_code,
                'request_id': e.request_id,
                'error_code': e.error_code,
                'error_msg': e.error_msg
            }
            return Response(error_response)  # 返回JSON格式错误响应
