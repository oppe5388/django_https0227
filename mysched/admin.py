from django.contrib import admin
from .models import *

from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
    
class MoneyTransResource(ModelResource):
    class Meta:
        model = MoneyTrans
        import_order = ('id', 'transfer', 'deadline', 'entry', 'fix', 'setoff')
        # import_id_fields = ['id']

#お知らせインポート、エクスポート
class MoneyTransAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'transfer', 'deadline', 'entry', 'fix', 'setoff')
    resource_class = MoneyTransResource

admin.site.register(MoneyTrans, MoneyTransAdmin)