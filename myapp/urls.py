from django.urls import path
from myapp import views
from myapp.IotData.IotData_Fenlei import IotData_Fenlei
from myapp.IotData.IotData_Jiance import IotData_Jiance
from myapp.IotData.IotData_ON import IotData_ON
from myapp.IotData.IotData_OFF import IotData_OFF
from myapp.User.Login import Login
from myapp.User.Register import Register

urlpatterns = [
    path('update_Jiance/', IotData_Jiance.as_view()),  # 从iot平台推送的信息访问目标检测算法
    path('update_Fenlei/', IotData_Fenlei.as_view()),  # 从iot平台推送的信息访问图像分类算法
    path('iotdata_on/', IotData_ON.as_view()),  # 调用命令下发API，ON
    path('iotdata_off/', IotData_OFF.as_view()),  # 调用命令下发API，OFF
    path('app/user/login/', Login.as_view()),  # 客户端用户登录校验
    path('app/user/register/', Register.as_view()),  # 客户端用户注册校验
    path('app/mubiao/', views.Mubiao_AppReq.as_view()),  # 目标检测
    path('app/battery/', views.Battery_AppReq.as_view()),  # 电池
    path('app/box/', views.Box_AppReq.as_view()),  # 纸盒
    path('app/egg/', views.Egg_AppReq.as_view()),  # 蛋壳
    path('app/food/', views.Food_AppReq.as_view()),  # 一次性餐盒
    path('app/fruit/', views.Fruit_AppReq.as_view()),  # 果皮
    path('app/medicine/', views.Medicine_AppReq.as_view()),  # 药品
    path('app/somke/', views.Smoke_AppReq.as_view()),  # 烟头
    path('app/toy/', views.Toy_AppReq.as_view()),  # 玩具
]
