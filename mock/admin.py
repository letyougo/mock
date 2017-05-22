from django.contrib import admin

# Register your models here.
from mock.models import *
admin.site.register(Project)
admin.site.register(Table)
admin.site.register(Colnum)
admin.site.register(Row)