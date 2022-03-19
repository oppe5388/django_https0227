from django import forms
from .models import MoneyTrans
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from datetime import date, datetime

# #メイン
# class MoneyForm(LoginRequiredMixin, forms.ModelForm):

# class BookForm(ModelForm):
#     """書籍のフォーム"""
#     class Meta:
#         model = Book
#         fields = ('name', 'publisher', 'page', )


#検索
class MoneyForm(LoginRequiredMixin, forms.Form):
    date_field = forms.DateField(
        widget=forms.DateInput(attrs={"type":"date"})
    )
    keyword = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    keyword2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))


    published_date = forms.DateTimeField(
        label='発刊日',
        required=True,
        widget=forms.DateInput(attrs={"type": "date"}),
        input_formats=['%Y-%m-%d']
    )
    