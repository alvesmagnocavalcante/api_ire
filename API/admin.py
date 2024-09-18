from django.contrib import admin
from .models import Bet, Center, Clasified, Schedule, Limit, Plan, Throw, User, Winner

# Register your models here.
admin.site.register(Bet)
admin.site.register(Center)
admin.site.register(Clasified)
admin.site.register(Schedule)
admin.site.register(Limit)
admin.site.register(Plan)
admin.site.register(Throw)
admin.site.register(User)
admin.site.register(Winner)
