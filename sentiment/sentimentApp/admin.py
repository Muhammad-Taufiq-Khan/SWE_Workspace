from django.contrib import admin

# Register your models here.
from sentimentApp.models import *
admin.site.register(Client)
admin.site.register(File)
admin.site.register(Result)


