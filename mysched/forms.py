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
    input_date = forms.DateField(widget=forms.DateInput(attrs={"type":"date"})