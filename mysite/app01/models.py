from django.db import models


# ORM的使用
class UseInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=20)

    def __str__(self):
        return '{}-{}'.format(self.id, self.name)


# 出版社
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    # 不为空的唯一name
    name = models.CharField(null=False, max_length=64, unique=True)
    # addr = models.CharField(max_length=128,default='黄河路')
    addr = models.CharField(max_length=128)


# 书
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    kucun = models.IntegerField(default=1000)
    maichu = models.IntegerField(default=0)
    # 固定精度的十进制，总共5位，小数占2位
    price = models.DecimalField(decimal_places=2,max_digits=6,default=9.9)
    title = models.CharField(max_length=64, null=False, unique=True)
#     '''
#     在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，此参数为了避免两个表里的数据不一致问题，不然会报错：
# TypeError: __init__() missing 1 required positional argument: 'on_delete'
#     老版本这个参数（models.CASCADE）是默认值
#     参数说明：
# on_delete有CASCADE、PROTECT、SET_NULL、SET_DEFAULT、SET()五个可选择的值
# CASCADE：此值设置，是级联删除。
# PROTECT：此值设置，是会报完整性错误。
# SET_NULL：此值设置，会把外键设置为null，前提是允许为null。
# SET_DEFAULT：此值设置，会把设置为外键的默认值。
# SET()：此值设置，会调用外面的值，可以是一个函数。
#     '''

    # 会自动加_id
    # related_name= 反向查找的名字 对象  使用obj.related_name
    # related_query_name 反向 字段查询
    publisher = models.ForeignKey(
        to="Publisher",
        on_delete=models.CASCADE,
        # related_name='books',
        # related_query_name='xx_books'
    )

    def __str__(self):
        return self.title


# 作者表
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16,unique=True,null=False)
    book = models.ManyToManyField(to='Book')  # orm会自动创建多对多id表

    def __str__(self):
        return self.name

