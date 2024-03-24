# Create your models here.
from django.db import models


# 用户表
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


# 目标识别算法-不需要清扫的垃圾
class Data(models.Model):
    # 原始数据字段，用于存储未经处理或者原始格式的数据，长度限制魏1000字符
    notify_data = models.CharField(max_length=1000)
    # 服务ID字段，用于标识与该数据记录相关服务，长度限制魏100字符
    service_id = models.CharField(max_length=100)
    # 事件时间字段，用于存储该数据记录产生的时间戳，长度限制魏100字符
    event_time = models.CharField(max_length=100)
    # 设备ID字段，用于关联生成该数据的设备，长度限制魏100字符
    device_id = models.CharField(max_length=100)
    # image值字段，用于Base64的图像数据，可以为空（null=Ture）且允许留空（blank=Ture）
    image_Value = models.CharField(null=True, blank=True, max_length=10240)
    # 类别字段
    class_name = models.CharField(max_length=100)
    # 置信度字段
    score = models.CharField(max_length=100)


# 图像分类算法-烟头表
class SmokeData(models.Model):
    # 原始数据字段，用于存储未经处理或者原始格式的数据，长度限制魏1000字符
    notify_data = models.CharField(max_length=1000)
    # 服务ID字段，用于标识与该数据记录相关服务，长度限制魏100字符
    service_id = models.CharField(max_length=100)
    # 事件时间字段，用于存储该数据记录产生的时间戳，长度限制魏100字符
    event_time = models.CharField(max_length=100)
    # 设备ID字段，用于关联生成该数据的设备，长度限制魏100字符
    device_id = models.CharField(max_length=100)
    # image值字段，用于Base64的图像数据，可以为空（null=Ture）且允许留空（blank=Ture）
    smoke_Value = models.CharField(null=True, blank=True, max_length=10240)
    # 类别字段
    class_name = models.CharField(max_length=100)
    # 置信度字段
    score = models.CharField(max_length=100)


# 图像分类算法-餐盒表
class FoodData(models.Model):
    # 原始数据字段，用于存储未经处理或者原始格式的数据，长度限制魏1000字符
    notify_data = models.CharField(max_length=1000)
    # 服务ID字段，用于标识与该数据记录相关服务，长度限制魏100字符
    service_id = models.CharField(max_length=100)
    # 事件时间字段，用于存储该数据记录产生的时间戳，长度限制魏100字符
    event_time = models.CharField(max_length=100)
    # 设备ID字段，用于关联生成该数据的设备，长度限制魏100字符
    device_id = models.CharField(max_length=100)
    # image值字段，用于Base64的图像数据，可以为空（null=Ture）且允许留空（blank=Ture）
    foodbox_Value = models.CharField(null=True, blank=True, max_length=10240)
    # 类别字段
    class_name = models.CharField(max_length=100)
    # 置信度字段
    score = models.CharField(max_length=100)


# 图像分类算法-果皮表
class FruitData(models.Model):
    # 原始数据字段，用于存储未经处理或者原始格式的数据，长度限制魏1000字符
    notify_data = models.CharField(max_length=1000)
    # 服务ID字段，用于标识与该数据记录相关服务，长度限制魏100字符
    service_id = models.CharField(max_length=100)
    # 事件时间字段，用于存储该数据记录产生的时间戳，长度限制魏100字符
    event_time = models.CharField(max_length=100)
    # 设备ID字段，用于关联生成该数据的设备，长度限制魏100字符
    device_id = models.CharField(max_length=100)
    # image值字段，用于Base64的图像数据，可以为空（null=Ture）且允许留空（blank=Ture）
    fruit_Value = models.CharField(null=True, blank=True, max_length=10240)
    # 类别字段
    class_name = models.CharField(max_length=100)
    # 置信度字段
    score = models.CharField(max_length=100)


