from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from myapp.models import User


class Register(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)
            print('用户名已存在')
            return HttpResponse('用户名已存在')
        except User.DoesNotExist:
            new_user = User.objects.create(username=username, password=password)
            print('注册成功')
            data = {
                'username': username,
                'datastr': '注册成功'
            }
            return JsonResponse(data)
        except Exception as e:
            print('注册失败: ' + str(e))
            return HttpResponse('注册失败')
