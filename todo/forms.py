from django import forms
from .models import Todos


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = ['todo', 'detail']
        widgets = {
            'detail': forms.Textarea(attrs={'class': 'form-control'})
        }
