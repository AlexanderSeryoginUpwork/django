from django import forms

from .models import Category
from .models import News
import re
from django.core.exceptions import ValidationError

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(
                attrs={"class": "form-control"}
            ),
            'content': forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5
                },
            ),
            'category': forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Заголовок не должен начинаться с цифры')
        return title

    def clean_content(self):
        content = self.cleaned_data['content']
        if re.match(r'.*123456.*', content):
            raise ValidationError('Текст содержит недопустимые символы 123456')
        return content
