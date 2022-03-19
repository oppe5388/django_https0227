from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import HttpResponse, Http404 # 追記
from .models import MoneyTrans
from .forms import MoneyForm
from datetime import date, datetime


def mysched(request):

    moneyForm = MoneyForm(request.GET)

    context = {
        'moneyForm': MoneyForm,
    }

    if moneyForm.is_valid():
        input_date = moneyForm.cleaned_data['input_date']
        
        if input_date:
            #入力日以降のクエリセットの1つ目
            past_sched = MoneyTrans.objects.filter(entry__gte=input_date).order_by('entry').first()
            context['past_sched'] = past_sched
            context['input_date'] = input_date

    else:
        moneyForm = MoneyForm()
        #今日以降のクエリセット
        moneytrans = MoneyTrans.objects.filter(deadline__gte=date.today()).order_by('deadline')

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