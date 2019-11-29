from django.shortcuts import render, redirect, get_object_or_404
from .forms import Basket_Team_Form, CommentForm
from .models import Basket_Team, Basket_member, Basket_team_maching, Basket_Team_Comment, Basket_team_maching_sinchung
from django.utils import timezone

def team_post(request, context={}):
	team_list = Basket_Team.objects.all()
	context['team_list'] = [] # 팀 내역
	# 기간이 지난건 안보여줌
	for i in team_list:
		if i.date_time > timezone.now():
			context['team_list'].append(i)

	members_model = Basket_member.objects.all()
	context['team_recommends'] = []
	context['jiwon_list'] = []
	context['team_maching_sinchung'] = []

	# 팀 매칭이 가능한 상태인지 확인하기 위해
	if str(request.user) != 'AnonymousUser':
		for i in Basket_Team.objects.filter(manager=request.user):
			for j in context['team_list']:
				# 내 팀이 아니고
				if i.manager != j.manager:
					# 일자가 같고
					if i.date_time.year == j.date_time.year and i.date_time.month == j.date_time.month and i.date_time.day == j.date_time.day:
						# 같은 구에 있는 팀이고
						if i.area_detail == j.area_detail and i.area == j.area:
							# 일정이 지나지 않은 팀들
							if i.date_time > timezone.now() and j.date_time > timezone.now():
								context['team_recommends'].append(j)
	# 신청한 팀이면 보이지 않기 위해
	tmp_list = []
	if str(request.user) != 'AnonymousUser':
		for i in Basket_team_maching_sinchung.objects.filter(request_user=request.user):
			tmp_list.append(i.team_1)
	context['team_recommends'] = list(set(context['team_recommends']) - set(tmp_list))

	# 로그인이 된 상태인지 확인, 지원한 상태인지 확인하기 위한 코드
	if str(request.user) != 'AnonymousUser':
		for i in Basket_Team.objects.all():
			maple = i.team_names.filter(user_name=request.user)
			if len(maple) != 0:
				context['jiwon_list'].append(i.pk)

	if request.method == "POST":
		#팀 생성경우
		context['form'] = Basket_Team_Form(request.POST)
		if context['form'].is_valid():
			basket = context['form'].save(commit=False)
			basket.basket_team_name = request.POST['basket_team_name']
			basket.manager = request.user
			basket.area = request.POST['submit'].split("|")[0]
			basket.area_detail = request.POST['submit'].split("|")[1]
			basket.date_time = request.POST['date_time']
			basket.discription = request.POST['discription']
			basket.max_people = request.POST['max_people']
			basket.place = request.POST['place']
			basket.level_pass = request.user.user_of.basket_pass_level
			basket.level_shoot = request.user.user_of.basket_shoot_level
			basket.level_dribble = request.user.user_of.basket_dribble_level
			basket.level_defense = request.user.user_of.basket_defense_level
			basket.save()
			return redirect('team_post')

		

	context['form'] = Basket_Team_Form()
	return render(request, 'post/team_post.html', context)

def team_cancel(request):
	# 팀 탈퇴하기 경우
	if request.method == "POST":
		if request.POST['jiwon_cancel']:
			Basket_team_pk = get_object_or_404(Basket_Team, pk=request.POST['jiwon_cancel'])
			Basket_member_pk = Basket_member.objects.filter(basket_team_names=request.POST['jiwon_cancel']).filter(user_name = request.user)
			Basket_member_pk.delete()
			
			

			Basket_team_pk.level_pass = int((Basket_team_pk.level_pass * Basket_team_pk.people_count - request.user.user_of.basket_pass_level)/ Basket_team_pk.people_count-1)
			Basket_team_pk.level_shoot = int((Basket_team_pk.level_shoot * Basket_team_pk.people_count - request.user.user_of.basket_shoot_level)/ Basket_team_pk.people_count-1)
			Basket_team_pk.level_dribble = int((Basket_team_pk.level_dribble * Basket_team_pk.people_count - request.user.user_of.basket_dribble_level)/ Basket_team_pk.people_count-1)
			Basket_team_pk.level_defense = int((Basket_team_pk.level_defense * Basket_team_pk.people_count - request.user.user_of.basket_defense_level)/ Basket_team_pk.people_count-1)

			if Basket_team_pk.level_pass < 0:
				Basket_team_pk.level_pass = 0
			if Basket_team_pk.level_shoot < 0:
				Basket_team_pk.level_shoot = 0
			if Basket_team_pk.level_dribble < 0:
				Basket_team_pk.level_dribble = 0
			if Basket_team_pk.level_defense < 0:
				Basket_team_pk.level_defense = 0

			Basket_team_pk.people_count = Basket_team_pk.people_count -1 # 팀원 수 줄이기

			Basket_team_pk.save()
			return redirect(request.POST['url'])



