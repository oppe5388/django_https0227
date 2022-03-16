from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import os

class MoneyTrans(models.Model):
    # transfer = models.CharField(max_length=100, verbose_name="送金日")
    # deadline = models.CharField(max_length=100, verbose_name="到着締切")
    # entry = models.CharField(max_length=100, verbose_name="登録日")
    # fix = models.CharField(max_length=100, verbose_name="承認日")
    # setoff = models.CharField(max_length=100, verbose_name="相殺締切")

    # transfer = models.FloatField(verbose_name="送金日")
    # deadline = models.FloatField(verbose_name="到着締切")
    # entry = models.FloatField(verbose_name="登録日")
    # fix = models.FloatField(verbose_name="承認日")
    # setoff = models.FloatField(verbose_name="相殺締切")

    transfer = models.DateTimeField(verbose_name="送金日")
    deadline = models.DateTimeField(verbose_name="到着締切")
    entry = models.DateTimeField(verbose_name="登録日")
    fix = models.DateTimeField(verbose_name="承認日")
    setoff = models.DateTimeField(verbose_name="相殺締切")

    def __str__(self):
        return self.transfer

    class Meta:
        verbose_name_plural = "送金スケジュール"