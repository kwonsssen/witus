from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Basket_place, Place_Comment, Soccer_place,Foot_place
from .forms import CommentForm
from post.models import Basket_Team
import json
from django.views.decorators.http import require_http_methods


def main(request, context={}):
	team_list = Basket_Team.objects.all()
	fast_team_list = []
	# 3일 이내의 팀들만 골라낸다
	for i in team_list:
		if (i.date_time - timezone.localtime())<timezone.timedelta(3) and (i.date_time - timezone.localtime())>timezone.timedelta(0):
			fast_team_list.append(i)
	
			
	context['fast_team_list'] = fast_team_list
	return render(request, 'first/main.html', context)


def sport_map(request, context={}):
	board_basket = Basket_place.objects.all()
	board_Soccer = Soccer_place.objects.all()
	board_Foot = Foot_place.objects.all()
	if request.method == "POST":
		Basket_places = get_object_or_404(Basket_place, pk=request.POST.get('pk'))
		context['form'] = CommentForm(request.POST)
		if context['form'].is_valid():
			comment = context['form'].save(commit=False)
			comment.author = request.user
			comment.place = Basket_places
			comment.save()
			

	context['comments'] = Place_Comment.objects.all()
	context['form'] = CommentForm()

	context['place_list'] = board_basket
	context['soccer_place_list'] = board_Soccer
	context['foot_place_list'] = board_Foot
	return render(request, 'first/sport_map.html', context)

@require_http_methods("POST") # 포스트 method만 받음
def sport_place_select_ajax(request):
	place = request.POST.get('place', None)
	if place == "soccer":
		context = {'place': 'soccer_hidden'}
	elif place == "basket":
		context = {'place': 'basket_hidden'}
	elif place == "foot":
		context = {'place': 'foot_hidden'}
	return HttpResponse(json.dumps(context), content_type="application/json")

