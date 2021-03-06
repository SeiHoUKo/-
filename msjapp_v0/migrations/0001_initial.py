# Generated by Django 3.2.6 on 2021-08-21 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ADMIN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=8, verbose_name='真实姓名')),
                ('admin_sex', models.CharField(max_length=2, verbose_name='性别')),
                ('admin_password', models.CharField(max_length=25, verbose_name='密码')),
                ('admin_id', models.CharField(max_length=30, verbose_name='手机号/账户')),
            ],
        ),
        migrations.CreateModel(
            name='CHEF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chef_name', models.CharField(max_length=8, verbose_name='真实姓名')),
                ('chef_sex', models.CharField(max_length=2, verbose_name='性别')),
                ('chef_password', models.CharField(max_length=25, verbose_name='密码')),
                ('chef_id', models.CharField(max_length=30, verbose_name='手机号/账户')),
            ],
        ),
        migrations.CreateModel(
            name='DESK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desk_id', models.CharField(max_length=2, verbose_name='桌号')),
                ('desk_state', models.BooleanField(verbose_name='桌子状态')),
            ],
        ),
        migrations.CreateModel(
            name='DISH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=8, verbose_name='菜名')),
                ('dish_picture', models.ImageField(upload_to='', verbose_name='菜图')),
                ('dish_describe', models.TextField(max_length=300, verbose_name='菜品介绍')),
                ('dish_price', models.FloatField(max_length=4, verbose_name='菜的价格')),
                ('dish_id', models.IntegerField(max_length=8, verbose_name='菜的编号')),
            ],
        ),
        migrations.CreateModel(
            name='ORDERS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders_id', models.IntegerField(max_length=8, verbose_name='订单的编号')),
                ('orders_user', models.CharField(max_length=30, verbose_name='订单的用户')),
                ('orders_state', models.CharField(max_length=3, verbose_name='订单的状态')),
                ('orders_price', models.FloatField(max_length=10, verbose_name='订单的价格')),
                ('orders_time', models.DateField(verbose_name='订单的时间')),
            ],
        ),
        migrations.CreateModel(
            name='ORDERS_to_DISH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders_id', models.IntegerField(max_length=8, verbose_name='订单的编号')),
                ('dish_id', models.IntegerField(max_length=8, verbose_name='菜的编号')),
            ],
        ),
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=8, verbose_name='真实姓名')),
                ('user_sex', models.CharField(max_length=2, verbose_name='性别')),
                ('user_password', models.CharField(max_length=25, verbose_name='密码')),
                ('user_id', models.CharField(max_length=30, verbose_name='手机号/账户')),
                ('user_picture', models.ImageField(upload_to='', verbose_name='头像')),
            ],
        ),
        migrations.CreateModel(
            name='WAITER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waiter_name', models.CharField(max_length=8, verbose_name='真实姓名')),
                ('waiter_sex', models.CharField(max_length=2, verbose_name='性别')),
                ('waiter_password', models.CharField(max_length=25, verbose_name='密码')),
                ('waiter_id', models.CharField(max_length=30, verbose_name='手机号/账户')),
            ],
        ),
    ]
