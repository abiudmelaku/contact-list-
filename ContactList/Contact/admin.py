from django.contrib import admin
from .models import contact_lst,Account
# Register your models here.
class contact_admin(admin.ModelAdmin):
    list_display = ('first_name' , 'last_name' , 'phone_num')
    list_filter = ('first_name',)
class Account_admin(admin.ModelAdmin):
    list_filter = ('username',)
admin.site.register(contact_lst , contact_admin)
admin.site.register(Account , Account_admin)

