from django.contrib import admin
from user_auth.models import *
# Register your models here.
admin.site.register(customUserModel)
admin.site.register(PendingAccountModel)