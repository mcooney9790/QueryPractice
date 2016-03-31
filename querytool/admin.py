from django.contrib import admin
from .models import Cities, Comedians, LessonQuestions, Club, Rapper, Album, NightClub
# Register your models here.


admin.site.register(Cities)
admin.site.register(Comedians)
admin.site.register(Club)
admin.site.register(Rapper)
admin.site.register(Album)
admin.site.register(NightClub)
admin.site.register(LessonQuestions)


