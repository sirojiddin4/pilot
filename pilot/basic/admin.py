from django.contrib import admin
from .models import TestQuestion, Candidate, UserResponse

# Register your models here.
admin.site.register(TestQuestion)
admin.site.register(Candidate)
admin.site.register(UserResponse)
