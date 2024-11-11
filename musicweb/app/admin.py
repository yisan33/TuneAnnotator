from django.contrib import admin

# Register your models here.

##
from .models import User, Music, MarkedScore, MarkedClip, MarkedDimensionScore, AssignUserMusic, Music_Vocal, Music_Instrumental, DimensionScore, MusicEmotion

admin.site.register(User)
admin.site.register(Music)
admin.site.register(MarkedScore)
admin.site.register(MarkedClip)
admin.site.register(MarkedDimensionScore)
admin.site.register(AssignUserMusic)
admin.site.register(Music_Vocal)
admin.site.register(Music_Instrumental)
admin.site.register(DimensionScore)
admin.site.register(MusicEmotion)
##