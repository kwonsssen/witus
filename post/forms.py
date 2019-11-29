from django import forms
from .models import Basket_Team, Basket_Team_Comment
#from choiceinput.widgets import ChoiceInput

class Basket_Team_Form(forms.ModelForm):


	#area = forms.ChoiceField(choices=SPORT_CHOICES, widget=forms.Select(attrs={'class': "form-control order-1"}))

	class Meta:
		model = Basket_Team
		fields = ['basket_team_name', 'date_time', 'discription', 'max_people', 'place']
		widgets={
			"basket_team_name":forms.TextInput(attrs={'placeholder':'팀명','class':'form-control order-1'}),
            "date_time":forms.DateTimeInput(format='%Y-%m-%d %H:%M' ,attrs={'class':'form-control order-1'}),
            "discription":forms.Textarea(attrs={'placeholder':'세부 일정 및 간단한 설명을 적어주세요','class':'form-control order-1'}),
            "max_people":forms.NumberInput(attrs={'placeholder':'세부 일정 및 간단한 설명을 적어주세요','class':'form-control order-1'}),
            "place":forms.TextInput(attrs={'placeholder':'경기장 명','class':'form-control order-1'}),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Basket_Team_Comment
        fields = ['text']

        widgets={
            "text":forms.Textarea(attrs={'placeholder':'배려와 매너가 밝은 커뮤니티를 만듭니다.','class':'form-control', 'id' : 'message-text', 'col':'0','rows':'0'}),
        }