from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from first.models import Basket_place

# 농구 팀(팀 구하는 게시판)
class Basket_Team(models.Model):
	basket_team_name = models.CharField(verbose_name="team_name",max_length=40, null=False)
	manager = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="매니저네임",  related_name='manager')
	area = models.CharField(verbose_name="지역1",max_length=40, null=True, blank=True,)
	area_detail = models.CharField(verbose_name="지역2",max_length=40, null=True, blank=True,)
	date_time = models.DateTimeField(default=timezone.now, verbose_name="일정")
	discription = models.TextField(verbose_name="설명")
	max_people = models.IntegerField(null=True, blank=True, default=0, verbose_name="모집인원")
	people_count = models.IntegerField(null=True, blank=True, default=1, verbose_name="현재 지원 인원")
	place = models.CharField(verbose_name="경기장",max_length=40)

	level_pass = models.IntegerField(null=True, blank=True, default=0, verbose_name="패스_수준")
	level_shoot = models.IntegerField(null=True, blank=True, default=0, verbose_name="슛_수준")
	level_dribble = models.IntegerField(null=True, blank=True, default=0, verbose_name="드리블_수준")
	level_defense = models.IntegerField(null=True, blank=True, default=0, verbose_name="수비_수준")
	
	def __str__(self):
		return self.basket_team_name


# 농구 팀원들
class Basket_member(models.Model):
    basket_team_names = models.ForeignKey(Basket_Team, on_delete=models.CASCADE, related_name='team_names')
    user_name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="용병_유저네임",  related_name='basket_member_user')
    
    

# 팀 매칭 신청 상태
class Basket_team_maching_sinchung(models.Model):
	team_1 = models.ForeignKey(Basket_Team, on_delete=models.CASCADE, verbose_name="팀_1", related_name="basket_sinchung")
	team_2 = models.CharField(verbose_name="팀_2", max_length=40, null=False, blank=False)
	success = models.BooleanField(default=False)
	request_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="유저네임",  related_name='mach_request_user') # 신청한 유저


# 팀 매칭 ( 사용 안함 )
class Basket_team_maching(models.Model):
	team_1 = models.ForeignKey(Basket_Team, on_delete=models.CASCADE, verbose_name="팀_1",  related_name='team_maching')
	team_2 = models.CharField(verbose_name="팀_2", max_length=40, null=False, blank=False)



class Basket_Team_Comment(models.Model):  
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="유저네임",  related_name='%(app_label)s_%(class)ss')
    team_name = models.ForeignKey(Basket_Team, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
	

