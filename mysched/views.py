from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import HttpResponse, Http404 # 追記

# Create your views here.

def mysched(request):
    return render(request, "mysched/mysched.html")
    # return HttpResponse('書籍の一覧')



def SerialToDateTime(serialVal:float) -> str:
    """日付シリアル値からyyyy/MM/dd HH:MM:ss 形式に変換
    Args:
        serialVal (float): シリアル値(Ex: 44434.3412172569)
    Returns:
        str: 時刻  yyyy/MM/dd HH:MM:ss 形式
    """      
    sDateTime = (datetime(1899,12,30) + timedelta(serialVal)).strftime('%Y/%m/%d %H:%M:%S')

    return sDateTime