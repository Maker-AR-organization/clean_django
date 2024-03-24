from huaweicloudsdkcore.auth.credentials import GlobalCredentials
from huaweicloudsdkiam.v3 import IamClient, KeystoneCreateUserTokenByPasswordRequest, AuthScopeProject, AuthScope, \
    PwdPasswordUserDomain, PwdPasswordUser, PwdPassword, PwdIdentity, PwdAuth, \
    KeystoneCreateUserTokenByPasswordRequestBody
from huaweicloudsdkiam.v3.region.iam_region import IamRegion
from huaweicloudsdkcore.exceptions import exceptions
import json
from myapp.Utils.CustomEncoder import CustomEncoder


def Get_Token():
    ak = "0QOEBQ4Y9GQ4YRFKH8QF"
    sk = "FUgLdQyiLwmtQgDYjjeecfuu2HUHEx4DB2tto5h1"

    credentials = GlobalCredentials(ak, sk)

    client = IamClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(IamRegion.value_of("cn-north-4")) \
        .build()

    try:
        request = KeystoneCreateUserTokenByPasswordRequest()
        projectScope = AuthScopeProject(
            id="6605e551a8bb4caaa0d735382c08ff3f",
            name="cn-north-4"
        )
        scopeAuth = AuthScope(
            project=projectScope
        )
        domainUser = PwdPasswordUserDomain(
            name="ws1924605640"
        )
        userPassword = PwdPasswordUser(
            domain=domainUser,
            name="ws060612",
            password="1924605640Ws"
        )
        passwordIdentity = PwdPassword(
            user=userPassword
        )
        listMethodsIdentity = [
            "password"
        ]
        identityAuth = PwdIdentity(
            methods=listMethodsIdentity,
            password=passwordIdentity
        )
        authbody = PwdAuth(
            identity=identityAuth,
            scope=scopeAuth
        )
        request.body = KeystoneCreateUserTokenByPasswordRequestBody(
            auth=authbody
        )
        response = client.keystone_create_user_token_by_password(request)

        # 使用自定义编码器将response对象转换为JSON字符串
        response_str = json.dumps(response, cls=CustomEncoder)

        # 解析JSON数据
        json_data = json.loads(response_str)

        # # 获取"X-Subject-Token"字段的值
        x_subject_token = json_data["x_subject_token"]
        return x_subject_token
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
