from django import forms
from .models import Place_Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Place_Comment
        fields = ['text']

        widgets={
            "text":forms.Textarea(attrs={'placeholder':'배려와 매너가 밝은 커뮤니티를 만듭니다.','class':'form-control', 'id' : 'message-text'}),
        }