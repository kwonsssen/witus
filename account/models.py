from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from django_fields import DefaultStaticImageField # pip install django-default-imagefield

'''
def img_path(instance, filename): #파라미터 instance는 Photo 모델을 의미 filename은 업로드 된 파일의 파일 이름
    from random import choice
    import string # string.ascii_letters : ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr) # 8자리 임의의 문자를 만들어 파일명으로 지정
    extension = filename.split('.')[-1] # 배열로 만들어 마지막 요소를 추출하여 파일확장자로 지정
    # file will be uploaded to MEDIA_ROOT/user_<id>/<random>
    return '%s/%s.%s' % (instance.owner.username, pid, extension) # 예 : wayhome/abcdefgs.png
'''

class UserManager(BaseUserManager):
    def create_user(self, user_id, nickname, password=None):
        if not user_id:
            raise ValueError('Users must have an user_id address')

        user = self.model(
            user_id= self.model.normalize_username(user_id),
            nickname = nickname
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, nickname, password):
        user = self.create_user(
            user_id,
            password=password,
            nickname = nickname
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    #id
    user_id = models.CharField(
        verbose_name='id',
        max_length=30,
        unique=True,
    )

    #닉네임
    nickname = models.CharField(
        verbose_name=_('닉네임'),
        max_length=30,
        unique=True,
        blank=False,
    )

    #사진
    Photo = DefaultStaticImageField(verbose_name=_('프로필 사진'),
        upload_to= 'account/user_img/%Y/%m/%d',
        default='',
        blank=True,
        null=True,
        default_image_path='../static/img/basic_image.png')

    #지역
    address = models.CharField(
        verbose_name=_('Address'),
        max_length=30,
        blank=True,
    )

    #생년월일
    birth = models.DateField(
        verbose_name=_('birth'),
        default=timezone.now,
        )

    # 카카오톡 아이디
    kakao_id = models.CharField(
        verbose_name=_('kakao_id'),
        max_length=30,
        blank=True,
        null=True,
    )


    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.user_id

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin



class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user_of',
    )

    #농구 패스 수준
    basket_pass_level = models.IntegerField(
        verbose_name=_('basket_pass_level'),
        default=0
    )

    #농구 슛 수준
    basket_shoot_level = models.IntegerField(
        verbose_name=_('basket_shoot_level'),
        default=0
    )

    #농구 드리블 수준
    basket_dribble_level = models.IntegerField(
        verbose_name=_('basket_dribble_level'),
        default=0
    )

    #농구 수비 수준
    basket_defense_level = models.IntegerField(
        verbose_name=_('basket_defense_level'),
        default=0
    )


    #축구 패스 수준
    soccer_pass_level = models.IntegerField(
        verbose_name=_('soccer_pass_level'),
        default=0
    )

    #축구 슛 수준
    soccer_shoot_level = models.IntegerField(
        verbose_name=_('soccer_shoot_level'),
        default=0
    )

    #축구 드리블 수준
    soccer_dribble_level = models.IntegerField(
        verbose_name=_('soccer_dribble_level'),
        default=0
    )

    #축구 수비 수준
    soccer_defense_level = models.IntegerField(
        verbose_name=_('soccer_defense_level'),
        default=0
    )

    
    #족구 리시브 수준
    foot_receive_level = models.IntegerField(
        verbose_name=_('foot_receive_level'),
        default=0
    )

    #족구 공격 수준
    foot_attack_level = models.IntegerField(
        verbose_name=_('foot_attack_level'),
        default=0
    )