from django import forms
from django.contrib.auth import get_user_model
from .models import Profile, User
from django.core.validators import RegexValidator


class LoginForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields=['user_id','password']
        widgets = {
        	'user_id':forms.TextInput(attrs={
				'class':'form-control order-1',
				}),
            'password':forms.PasswordInput(attrs={
				'class':'form-control order-1',
				}),
			
		}
# 회원가입 폼
class UserCreationForm(forms.ModelForm):
	password1 = forms.CharField(
		label = 'Password',
		widget = forms.PasswordInput(attrs={'class':'form-control order-1','placeholder':'password',})
	)

	password2 = forms.CharField(
		label = 'Password Confirmation',
		widget = forms.PasswordInput(attrs={'class':'form-control order-1','placeholder':'password',})
	)

	

	class Meta:
		model = get_user_model()
		fields = ['user_id','nickname','address','birth', 'kakao_id']
		widgets = {
			'user_id':forms.TextInput(attrs={
				'class':'form-control order-1',
				}),
			'nickname':forms.TextInput(attrs={
				'class':'form-control order-1',
				}),
			'address':forms.TextInput(attrs={
				'class':'form-control order-1',
				'placeholder':'ex) 서울특별시 강남구'
				}),
			'birth':forms.DateInput(attrs={
				'class':'form-control order-1',
				}),
			'kakao_id':forms.TextInput(attrs={
				'class':'form-control order-1',
				'placeholder':'ex) 카카오톡 아이디'
				}),
		}

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
			Profile.objects.create(user=user)
		return user



class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['Photo', 'address', 'kakao_id']
        widgets = {
			'Photo':forms.FileInput(attrs={
				'class':'form-control order-1',
				}),
			'address':forms.TextInput(attrs={
				'class':'form-control order-1',
				}),
			'kakao_id':forms.TextInput(attrs={
				'class':'form-control order-1',
				}),
		}
	

#정보 수정 폼
class UserUpdateForm(forms.ModelForm):
	address = forms.CharField(widget=forms.TextInput(
		attrs={'class':'form-control order-1'
		}), required=False,
	)

	kakao_id= forms.CharField(max_length=11, widget= forms.TextInput(attrs={
        'class':'form-control order-1',
        }),required=False)

	basket_pass_level = forms.IntegerField(widget= forms.NumberInput(attrs={
        'class':'form-control order-1',
        }),required=False, min_value = 0, max_value = 100)

	basket_shoot_level = forms.IntegerField(widget= forms.NumberInput(attrs={
        'class':'form-control order-1',
        }),required=False, min_value = 0, max_value = 100)

	basket_dribble_level = forms.IntegerField(widget= forms.NumberInput(attrs={
        'class':'form-control order-1',
        }),required=False, min_value = 0, max_value = 100)

	basket_defense_level = forms.IntegerField(widget= forms.NumberInput(attrs={
        'class':'form-control order-1',
        }),required=False, min_value = 0, max_value = 100)

	
	class Meta:
		model = get_user_model()
		fields = ['Photo']
		widgets = {
			'Photo':forms.FileInput(
				attrs={
				'class':'form-control order-1',
				
			}),
		}

	def __init__(self, *args, **kwargs):
		super(UserUpdateForm, self).__init__(*args, **kwargs)

	def clean(self):
		return self.cleaned_data

	def save(self, commit=True):
		user = self.instance
		address = self.cleaned_data['address']
		photo = self.cleaned_data['Photo']
		kakao_id = self.cleaned_data['kakao_id']
		basket_pass_level = self.cleaned_data['basket_pass_level']
		basket_shoot_level = self.cleaned_data['basket_shoot_level']
		basket_dribble_level = self.cleaned_data['basket_dribble_level']
		basket_defense_level = self.cleaned_data['basket_defense_level']
		print('ddddsadsa')
		if photo:
			user.Photo = photo
		if address:
			user.address=address
		if kakao_id:
			user.kakao_id=kakao_id
		if basket_pass_level:
			user.user_of.basket_pass_level = basket_pass_level
		if basket_shoot_level:
			user.user_of.basket_shoot_level = basket_shoot_level
		if basket_dribble_level:
			user.user_of.basket_dribble_level = basket_dribble_level
		if basket_defense_level:
			user.user_of.basket_defense_level = basket_defense_level
		if commit:
			user.user_of.save()
			user.save()
		return user