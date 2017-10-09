from django.db import models

from django.db import models
from django.contrib import admin

# Create your models here.

class LockUser(models.Model):
    user = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    lock_id = models.CharField(max_length = 10)

class LockUse(models.Model):
    lock_id = models.CharField(max_length = 10)
    lock_state = models.CharField(max_length = 3, null=True)
    state = models.CharField(max_length = 2, null=True) #判断硬件是否执行成功
    last_use_time = models.DateTimeField(null=True)

class LockUserAdmin(admin.ModelAdmin):
    list_display = ('user','lock_id')
    search_fields = ('user','lock_id')

class LockUseAdmin(admin.ModelAdmin):
    list_display = ('lock_id','lock_state','last_use_time')
    search_fields = ('lock_id','lock_state')
    
admin.site.register(LockUser,LockUserAdmin)
admin.site.register(LockUse,LockUseAdmin)
