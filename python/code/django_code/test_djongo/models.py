from django.db import models

# Create your models here.
# 创建Book表
class Book(models.Model):

    # 表自增字段
    id = models.AutoField(primary_key=True)

    # 创建热销书籍
    hoot_book = models.BooleanField(null=True,default=1)

    # 价格
    book_money = models.IntegerField(default=100)

    # 书名
    book_name = models.CharField(max_length=40,unique=True)

    # 书籍评论信息字段
    book_info = models.TextField(blank=True)

    # 书籍创建时间
    book_date = models.DateField()

    # 创建关联表，关联出版社信息
    # 出版社属于一对多模型，类似一本书对应一个出版社
    book_publish = models.ForeignKey("Book_Publish_Info", on_delete=models.CASCADE)

    # 创建第三张关联表
    # 此表记录了书籍对应的作者信息
    # 创建多对多表，类似"西游记"书籍，作者有俩个人 "A"和"B"作者
    # 自动生成第三张表格维护对应关系信息
    book_author = models.ManyToManyField("Book_Author_Info",db_table='tb_book_author_many')


    class Meta():

        db_table = 'tb_book'


# 创建出版社信息表
class Book_Publish_Info(models.Model):

    # id
    id = models.AutoField(primary_key=True)
    # 出版社名称
    publish_name = models.CharField(max_length=40)

    class Meta():

        db_table = 'tb_publish'

    def __str__(self):

        return self.publish_name


# 创建作者邮箱表
class Book_Author_Emaill(models.Model):

    # id
    id = models.AutoField(primary_key=True)
    # 邮箱地址
    emaill = models.EmailField()


    class Meta():

        db_table = 'tb_author_emaill'

    def __str__(self):

        return  self.emaill


# 创建作者信息表
class Book_Author_Info(models.Model):

    CHOICES = [

        ('0','女性'),
        ('1','男性'),
        ('2','保密')
    ]

    # id
    id = models.AutoField(primary_key=True)
    # 作者姓名
    author_name = models.CharField(max_length=40)
    # 创建一对一模型
    # 作者邮箱 ，邮箱都是唯一的
    author_emaill = models.OneToOneField(to="Book_Author_Emaill",on_delete=models.CASCADE,primary_key=True)
    author_emaill = models.EmailField()
    # 作者性别
    author_gender = models.CharField(max_length=10,choices=CHOICES)

    class Meta():

        db_table = 'tb_author_info'

    def __str__(self):

        return self.author_name