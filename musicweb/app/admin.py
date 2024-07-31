from django.contrib import admin

# Register your models here.

##
from .models import User, Music, MarkedScore, MarkedClip, MarkedDimensionScore, AssignUserMusic

admin.site.register(User)
admin.site.register(Music)
admin.site.register(MarkedScore)
admin.site.register(MarkedClip)
admin.site.register(MarkedDimensionScore)
admin.site.register(AssignUserMusic)
##