# 图像分类算法-蛋壳表
class EggData(models.Model):
    # 原始数据字段，用于存储未经处理或者原始格式的数据，长度限制魏1000字符
    notify_data = models.CharField(max_length=1000)
    # 服务ID字段，用于标识与该数据记录相关服务，长度限制魏100字符
    service_id = models.CharField(max_length=100)
    # 事件时间字段，用于存储该数据记录产生的时间戳，长度限制魏100字符
    event_time = models.CharField(max_length=100)
    # 设备ID字段，用于关联生成该数据的设备，长度限制魏100字符
    device_id = models.CharField(max_length=100)
    # image值字段，用于Base64的图像数据，可以为空（null=Ture）且允许留空（blank=Ture）
    egg_Value = models.CharField(null=True, blank=True, max_length=10240)
    # 类别字段
    class_name = models.CharField(max_length=100)
    # 置信度字段
    score = models.CharField(max_length=100)


# 图像分类算法-玩具表
class ToyData(models.Model):
    # 原始数据字段，用于存储未经处理或者原始格式的数据，长度限制魏1000字符
    notify_data = models.CharField(max_length=1000)
    # 服务ID字段，用于标识与该数据记录相关服务，长度限制魏100字符
    service_id = models.CharField(max_length=100)
    # 事件时间字段，用于存储该数据记录产生的时间戳，长度限制魏100字符
    event_time = models.CharField(max_length=100)
    # 设备ID字段，用于关联生成该数据的设备，长度限制魏100字符
    device_id = models.CharField(max_length=100)
    # image值字段，用于Base64的图像数据，可以为空（null=Ture）且允许留空（blank=Ture）
    toy_Value = models.CharField(null=True, blank=True, max_length=10240)
    # 类别字段
    class_name = models.CharField(max_length=100)
    # 置信度字段
    score = models.CharField(max_length=100)


# 图像分类算法-纸箱表
class BoxData(models.Model):
    # 原始数据字段，用于存储未经处理或者原始格式的数据，长度限制魏1000字符
    notify_data = models.CharField(max_length=1000)
    # 服务ID字段，用于标识与该数据记录相关服务，长度限制魏100字符
    service_id = models.CharField(max_length=100)
    # 事件时间字段，用于存储该数据记录产生的时间戳，长度限制魏100字符
    event_time = models.CharField(max_length=100)
    # 设备ID字段，用于关联生成该数据的设备，长度限制魏100字符
    device_id = models.CharField(max_length=100)
    # image值字段，用于Base64的图像数据，可以为空（null=Ture）且允许留空（blank=Ture）
    box_Value = models.CharField(null=True, blank=True, max_length=10240)
    # 类别字段
    class_name = models.CharField(max_length=100)
    # 置信度字段
    score = models.CharField(max_length=100)


# 图像分类算法-电池表
class BatteryData(models.Model):
    # 原始数据字段，用于存储未经处理或者原始格式的数据，长度限制魏1000字符
    notify_data = models.CharField(max_length=1000)
    # 服务ID字段，用于标识与该数据记录相关服务，长度限制魏100字符
    service_id = models.CharField(max_length=100)
    # 事件时间字段，用于存储该数据记录产生的时间戳，长度限制魏100字符
    event_time = models.CharField(max_length=100)
    # 设备ID字段，用于关联生成该数据的设备，长度限制魏100字符
    device_id = models.CharField(max_length=100)
    # image值字段，用于Base64的图像数据，可以为空（null=Ture）且允许留空（blank=Ture）
    battery_Value = models.CharField(null=True, blank=True, max_length=10240)
    # 类别字段
    class_name = models.CharField(max_length=100)
    # 置信度字段
    score = models.CharField(max_length=100)


# 图像分类算法-药物表
class MedicineData(models.Model):
    # 原始数据字段，用于存储未经处理或者原始格式的数据，长度限制魏1000字符
    notify_data = models.CharField(max_length=1000)
    # 服务ID字段，用于标识与该数据记录相关服务，长度限制魏100字符
    service_id = models.CharField(max_length=100)
    # 事件时间字段，用于存储该数据记录产生的时间戳，长度限制魏100字符
    event_time = models.CharField(max_length=100)
    # 设备ID字段，用于关联生成该数据的设备，长度限制魏100字符
    device_id = models.CharField(max_length=100)
    # image值字段，用于Base64的图像数据，可以为空（null=Ture）且允许留空（blank=Ture）
    medicine_Value = models.CharField(null=True, blank=True, max_length=10240)
    # 类别字段
    class_name = models.CharField(max_length=100)
    # 置信度字段
    score = models.CharField(max_length=100)