# 팀 설명 세부 페이지 
def team_post_detail(request, pk, context={}):
	team_post = get_object_or_404(Basket_Team, pk=pk)
	basket_comment_filter = Basket_Team_Comment.objects.filter(team_name=pk)
	besket_members = Basket_member.objects.all()

	context['jiwon_list'] = []
	# 로그인이 된 상태인지 확인, 지원한 상태인지 확인하기 위한 코드
	if str(request.user) != 'AnonymousUser':
		for i in Basket_Team.objects.all():
			maple = i.team_names.filter(user_name=request.user)
			if len(maple) != 0:
				context['jiwon_list'].append(i.pk)
	
	# 팀원들 리스트를 만듦	
	members = []
	for i in besket_members:
		if i.basket_team_names == team_post:
			members.append(i)

	# 댓글 달기
	if request.method == "POST":
		#Basket_places = get_object_or_404(Basket_place, pk=request.POST.get('pk'))
		context['form'] = CommentForm(request.POST)
		if context['form'].is_valid():
			comment = context['form'].save(commit=False)
			comment.author = request.user
			comment.team_name = team_post
			comment.save()
			return  redirect('/team_post_detail/'+str(pk))
	
	context['comments'] = basket_comment_filter
	context['form'] = CommentForm()
	context['team_post'] = team_post
	context['basket_level'] = int((team_post.level_pass + team_post.level_shoot + team_post.level_dribble + team_post.level_defense)/4)
	context['members'] = members
	return render(request,'post/team_post_detail.html',context)



def team_jiwon(request):
	# 지원하기 경우
	if request.method == "POST":
		if request.POST['jiwon']:
			Basket_team_filter = Basket_member.objects.filter(basket_team_names=request.POST['jiwon']).filter(user_name = request.user)
			Basket_team_pk = get_object_or_404(Basket_Team, pk=request.POST['jiwon'])
			if len(Basket_team_filter) == 0 and Basket_team_pk.people_count < Basket_team_pk.max_people:
				Basket_members = Basket_member.objects.create(
					basket_team_names = Basket_team_pk, 
					user_name = request.user,
				)
				
				Basket_team_pk.level_pass = int((Basket_team_pk.level_pass * Basket_team_pk.people_count + request.user.user_of.basket_pass_level)/Basket_team_pk.people_count+1)
				Basket_team_pk.level_shoot = int((Basket_team_pk.level_shoot * Basket_team_pk.people_count + request.user.user_of.basket_shoot_level)/Basket_team_pk.people_count+1)
				Basket_team_pk.level_dribble = int((Basket_team_pk.level_dribble * Basket_team_pk.people_count + request.user.user_of.basket_dribble_level)/Basket_team_pk.people_count+1)
				Basket_team_pk.level_defense = int((Basket_team_pk.level_defense * Basket_team_pk.people_count + request.user.user_of.basket_defense_level)/Basket_team_pk.people_count+1)
				Basket_team_pk.people_count = Basket_team_pk.people_count + 1 # 팀원 수 늘리기
				Basket_team_pk.save()
			return redirect(request.POST['url'])

# 팀 매칭 1차 단계
def team_mach_request(request):
	if request.method == "POST":
		if request.POST['team_mach_request']:
			Basket_team_1 = get_object_or_404(Basket_Team, pk=request.POST['team_mach_request'])
			for i in Basket_Team.objects.filter(manager=request.user):
				if i.date_time.date() == Basket_team_1.date_time.date():
					jiwon_team = i
					break
			Basket_team_maching_sinchung.objects.create(
					team_1 = Basket_team_1, 
					team_2 = jiwon_team.basket_team_name,
					request_user = request.user,
				)
			return redirect(request.POST['url'])


# 팀 매칭 결정 단계
def team_mach_confirm(request):
	if request.method == "POST":
		if request.POST['team_mach_confirm']:
			success_request = get_object_or_404(Basket_team_maching_sinchung, pk=request.POST['team_mach_confirm'])
			success_request.success = True
			success_request.save()
			return redirect(request.POST['url'])


# 팀 매칭 취소
def team_mach_cancle(request):
	if request.method == "POST":
		if request.POST['team_mach_cancle']:
			success_request = get_object_or_404(Basket_team_maching_sinchung, pk=request.POST['team_mach_cancle'])
			success_request.success = False
			success_request.save()
			return redirect(request.POST['url'])