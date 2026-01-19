from django.contrib import admin
from .models import PlayerAttendance, User, UserPlayer

admin.site.site_header = "Academy Admin"
admin.site.register(User)
admin.site.register(UserPlayer)
admin.site.register(PlayerAttendance)
