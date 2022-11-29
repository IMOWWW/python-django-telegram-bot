from django.contrib import admin
from .models import Profile, Message, MessageMe
# Register your models here.



class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id","user_id","username","f_name","l_name"]


class MessageAdmin(admin.ModelAdmin):
    list_display = ["id","text"]

class MessageMeAdmin(admin.ModelAdmin):
    list_display = ["id", "profile", "messages"]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Message,MessageAdmin)
admin.site.register( MessageMe, MessageMeAdmin)