from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from myapp.models import User


class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)
            if user.password == password:
                print('登录成功')
                data = {
                    'username': username,
                    'datastr': '登录成功'
                }
                return JsonResponse(data)
            else:
                print('密码错误')
                return HttpResponse('密码错误')
        except User.DoesNotExist:
            print('查无此人')
            return HttpResponse('查无此人')
        except Exception as e:
            print('请求失败: ' + str(e))
            return HttpResponse('请求失败')
