from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils import timezone

class Basket_place(models.Model):
    title = models.CharField(verbose_name="title",max_length=40, null=False)
    x_coor = models.CharField(max_length=40, default=0, verbose_name=_('위도'))
    y_coor = models.CharField(max_length=40, default=0, verbose_name=_('경도'))
    address = models.CharField(verbose_name="주소", max_length=50)
    discription = models.TextField(verbose_name="설명")
    score = models.IntegerField(null=False, blank=False, default=0, verbose_name="평점")
    photo = models.ImageField(verbose_name=_('프로필 사진'), upload_to="first/%Y/%m/%d", blank=True, null=True)

    def __str(self):
        return self.title

class Soccer_place(models.Model):
    title = models.CharField(verbose_name="title",max_length=40, null=False)
    x_coor = models.CharField(max_length=40, default=0, verbose_name=_('위도'))
    y_coor = models.CharField(max_length=40, default=0, verbose_name=_('경도'))
    address = models.CharField(verbose_name="주소", max_length=50)
    discription = models.TextField(verbose_name="설명")
    score = models.IntegerField(null=False, blank=False, default=0, verbose_name="평점")
    photo = models.ImageField(verbose_name=_('프로필 사진'), upload_to="first/%Y/%m/%d", blank=True, null=True)

    def __str(self):
        return self.title

class Foot_place(models.Model):
    title = models.CharField(verbose_name="title",max_length=40, null=False)
    x_coor = models.CharField(max_length=40, default=0, verbose_name=_('위도'))
    y_coor = models.CharField(max_length=40, default=0, verbose_name=_('경도'))
    address = models.CharField(verbose_name="주소", max_length=50)
    discription = models.TextField(verbose_name="설명")
    score = models.IntegerField(null=False, blank=False, default=0, verbose_name="평점")
    photo = models.ImageField(verbose_name=_('프로필 사진'), upload_to="first/%Y/%m/%d", blank=True, null=True)

    def __str(self):
        return self.title
	


class Place_Comment(models.Model):  
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    place = models.ForeignKey(Basket_place, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text