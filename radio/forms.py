from django import forms
from .models import Show, Audio, Category


CATEGORY_CHOICES = Category.objects.all().values_list('name', 'name')
category_list = []
for item in CATEGORY_CHOICES:
    category_list.append(item)

FILE_TYPE_CHOICES = [
    ('MP3', 'MP3'),
    ('AAC', 'AAC'),
    ('WAV', 'WAV'),
    ]


class ShowCreateForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ['show_name', 'category', 'show_logo']
        widgets = {
            'category': forms.Select(choices=category_list),
        }


class ShowUpdateForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ['show_name', 'category', 'show_logo',]
        widgets = {
            'category': forms.Select(choices=category_list),
        }


class AudioCreateForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['file_title', 'description', 'file_type']
        widgets = {
            'file_type': forms.Select(choices=FILE_TYPE_CHOICES),
        }
