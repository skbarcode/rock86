from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

from DjangoUeditor.models import UEditorField


# Create your models here.


class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:  # 不生成表
        abstract = True


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='呢称', default='')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    address = models.CharField(max_length=100, verbose_name="地址", default='')
    mobile = models.CharField(max_length=11, verbose_name='手机号码')
    image = models.ImageField(upload_to='upload/%Y/%m', default='upload/default.jpg', verbose_name='用户头像')

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.get_full_name


class Knowledge(BaseModel):
    title = models.CharField(max_length=64, verbose_name='标题')
    detail = UEditorField(verbose_name='内容', imagePath='upload/img/', filePath='upload/files/')
