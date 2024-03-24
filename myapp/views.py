from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from myapp.models import Data, SmokeData, BoxData, EggData, ToyData, FoodData, MedicineData, BatteryData, FruitData


# 目标检测接口
class Mubiao_AppReq(APIView):
    def get(self, request):
        try:
            # 获取最新的目标检测图像
            mysqlData = Data.objects.last()
            return HttpResponse(mysqlData.image_Value)
        except Data.DoesNotExist:
            # 如果 Data 对象不存在，则返回指定的消息
            return HttpResponse("数据不存在")


# 纸盒接口
class Box_AppReq(APIView):
    def get(self, request):
        try:
            # 获取最新的纸箱图像
            mysqlData = BoxData.objects.last()
            return HttpResponse(mysqlData.box_Value)
        except BoxData.DoesNotExist:
            # 如果 Data 对象不存在，则返回指定的消息
            return HttpResponse("数据不存在")


# 蛋壳接口
class Egg_AppReq(APIView):
    def get(self, request):
        try:
            # 获取最新的蛋壳图像
            mysqlData = EggData.objects.last()
            return HttpResponse(mysqlData.egg_Value)
        except EggData.DoesNotExist:
            # 如果 Data 对象不存在，则返回指定的消息
            return HttpResponse("数据不存在")


# 果皮接口
class Fruit_AppReq(APIView):
    def get(self, request):
        try:
            # 获取最新的果皮图像
            mysqlData = FruitData.objects.last()
            print(mysqlData)
            return HttpResponse(mysqlData.fruit_Value)
        except FruitData.DoesNotExist:
            # 如果 Data 对象不存在，则返回指定的消息
            return HttpResponse("数据不存在")


# 电池接口
class Battery_AppReq(APIView):
    def get(self, request):
        try:
            # 获取最新的电池图像
            mysqlData = BatteryData.objects.last()
            print(mysqlData)
            return HttpResponse(mysqlData.battery_Value)
        except BatteryData.DoesNotExist:
            # 如果 Data 对象不存在，则返回指定的消息
            return HttpResponse("数据不存在")


# 一次性餐盒接口
class Food_AppReq(APIView):
    def get(self, request):
        try:
            # 获取最新的一次性餐盒图像
            mysqlData = FoodData.objects.last()
            print(mysqlData)
            return HttpResponse(mysqlData.food_Value)
        except FoodData.DoesNotExist:
            # 如果 Data 对象不存在，则返回指定的消息
            return HttpResponse("数据不存在")


# 药物接口
class Medicine_AppReq(APIView):
    def get(self, request):
        try:
            # 获取最新的药物图像
            mysqlData = MedicineData.objects.last()
            print(mysqlData)
            return HttpResponse(mysqlData.medicine_Value)
        except MedicineData.DoesNotExist:
            # 如果 Data 对象不存在，则返回指定的消息
            return HttpResponse("数据不存在")


# 烟头接口
class Smoke_AppReq(APIView):
    def get(self, request):
        try:
            # 获取最新的烟头图像
            mysqlData = SmokeData.objects.last()
            print(mysqlData)
            return HttpResponse(mysqlData.smoke_Value)
        except SmokeData.DoesNotExist:
            # 如果 Data 对象不存在，则返回指定的消息
            return HttpResponse("数据不存在")


# 玩具接口
class Toy_AppReq(APIView):
    def get(self, request):
        try:
            # 获取最新的玩具图像
            mysqlData = ToyData.objects.last()
            print(mysqlData)
            return HttpResponse(mysqlData.toy_Value)
        except ToyData.DoesNotExist:
            # 如果 Data 对象不存在，则返回指定的消息
            return HttpResponse("数据不存在")
