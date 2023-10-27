from django.contrib import admin
from users.models import *
# Register your models here.


admin.site.register(Roles)
admin.site.register(Systems)
admin.site.register(UsersRole)
admin.site.register(UsersSystem)