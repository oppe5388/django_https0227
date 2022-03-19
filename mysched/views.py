from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import HttpResponse, Http404 # 追記
from .models import MoneyTrans
from .forms import MoneyForm

def mysched(request):

    moneyForm = MoneyForm(request.GET)

    context = {
        'moneyForm': moneyForm,
    }

    if moneyForm.is_valid():
        queryset = MoneyTrans.objects.all()
        keyword = moneyForm.cleaned_data['keyword']
        if keyword:
            queryset = queryset.filter(title__icontains=k).order_by('-id')#

            context['moneytrans'] = queryset
    else:
        moneyForm = MoneyForm()
        moneytrans = MoneyTrans.objects.filter(deadline__gte=date.today()).order_by('deadline')#以上の場合
        context['moneytrans'] = moneytrans

        

    # #通知（有無だけ）
    # if request.user.id is not None:
    #     notifi_exis =  Notifications.objects.filter(user=request.user).exists()

    #     #既読も
    #     # my_unread = ReadStates.objects.all().filter(user=request.user)
    #     unread_set = ReadStates.objects.all()

    #     #contextは辞書型、context['weather'] = '晴れ'、でkeyがweather、valueが晴れというデータを追加
    #     context['notifi_exis'] = notifi_exis
    #     context['unread_set'] = unread_set


    return render(request, "mysched/mysched.html", context)



    # Model.objects.filter(field__gt='value') #大きい場合
    # model.objects.filter(field__gte='value') #以上の場合
    # Model.objects.filter(field__lt='value') #未満の場合
    # model.objects.filter(field__lte='value') #以下の場合


    #入力日が、entryの日以上のQueryセットをとって、その1番上
    # p = Article.objects.order_by('title', 'pub_date').first()