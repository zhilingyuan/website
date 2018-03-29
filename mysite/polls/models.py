from django.db import models
import datetime
from django.utils import timezone# 这两个是为了替代str做一个实用性更强的标记

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
    question=models.ForeignKey(Question,
                              on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text#__str__(self)的作用在于创建表征对象<question:question object (1)> 的str
'''
ForeignKey,ManyToManyField与OneToOneField分别在Model中定义多对一，
多对多，一对一关系。

例如，一本书由一家出版社出版，一家出版社可以出版很多书。一本书由多个作者合写，
一个作者可以写很多书。

class Author(models.Model):
    name=models.CharField(max_length=20)
class Publisher(models.Model):
    name=models.CharField(max_length=20)
class Book(models.Model):
    name=models.CharField(max_length=20)
    pub=models.ForeignKey(Publisher)
    authors=models.ManyToManyField(Author)
'''
