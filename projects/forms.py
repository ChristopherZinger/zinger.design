from django import forms
from .models import Project, ProjectImg


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'description',
            ]


class ProjectImgForm(forms.ModelForm):
    title = forms.CharField(label='Img Title')
    description = forms.CharField(widget=forms.Textarea(),label='Img Description')
    img = forms.ImageField(label='Image:')

    class Meta:
        model = ProjectImg
        fields = [ 
            'title',
            'description',
            'img',
        ]

class saveImgOrderForm(forms.Form):
    images = forms.CharField(widget=forms.Textarea)
    order = forms.CharField(widget=forms.Textarea)
    