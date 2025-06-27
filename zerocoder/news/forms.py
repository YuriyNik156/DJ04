from .models import News_post
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class New_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text', 'pub_date']
        widgets = {
            'title' : TextInput(attrs={'class':'form-control', 'placeholder':'Введите заголовок'}),
            'short_description' : TextInput(attrs={'class':'form-control', 'placeholder':'Введите краткое описание'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст новости'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Введите дату публикации'}),
        }
