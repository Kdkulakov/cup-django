from django.contrib import admin
from userprofile.models import Userprofile, UserCategory, UserCompany
# Register your models here.
admin.site.register(Userprofile)
admin.site.register(UserCategory)
admin.site.register(UserCompany)