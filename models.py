from django.db import models

# Create your models here.
class USER(models.Model):
    user_name = models.CharField(max_length=8,verbose_name="真实姓名") 
    user_sex = models.CharField(max_length=2,verbose_name="性别") 
    user_password = models.CharField(min_length=6,max_length=25,verbose_name="密码")
    user_id = models.CharField(max_length=30,verbose_name="手机号/账户")
    user_picture = models.ImageField(verbose_name="头像")#图片

class WAITER(models.Model):
    waiter_name = models.CharField(max_length=8,verbose_name="真实姓名")    
    waiter_sex = models.CharField(max_length=2,verbose_name="性别")
    waiter_password = models.CharField(min_length=6,max_length=25,verbose_name="密码")  
    waiter_id = models.CharField(max_length=30,verbose_name="手机号/账户")

class CHEF(models.Model):
    chef_name = models.CharField(max_length=8,verbose_name="真实姓名")
    chef_sex = models.CharField(max_length=2,verbose_name="性别")
    chef_password = models.CharField(min_length=6,max_length=25,verbose_name="密码")
    chef_id = models.CharField(max_length=30,verbose_name="手机号/账户")

class ADMIN(models.Model):
    admin_name = models.CharField(max_length=8,verbose_name="真实姓名")
    admin_sex = models.CharField(max_length=2,verbose_name="性别")
    admin_password = models.CharField(min_length=6,max_length=25,verbose_name="密码")
    admin_id = models.CharField(max_length=30,verbose_name="手机号/账户")

class DESK(models.Model):
    desk_id = models.CharField(max_length=2,verbose_name="桌号")
    desk_state = models.BooleanField(verbose_name="桌子状态")#布尔

class DISH(models.Model):
    dish_name = models.CharField(max_length=8,verbose_name="菜名")  
    dish_picture = models.CharField(verbose_name="菜图")
    dish_describe = models.TextField(max_length=300,verbose_name="菜品介绍")#长文本
    dish_price = models.FloatField(max_length=4,verbose_name="菜的价格") #小数
    dish_id = models.IntegerField(max_length=8,verbose_name="菜的编号") #整数

class ORDERS(models.Model):
    orders_id = models.IntegerField(max_length=8,verbose_name="订单的编号")#/整数
    orders_user = models.CharField(max_length=30,verbose_name="订单的用户")
    orders_state = models.CharField(max_length=3,verbose_name="订单的状态")
    orders_price = models.FloatField(max_length=10,verbose_name="订单的价格")#小数
    orders_time = models.DateField(verbose_name="订单的时间")#日期

class ORDERS_to_DISH(models.Model):
    orders_id = models.IntegerField(max_length=8,verbose_name="订单的编号")#整数
    dish_id = models.IntegerField(max_length=8,verbose_name="菜的编号") #整数