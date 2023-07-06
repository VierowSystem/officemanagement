from django.contrib import admin

from OfficeApp import models

admin.site.register(models.Login)
# admin.site.register(models.User)
admin.site.register(models.Stock)
admin.site.register(models.Account)
admin.site.register(models.Expense)

