from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import UserCreationForm, LoginForm, CustomUserChangeForm, UserUpdateForm
from django.contrib.auth import login, get_user_model, authenticate, update_session_auth_hash, logout
from django.utils import timezone
from .models import Profile
from django.contrib.auth.hashers import check_password
from post.models import Basket_Team, Basket_team_maching_sinchung
from django.views.decorators.http import require_http_methods
import json

# 회원가입
def signup(request,context={}):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            context['form'] = form

    if request.method =="GET":
        form = UserCreationForm()
        context['form']=form

    return render(request, 'account/signup.html', context)


def login_func(request):
    if 'user_id' in request.POST:
        user_id = request.POST['user_id']
        password = request.POST['password']
        
    else:
        user_id = False
        password = False
    user= authenticate(request, user_id=user_id,password=password)
    if user is not None:
        login(request, user)
        user = get_user_model().objects.get(pk=request.user.id)
        user.last_login=timezone.now
        
        return ''
    else:
        return '아이디/비밀번호가 틀렸습니다.'

def signin(request,context={}):
    if request.method == "POST":        
        form = LoginForm(request.POST)
        context['error']= login_func(request)
        return redirect('/')
    form = LoginForm()
    context['form'] = form

    return render(request, 'account/signin.html', context)

def logouts(request):
    logout(request)
    return redirect('/')


def my_page(request,context={}):
    if request.method == "POST":
        # password change, 비밀번호 변경
        if request.POST['info_change'] == 'password_change':
            
            current_password = request.POST.get("origin_password")
            user = request.user
            if check_password(current_password,user.password):
                new_password = request.POST.get("password1")
                password_confirm = request.POST.get("password2")
                if new_password == password_confirm:
                    user.set_password(new_password)
                    user.save()
                    return redirect("/signin")
                else:
                    context.update({'error':"새로운 비밀번호를 다시 확인해주세요."})
        

        # updating, 정보 변경
        elif request.POST['info_change'] == 'info_change':
            user_change_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
            if user_change_form.is_valid():
                user_change_form.save()
            return redirect('/my_page')
    else:
        context['author'] = request.user
        # editting
        data ={
        'address':request.user.address,
        'Photo':request.user.Photo,
        'kakao_id':request.user.kakao_id,
        'basket_pass_level':request.user.user_of.basket_pass_level,
        'basket_shoot_level':request.user.user_of.basket_shoot_level,
        'basket_dribble_level':request.user.user_of.basket_dribble_level,
        'basket_defense_level':request.user.user_of.basket_defense_level,
        }
        user_change_form = UserUpdateForm(initial=data)
        context['user_change_form'] = user_change_form
        context['basket_total_level'] = int(request.user.user_of.basket_pass_level +request.user.user_of.basket_shoot_level +request.user.user_of.basket_dribble_level+request.user.user_of.basket_defense_level)/4

    return render(request, 'account/my_page.html', context)



def my_page_shinchung(request, context={}):
    # 팀 매칭 신청을 받은 리스트
    context['basket_sinchung_list'] = []
    context['sinchung_sucess'] = {}
    for i in Basket_team_maching_sinchung.objects.all():
        if str(i.team_1.manager) == str(request.user):
            if i.team_1.date_time > timezone.now():
                context['basket_sinchung_list'].append(i)
            if i.success == True and len(context['sinchung_sucess'])==0:
                context['sinchung_sucess'] = {'success':True, 'id':i.team_2}
        

    # 지원 현황
    context['basket_jiwon_list'] = []
    # 로그인이 된 상태인지 확인, 지원한 상태인지 확인하기 위한 코드
    for i in Basket_Team.objects.all():
        maple = i.team_names.filter(user_name=request.user)
        if len(maple) != 0 or i.manager == request.user:
            context['basket_jiwon_list'].append(i)
    return render(request, 'account/shinchung_list.html', context)


# 지원 리스트를 넘겨주는 ajax
@require_http_methods("POST") # 포스트 method만 받음
def my_page_shinchung_list_ajax(request):
    basket_jiwon_list = []
    # 로그인이 된 상태인지 확인, 지원한 상태인지 확인하기 위한 코드
    
    for i in Basket_Team.objects.all():
        maple = i.team_names.filter(user_name=request.user)
        if len(maple) != 0 or i.manager == request.user:
            basket_jiwon_list.append(str(i.date_time.strftime("%Y")))
            basket_jiwon_list.append(str(i.date_time.strftime("%m")))
            basket_jiwon_list.append(str(i.date_time.strftime("%d")))
            basket_jiwon_list.append(str(i))
            basket_jiwon_list.append(i.pk)

    context = {'jiwon_list': basket_jiwon_list}
    return HttpResponse(json.dumps(context), content_type="application/json")